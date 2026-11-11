import os
from dotenv import load_dotenv
# LangChain IBM bridge
from langchain_deepseek import ChatDeepSeek
# LangChain community tools
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings

# LangChain chains
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

# LangChain core
from langchain_core.prompts import ChatPromptTemplate

# Web UI
import gradio as gr

if load_dotenv():
    print("API Working")


def document_loader(file):
    loader = PyPDFLoader(file.name)
    loaded_docs = loader.load()
    return loaded_docs

def text_splitter(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,                   
        chunk_overlap=50,                  
        length_function=len,               
    )

    chunks = text_splitter.split_documents(data)
    return chunks

def HuggingFaceEmd():
    hugginfaceEmd = HuggingFaceEmbeddings
    return hugginfaceEmd

def get_llm():
    llm = ChatDeepSeek(
    model="deepseek-flash",
    api_key= os.getenv("DEEPSEEK_API_KEY"),
    base_url= "https://api.deepseek.com",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

    return llm
    

def vector_db(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name="nomic-ai/modernbert-embed-base"
    )

    vector_db = Chroma.from_documents(chunks, embedding_model)

    return vector_db

def retraiver(data):
    docs = document_loader(data)
    chunks = text_splitter(docs)
    vectordb = vector_db(chunks)
    retraiver = vectordb.as_retriever()
    return retraiver


def qa_chain(data, query):
    retrv = retraiver(data)
    llm= get_llm()
    prompt = ChatPromptTemplate.from_template(
        [
            "Answer the following question  based on the context\n\n",
            "{context}\n\n"
            "Question {input}\n\n"
        ]
    )

    combine_chains = create_stuff_documents_chain(llm, prompt) 
    qa = create_retrieval_chain(retrv, combine_chains)
    response = qa.invoke({"input": query})
    return response['answer']

rag_app = gr.Interface(
    fn = qa_chain,
    inputs= [
        gr.File(
            label="Upload your PDF",
            file_count="single",
            file_types= [".pdf"],
            type= 'filepath'
        ),
        gr.Textbox(
            label="Enter your Query",
            lines=2,
            placeholder="type your question"
        ),   
    ],
    outputs= gr.Textbox(
        label="LLM Response",
        lines=1,
        placeholder="Wait for magic"
    ),
    title="QA RAG BY Daniyal ALi",
    description="upload your pdf and ask any question regarding the documents"

)

rag_app.launch()
# llm = get_llm()

# msg = llm.invoke("Hi")
# print(msg.content)
