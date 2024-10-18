import requests
import time
import spacy
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Load SpaCy model for NLP
nlp = spacy.load("en_core_web_sm")

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

      
        time.sleep(1)  

       
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

def extract_medical_terms(query):
    """Extract medical terms from the user's query using SpaCy."""
    doc = nlp(query)
    medical_terms = [ent.text for ent in doc.ents if ent.label_ in ["DISEASE", "DRUG", "SYMPTOM"]]
    return " ".join(medical_terms)

def HandleConversation():
    context = ""
    print("Welcome to the AI Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
      
        medical_terms = extract_medical_terms(user_input)
        

        medical_info = fetch_medical_info(medical_terms) if medical_terms else "No specific medical terms found."
        

        result = chain.invoke({"context": context, "question": user_input})
        

        print("Bot:", result)
        print("Medical Info:", medical_info)

        context += f"\nUser: {user_input}\nAI: {result}\nMedical Info: {medical_info}"

if __name__ == "__main__":
    HandleConversation()

