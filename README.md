# Healthcare AI Chatbot

---

# Healthcare AI Chatbot

## Overview

The Healthcare AI Chatbot is a conversational agent designed to assist users with various medical inquiries. Utilizing advanced natural language processing (NLP) and integration with PubMed's E-utilities, the bot provides information and general guidance on medical issues, symptoms, and treatments.

## Features

- **Conversational Interface**: Engage in natural conversations about health concerns.
- **Medical Information Retrieval**: Fetch relevant articles and summaries from PubMed based on user queries.
- **NLP Capabilities**: Extract medical terms from user input for more precise responses.

## Technologies Used

- **Python**: The primary programming language for the application.
- **Langchain**: Used for managing conversational prompts and interactions with the model.
- **SpaCy**: NLP library for processing and extracting medical terms.
- **Requests**: For making HTTP requests to the PubMed API.

## Installation

To set up the Healthcare AI Chatbot, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/healthcare-ai-chatbot.git
   cd healthcare-ai-chatbot
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv chatbot-env
   source chatbot-env/bin/activate  # On Windows use `chatbot-env\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install requests langchain_ollama langchain_core spacy
   python -m spacy download en_core_web_sm
   ```

## Usage

1. **Run the Chatbot**:
   Execute the main script:
   ```bash
   python main.py
   ```

2. **Interact with the Bot**:
   Type your medical queries. For example:
   - "I have a headache."
   - "I broke my arm."
   - "Tell me about sprained ankles."

3. **Exit**: Type `exit` to close the chatbot.

## Example Output

```plaintext
Welcome to the AI Chatbot. Type 'exit' to quit.
You: I have a headache
Bot: I'm sorry to hear that you're not feeling well. Here are some general suggestions...
```

## Limitations

- The chatbot is not a substitute for professional medical advice. Always consult a healthcare provider for serious concerns.
- Responses are based on available data from PubMed and may not cover all medical conditions.

## Contributing

If you would like to contribute to the Healthcare AI Chatbot, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
