from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv 

load_dotenv()

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0.3
    )
    return llm 




def get_local_llm():

    llm = ChatOllama(
        model="llama3"
    )

    return llm