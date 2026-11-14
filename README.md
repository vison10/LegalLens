# ⚖️ LegalLens – AI-Powered Indian Legal Assistant

<div align="center">

### Your Intelligent Companion for Understanding Indian Law
**Developed by Ansh Sharma**

LegalLens is a Retrieval-Augmented Generation (RAG) chatbot built to answer Indian legal questions using local language models and legal document context.

</div>

---

## About the Project
LegalLens helps users ask natural-language questions about Indian law and receive grounded answers based on relevant legal document chunks. The application combines:

- document ingestion
- semantic retrieval using FAISS
- local LLM inference with Llama 2
- a simple Streamlit-based chat interface

This makes it easier to explore legal information without manually reading long PDFs.

## Key Features

- Legal question answering in natural language
- Retrieval-Augmented Generation (RAG) pipeline
- Semantic similarity search over legal text chunks
- Local Llama 2 model support
- PDF-based legal document ingestion
- Streamlit chat interface
- GPU acceleration support when available

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- Llama 2 / Llama.cpp
- PyPDF2
- PyTorch

## How It Works

### 1. Document Ingestion
1. A legal PDF is loaded from the `Data` directory.
2. The PDF text is extracted with PyPDF2.
3. Text is split into smaller chunks.
4. Hugging Face embeddings are generated for each chunk.
5. FAISS stores the vectors for similarity search.

### 2. Question Answering
1. The user asks a question in the Streamlit app.
2. The app uses the vector database to retrieve the most relevant legal text chunks.
3. The retrieved context is passed to the local Llama 2 model.
4. The model produces a short answer grounded in the retrieved context.

## Project Structure

```text
LegalLens-India/
├── Data/
│   └── ipc_law.pdf
├── Models/               # create this folder and place gguf model files here
│   ├── llama-2-7b-chat.Q4_K_M.gguf
│   └── llama-2-13b-chat.Q4_K_M.gguf
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
├── app.py
├── ingest.py
├── htmlTemplates.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.9+
- pip
- Git
- At least 8 GB RAM recommended
- NVIDIA GPU optional for faster inference

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vison10/LegalLens.git
cd LegalLens
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the Models folder
Create a folder named `Models` in the project root and download the Llama 2 GGUF files into it.

Examples:

- `Models/llama-2-7b-chat.Q4_K_M.gguf`
- `Models/llama-2-13b-chat.Q4_K_M.gguf`

Download links:

- [Llama 2 7B Chat GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
- [Llama 2 13B Chat GGUF](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF)

### 4. Prepare legal documents
Keep the legal PDFs inside the `Data` folder.

The default script expects:

```text
Data/ipc_law.pdf
```

### 5. Generate the vector database

```bash
python ingest.py
```

This loads the PDF, splits it into chunks, creates embeddings, and stores the FAISS index in `vectorstore/`.

### 6. Run the app

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Using the App

1. Start the Streamlit app.
2. Select the Llama 2 model version from the sidebar.
3. Enter a legal question in the chat box.
4. Wait for the RAG pipeline to retrieve relevant context and generate an answer.

## Notes

- The repository uses `Data/` with a capital `D` for legal documents.
- The `Models/` directory is created manually and is not uploaded to Git by default.
- If you are on Linux/macOS, keep the folder and file names case-sensitive.

## Disclaimer
This project is intended for educational and informational use. It is not a substitute for professional legal advice. For legal matters, consult a qualified lawyer or legal professional.

## License
This project is distributed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Built with  by Ansh Sharma
**LegalLens – Making Indian Law Easier to Understand**

</div>
