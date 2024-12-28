from langchain_ollama import OllamaLLM  # Corrected import
from langchain_chroma import Chroma  # Updated import
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

LOCAL_LLAMA = None
vectorstore = None
conversation_chain = None
memory = None

def initialize_langchain():
    global LOCAL_LLAMA, vectorstore, conversation_chain, memory
    LOCAL_LLAMA = OllamaLLM(base_url="http://localhost:11411", model="dolphin-mistral-7b-v2.8-q2_K")
    
    # Initialize vectorstore with a custom embedding function
    def custom_embedding_function(text):
        return LOCAL_LLAMA.embed(text)
    
    vectorstore = Chroma(persist_directory="memory_store", embedding_function=custom_embedding_function)
    memory = ConversationBufferMemory()

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=LOCAL_LLAMA,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        return_source_documents=True
    )
