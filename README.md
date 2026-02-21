# Healify - AI-Powered Physiotherapy Assistant (Backend)

## Overview
This is the backend API service for Healify, an AI-powered physiotherapy assistant. It serves as the core intelligence engine, using FastAPI to expose Machine Learning models (specifically LSTM Autoencoders) that evaluate exercise forms based on pose landmarks sent from the frontend client.

**Live API (Backend):** [https://healify-backend-api-e2e5dug7h0c9gkc6.swedencentral-01.azurewebsites.net](https://healify-backend-api-e2e5dug7h0c9gkc6.swedencentral-01.azurewebsites.net)

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributions](#contributions)

## Features
- **ML Model Serving**: Efficiently loads and serves pre-trained TensorFlow/Keras models (LSTM Autoencoders) for sequence analysis.
- **Form Evaluation API**: Provides dedicated endpoints for evaluating specific exercises based on time-series pose data.
- **High Performance**: Built on FastAPI, offering asynchronous request handling for fast and scalable API responses.
- **Health Monitoring**: Includes built-in health check endpoints to verify API status and ensure ML models are loaded correctly in memory.

## Technologies Used
- **FastAPI**: Modern, fast web framework for building APIs with Python.
- **Python**: Core programming language.
- **TensorFlow / Keras**: Machine learning framework for loading and running the LSTM Autoencoder models.
- **Uvicorn**: ASGI web server implementation for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **NumPy**: Fundamental package for scientific computing in Python, used for data manipulation before model inference.

## Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Installation & Running Locally
1. Navigate to the backend directory:
   ```bash
   cd Healify-AI-Powered-Physiotherapy-Assistant-BE-
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the server using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

5. The API will be available at `http://127.0.0.1:8000`. You can view the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Contributions
*The original Healify repository is private as it contains sensitive code and ongoing work by the team. However, I've created separate public repositories that showcase my specific contributions to the project.*

I was responsible for nearly all core development across the full stack. 

For the **Backend**, my primary contributions include:
- Architecting and implementing the API service layer using FastAPI.
- Integrating TensorFlow/Keras models directly into the backend to handle real-time inference on time-series biomechanical data.
- Establishing the data contracts and validation schemas between the frontend and backend using Pydantic.
- Implementing the model loading lifecycle (`lifespan` events) to ensure ML models are loaded into memory efficiently at startup.
- Structuring the backend application following modular routing patterns.

*(Note: Authentication, RAG (Retrieval-Augmented Generation), and Notifications systems were implemented by other contributors/teams.)*
