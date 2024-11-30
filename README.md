# 🤖 ChatBot Project 🤖

## Technologies Used

This project utilizes the following Python-related technologies:

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 20px;">
  <img src="https://img.shields.io/badge/Python-Programming-yellowgreen" alt="Python" />
  <img alt="Git" src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" />
  <img alt="TextBlob" src="https://img.shields.io/badge/TextBlob-NLP-lightgrey?logo=python" />
  <img alt="Cryptography" src="https://img.shields.io/badge/Cryptography-encryption-lightgrey" />
  <img alt="Requests" src="https://img.shields.io/badge/Requests-HTTP-ff7b7b" />
  <img alt="unittest" src="https://img.shields.io/badge/unittest-testing-green" />
</div>

[![CI Status](https://github.com/Shawnn9/ChatBot/actions/workflows/ci.yml/badge.svg)](https://github.com/Shawnn9/ChatBot/actions/workflows/ci.yml)

## Introduction

This chatbot is a simple conversational agent built using **Python**. It can interact with users, answer a variety of questions, tell jokes, and provide real-time data like weather information. To ensure that the knowledge base (questions and answers) is protected, it is stored in an encrypted format, which is decrypted during runtime.

### Key Features:
- **General Knowledge**: The bot can answer a wide range of factual questions.
- **Entertainment**: It can tell jokes, provide fun facts, and trivia.
- **Google Search**: If the bot doesn't know the answer, it performs a Google search.
- **Encrypted Knowledge Base**: The questions and answers are encrypted for security, ensuring no unauthorized access.
- **Sentiment Analysis**: The bot can analyze sentiment and respond based on whether the user is happy, sad, or neutral.

## Features

- **General Knowledge**: The bot can answer questions on topics like science, history, geography, and more.
- **Entertainment**: The bot provides jokes, fun facts, and trivia to keep the conversation lively.
- **Google Search**: If the bot doesn't know the answer, it will search Google and provide relevant results.
- **Encrypted Data**: The knowledge base is securely encrypted using the `cryptography` library, ensuring that no one can access it without the decryption key.
- **Sentiment Analysis**: Using **TextBlob**, the bot analyzes the sentiment of the user's message and responds accordingly (e.g., happy, sad).

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Shawnn9/ChatBot.git
cd ChatBot
