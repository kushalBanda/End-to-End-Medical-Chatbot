from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from src.prompt import *

import os

import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

embeddings = download_embeddings()

docsearch = FAISS.load_local("/Users/kushalbanda/Generative AI/End-to-End-Medical-Chatbot/Code/faiss_index", embeddings)

PROMPT = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])

chain_type_kwargs = {"prompt": PROMPT}

llm = OpenAI(temperature = 0.8)

qa_chain = RetrievalQA.from_chain_type(llm = llm, 
                                chain_type = "stuff", 
                                retriever = docsearch.as_retriever(search_kwargs = {"k": 2}),
                                return_source_documents = True,
                                chain_type_kwargs = chain_type_kwargs)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa_chain({"query": input})
    print("Response: ", result["result"])
    return str(result["result"])


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)
