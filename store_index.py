from src.helper import load_pdf, text_split, download_embeddings
from langchain_community.vectorstores import FAISS
import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

extracted_data = load_pdf('/Users/kushalbanda/Generative AI/End-to-End-Medical-Chatbot/Data')
text_chunks = text_split(extracted_data)
embeddings = download_embeddings()

docsearch = FAISS.load_local("/Users/kushalbanda/Generative AI/End-to-End-Medical-Chatbot/Code/faiss_index", embeddings)