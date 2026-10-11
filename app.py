import os
from pathlib import Path

import joblib
import numpy as np
import requests
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity


PROJECT_ROOT = Path(__file__).resolve().parent
INDEX_PATH = PROJECT_ROOT / "embeddings.joblib"
OLLAMA_URL = "http://localhost:11434"


@st.cache_resource
def load_index():
    return joblib.load(INDEX_PATH)


def ollama_embed(text):
    response = requests.post(
        f"{OLLAMA_URL}/api/embed",
        json={"model": "bge-m3", "input": [text]},
        timeout=300,
    )
    response.raise_for_status()
    return response.json()["embeddings"][0]


def ollama_generate(prompt):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "llama3.2", "prompt": prompt, "stream": False},
        timeout=300,
    )
    response.raise_for_status()
    return response.json()["response"]


def build_prompt(question, results):
    context = results[["title", "number", "start", "end", "text"]].to_json(
        orient="records"
    )
    return f"""You are a helpful HTML teaching assistant. Use only the transcript chunks below.
Answer the student's question clearly. Mention the relevant video title and timestamp.
If the question is unrelated to these lectures, say that you can only answer questions
about the provided lecture content.

Transcript chunks:
{context}

Student question: {question}
"""


st.set_page_config(page_title="HTML Lecture Assistant", page_icon="HT", layout="wide")
st.title("HTML Lecture Assistant")
st.caption("Search your lecture transcripts with local Ollama models.")

try:
    index = load_index()
except Exception as error:
    st.error(f"Could not load the embedding index: {error}")
    st.stop()

with st.sidebar:
    st.subheader("Lecture library")
    st.metric("Transcript chunks", len(index))
    st.metric("Videos", index["title"].nunique())
    st.caption("Models: bge-m3 + llama3.2")

question = st.text_input(
    "Ask a question about the lectures",
    placeholder="For example: What is HTML boilerplate code?",
)

if st.button("Ask Ollama", type="primary", disabled=not question.strip()):
    with st.spinner("Searching the lecture library..."):
        try:
            question_embedding = ollama_embed(question.strip())
            similarities = cosine_similarity(
                np.vstack(index["embedding"]), [question_embedding]
            ).flatten()
            result_indexes = similarities.argsort()[::-1][:4]
            results = index.iloc[result_indexes]
            answer = ollama_generate(build_prompt(question.strip(), results))
        except requests.RequestException as error:
            st.error(f"Ollama is unavailable at {OLLAMA_URL}: {error}")
            st.stop()

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Relevant lecture moments")
    for _, result in results.iterrows():
        start = int(result["start"])
        minutes, seconds = divmod(start, 60)
        st.markdown(
            f"**{result['title']}**  \n"
            f"Timestamp: `{minutes:02d}:{seconds:02d}`  \n"
            f"{result['text'].strip()}"
        )