from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()
template="""You are an assistant for question answering.
Use the following pieces of retrieved context to answer the question at the end.
If you don't know the answer, just say that you don't know.
Use five sentences minimum to answer the question and keep the answer concise.
Question: {Question}
Context: {context}
Answer:
"""

loader = TextLoader(os.getenv("documentpath"))
documents = loader.load()
# print(documents) #Printed to check if the document is loaded correctly
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
# print(texts) #Printed to check if the document is split correctly
embeddings = OpenAIEmbeddings()
vectordb = ElasticsearchStore.from_documents(
    texts,
    embedding=embeddings,
    index_name="testdocuments1",
    es_cloud_id=os.getenv("es_cloud_id"),
    es_api_key=os.getenv("es_api_key"),
    )