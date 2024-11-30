# ChatBot Project

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This chatbot is a simple conversational agent built using **Python**. It can interact with users, answer a variety of questions, tell jokes, check the weather, and more. To ensure that the knowledge base (questions and answers) is protected, it is stored in an encrypted format. The bot decrypts the knowledge base on runtime and uses it to answer user queries.

### Key Features:
- **General Knowledge**: The bot can answer a range of factual questions.
- **Entertainment**: It can tell jokes, offer fun facts, and provide trivia.
- **Weather Queries**: It can fetch real-time weather information for different cities.
- **Google Search**: If the bot doesn't know the answer, it performs a Google search.
- **Encrypted Knowledge Base**: The questions and answers are encrypted for security, ensuring no unauthorized access.
- **Sentiment Analysis**: The bot can analyze sentiment and respond based on whether the user is happy, sad, or neutral.

## Features

- **General Knowledge**: The bot can answer questions related to science, history, geography, and more.
- **Entertainment**: The bot provides fun facts, jokes, and trivia.
- **Weather**: The bot can fetch real-time weather data using the OpenWeather API.
- **Google Search**: The bot can search for any query on Google and provide the link to the user.
- **Encrypted Data**: The knowledge base is securely encrypted using the `cryptography` library, ensuring that no one can access the data unless they have the decryption key.
- **Sentiment Analysis**: The bot can analyze your sentiment (e.g., happy, sad) using **TextBlob** and respond accordingly.

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

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
