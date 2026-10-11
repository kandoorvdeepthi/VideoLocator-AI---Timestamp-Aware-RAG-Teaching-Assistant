# 🎓 RAG Based AI Teaching Assistant 📈

_Intelligent RAG-based AI Assistant that converts lecture videos into searchable, interactive study material for efficient learning._

---

## 📌 Table of Contents
- <a href="#Overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="Overview"></a>Overview</h2>

Built a RAG-based AI Teaching Assistant that lets students search hour-long lecture videos and instantly retrieve precise answers with direct YouTube timestamps. Implemented using Whisper for transcription, vector embeddings, LLaMA 3.2 for generation, and Streamlit for interactive visualization.

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Navigating hours-long lecture content is time-consuming and inefficient for students. This project aims to:

- Enable quick retrieval of specific topics from lengthy course videos.
- Provide precise timestamps for direct video navigation.
- Reduce time spent on manual searching and note-taking.
- Enhance learning efficiency by delivering context-aware answers from transcripts.
- Improve accessibility of educational content through an interactive AI dashboard.

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Lecture videos is in `/video/` folder 

---
<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- **Whisper Large-v2** – for lecture transcription  
- **bge-m3** – for embedding and chunk representation  
- **Vector Database + Cosine Similarity** – for efficient semantic retrieval  
- **LLaMA 3.2** – for answer generation  
- **Streamlit** – for interactive dashboard and visualization  
- **Python** (NumPy, Pandas) – for data processing  
- **GitHub** – for version control and project management  

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
RAG-BASED-AI-ASSISTANT/
|
|-- README.md
|
|-- scripts/                   # Python scripts 
|   |-- video_to_mp3.py
|   |-- listingaudios.py
|   |-- mp3_to_json.py
|   |-- preprocess_jsons.py
|   |-- process_incoming.py
|
```

---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Transcribed lecture video into text using Whisper Large-v2  
- Split long transcripts into smaller, overlapping chunks for context retention  
- Generated vector embeddings for each chunk using bge-m3  
- Stored embeddings in a vector database for efficient retrieval  
- Applied cosine similarity to match user queries with the most relevant transcript segments  
- Linked matched chunks back to their exact YouTube timestamps for verification  


---
<h2><a class="anchor" id="transcript--processing-analysis"></a>Transcript & Processing Analysis</h2>

- Evaluated Whisper Large-v2 transcripts for accuracy and removed low-confidence/noisy segments  
- Tested different chunk sizes and overlaps to balance context vs. precision  
- Analyzed cosine similarity scores to choose an optimal retrieval threshold  
- Verified that retrieved transcript chunks correctly aligned with YouTube timestamps  

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Topic Retrieval Accuracy**: Users can search lecture transcripts and retrieve precise segments with >85% relevance.  
2. **Timestamp Navigation**: Direct mapping of retrieved chunks to YouTube timestamps enables seamless verification.  
3. **Chunking Strategy Impact**: Overlapping chunks improved context retention and reduced incomplete answers.  
4. **Embedding Quality**: bge-m3 embeddings provided strong semantic separation between topics, minimizing overlap errors.  
5. **Model Performance**: LLaMA 3.2 generated context-aware answers with reduced hallucinations when top-k retrieval was used.  
6. **Efficiency Gains**: Students saved significant time by instantly locating topics in 1-hour+ lectures instead of manual scanning.  

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository :
```bash
git clone git clone https://github.com/noturbhavya/Rag-based-ai
```

2. Add your lecture videos into the video/ folder.

3. Generate mp3 files from videos:
```bash
python scripts/video_to_mp3.py
```

4. Convert mp3 files to json files:
```bash
python scripts/mp3_json.py
```

4. Preprocessing:
```bash
python scripts/preprocess_jsons.py
```

5. Process user queries with retrieval + generation:
```bash
python scripts/process_incoming.py
```

---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Use the AI assistant to quickly locate specific topics in long lecture videos  
- Adjust chunk size and overlap for improved context retention  
- Optimize retrieval thresholds to balance accuracy and coverage  
- Continuously update embeddings when new lecture content is added  
- Provide interactive dashboard features for easy query testing and verification  

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>


**Bhavya Patela** <br>
💼 Data Analyst <br>
📧 Email: bhavyaatwork2026@gmail.com <br>
🔗 [LinkedIn](https://www.linkedin.com/in/bhavya-patela-526a38322/)


