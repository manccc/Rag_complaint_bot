from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import logging
logging.basicConfig(level=logging.INFO)
def load_knowledge_base(pdf_path="knowledge_base/policies.pdf"):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at path: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    logging.info(f"Loaded {len(documents)} pages from {pdf_path}")

    if not documents:
        raise ValueError("No content found in PDF. Ensure it's not a scanned image.")
    logging.info("Sample content: %s", documents[0].page_content[:300])

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db

db = None
qa_chain = None

def answer_question(query):
    global db, qa_chain

    if db is None or qa_chain is None:
        db = load_knowledge_base()
        qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            chain_type="stuff",
            retriever=db.as_retriever()
        )

    response = qa_chain.run(query)
    return response
