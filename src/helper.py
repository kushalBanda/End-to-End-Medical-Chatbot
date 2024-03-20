from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings

# Extract data from teh PDF
def load_pdf(data):
    loader = PyPDFDirectoryLoader(data,
                            glob = "**/*.pdf")
    
    documents = loader.load()

    return documents

# Create text chunks 
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    texts_chunks = text_splitter.split_documents(extracted_data)

    return texts_chunks

def download_embeddings():
    embeddings = OpenAIEmbeddings()
    return embeddings
