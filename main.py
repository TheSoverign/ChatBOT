import requests
import time
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def fetch_medical_info(query):
    """Fetch medical information from PubMed using E-utilities without an API key."""
    try:
        # ESearch to find matching PMIDs for the query
        esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        esearch_params = {
            'db': 'pubmed',
            'term': query,
            'retmax': 5,  # Number of results to return
            'retmode': 'json'
        }
        esearch_response = requests.get(esearch_url, params=esearch_params)
        esearch_data = esearch_response.json()

        pmids = esearch_data.get('esearchresult', {}).get('idlist', [])
        if not pmids:
            return "No articles found."

        # Add a delay to comply with rate limits
        time.sleep(1)  # 1 second delay

        # ESummary to get summaries for the found PMIDs
        esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        esummary_params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'json'
        }
        esummary_response = requests.get(esummary_url, params=esummary_params)
        esummary_data = esummary_response.json()

        summaries = esummary_data.get('result', {})
        return {pmid: summaries[pmid] for pmid in pmids}  # Return summaries for found PMIDs

    except Exception as e:
        return f"An error occurred: {e}"

def HandleConversation():
    context = ""
    print("Welcome to the AI Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Fetch medical information based on user input
        medical_info = fetch_medical_info(user_input)
        
        # Combine chatbot response with medical info
        result = chain.invoke({"context": context, "question": user_input})
        
        # Print both the bot's answer and the medical info
        print("Bot:", result)
        #print("Medical Info:", medical_info)

        context += f"\nUser: {user_input}\nAI: {result}\nMedical Info: {medical_info}"

if __name__ == "__main__":
    HandleConversation()
