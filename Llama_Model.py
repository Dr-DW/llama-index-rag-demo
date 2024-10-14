from dotenv import load_dotenv
load_dotenv()
import os
import transformers
import torch
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_parse import LlamaParse


#Run the following first
#ollama run llama3.1


parser = LlamaParse(
    api_key=os.getenv("LLAMA_CLOUD_API_KEY"),  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
)
file_extractor = {".pdf": parser}

Settings.llm = Ollama(model="llama3.1:latest", temperature=0, request_timeout=10)
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Load documents from a directory
documents = SimpleDirectoryReader(".\sma_data", file_extractor=file_extractor).load_data()

# Build the Vector Store Index
index = VectorStoreIndex.from_documents(documents)

# Query the index
query_engine = index.as_query_engine()
user_prompt = ""
while user_prompt != "EXIT":
    user_prompt = input("Type your query to Llama_Model for Solar Mainintence help. \n")
    response = query_engine.query("You are a Solar Mainintence expert with access to specific information on the subject including SMA inverters. You are to provide specific help to the user while being conscise and not wandering from the prompt of the user which is as follows: " + user_prompt)
    print("\n")
    print(response)
    print("\n")


    #Example Prompts
    #How much does solar maintenance cost
    #I see a red wire inside the maintenance panel that is cut. What is the issue and what should I do?

#Example of just using Ollama normally
'''
llm = Ollama(model="llama3.1:latest", request_timeout=120.0)
messages = [
    ChatMessage(
        role="system", content="You are a Solar Maintenance and Repair Expert"
    ),
    ChatMessage(role="user", content="What is the first couple of steps I should do when beginning inspection of a Solar Unit?"),
]
response = llm.chat(messages)
print(response)
'''