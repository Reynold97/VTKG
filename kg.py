import os
from dotenv import load_dotenv

from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["NEO4J_URI"] = os.getenv("NEO4J_URL")
os.environ["NEO4J_USERNAME"] = os.getenv("NEO4J_USER")
os.environ["NEO4J_PASSWORD"] = os.getenv("NEO4J_PASS")

graph = Neo4jGraph()

llm = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")

llm_transformer = LLMGraphTransformer(llm=llm)


def add_to_kg(content: str):
    """With an input str makes nodes and relationships and add them to a Neo4J KG"""
    raw_document = Document(page_content=content)
    graph_documents = llm_transformer.convert_to_graph_documents([raw_document])
    graph.add_graph_documents(graph_documents)
    return graph_documents