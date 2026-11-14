import os
import time

import PyPDF2
import torch
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIRS = [os.path.join(PROJECT_ROOT, 'Data'), os.path.join(PROJECT_ROOT, 'data')]
VECTORSTORE_DIR = os.path.join(PROJECT_ROOT, 'vectorstore')

print('Loading model ...')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
embeddings = HuggingFaceEmbeddings(model_name='multi-qa-mpnet-base-dot-v1', model_kwargs={'device': device})

print('Processing text ...')
document_path = None
for directory in DATA_DIRS:
    candidate = os.path.join(directory, 'ipc_law.pdf')
    if os.path.exists(candidate):
        document_path = candidate
        break

if document_path is None:
    raise FileNotFoundError("PDF not found. Place ipc_law.pdf inside the Data/ directory.")

reader = PyPDF2.PdfReader(document_path)
text = ''
for page in reader.pages:
    extracted = page.extract_text() or ''
    text += extracted

text_splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size=512,
    chunk_overlap=64,
    length_function=len,
)
chunks = text_splitter.split_text(text)

time1 = time.time()
print('Storing embedding ...')
vectordb = FAISS.from_texts(chunks, embeddings)
vectordb.save_local(VECTORSTORE_DIR)
print('Time required : ', time.time() - time1)
