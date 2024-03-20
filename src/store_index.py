from src.helper import load_pdf, text_split, download_embeddings
from langchain.vectorstore import FAISS
from dotenv import load_dotenv
load_dotenv()

extracted_data = load_pdf('../Data/')
text_chunks = text_split(extracted_data)
embeddings = download_embeddings()

docsearch = FAISS.load_local("faiss_index", embeddings)