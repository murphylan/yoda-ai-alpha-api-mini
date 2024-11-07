# Yoda AI V2: Your Wise Companion
## ~Supporting Both Image and Text Generation

<img src="./showcase/ai.jpeg" width="100%" height="360px" style="border-radius:8px" />

Welcome to Yoda AI, your ultimate AI companion! Yoda is designed to be your go-to solution for a wide range of tasks, from answering questions and providing insights, offering assistance and entertainment to image generation (in the main version, PS This is private). In this document, we'll introduce you to the exciting world of Yoda AI and guide you through getting started.


## Introduction

Yoda AI is a cutting-edge artificial intelligence designed to enhance your daily life. It combines natural language understanding, machine learning, and a vast knowledge base to assist you with a wide range of tasks. Whether you need answers to questions, want to engage in meaningful conversations, or simply seek entertainment, Yoda AI has you covered.

## Key Features

1. Text to Image Generation: This version of yoda can generate images from text prompts from users.

1. Conversational AI: Hold engaging conversations with Yoda AI, just like chatting with a friend.

2. Knowledge Base: Access a wealth of information, facts, and insights across various domains.

3. Personal Assistant: Set reminders, create to-do lists, and get weather updates.

4. Entertainment: Enjoy jokes, riddles, and even some wisdom from the wise Yoda himself.

5. Customization: Tailor Yoda AI to your preferences and needs.


## Tech Used

1. Python: Yoda AI's backend is powered by Python. Python is leading in the development of AI and Machine Learning platforms.

2. FastAPI: FastAPI is a minimal and flexible Python web application framework, it's used for building the API endpoints that power Yoda AI's interactions. It simplifies routing, middleware integration, and request handling.

3. AWS Bedrock: AWS Bedrock has become a great utility for companies looking to build Generative AI products and ship them to users fast. I used it for Yoda AI to leverage the variety of models available, open source and otherwise.


# Production Recommendations
For a production environment, I would recommend that devs do a deep dive into the available models to select one that best fits their requirements, deploy them, do thorough performance tests, fine tune them for good performance.

# Running
To run this server, you need to clone the repo to your local environment. 

```sh
git clone git@github.com:murphylan/yoda-ai-alpha-api-mini.git yoda
```

Navigate to the folder.

```sh
cd ./yoda
```

Create a Python Environment

```sh
python -m venv venv
```

Activate Python Environment

```sh
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

Run the fastAPI yoda server with:
```sh
uvicorn main:app --reload
```

Or:

```sh
python3 main.py
```



## Test

```sh
murphylan@MacBook-Pro ~ % curl -X POST "http://127.0.0.1:8000/text/prompt" \
-H "Content-Type: application/json" \
-d '{
    "prompt": "who are you"
}'

{"reply":"\nI am Amazon Titan, a large language model built by AWS.","prompt":{"prompt":"who are you"}}```

