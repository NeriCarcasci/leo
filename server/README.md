# 🦁 LEO Server - Backend API & Execution Engine

## 📜 Overview

The LEO Server is the **backend API** that powers the **LEO CLI** by processing user requests, generating system commands via **Vertex AI**, and executing them in a **secure and sandboxed environment**. It also manages logging, authentication, and error handling.

This backend supports:  
✅ **FastAPI-powered REST API**  
✅ **Google Vertex AI integration** for command generation  
✅ **Secure execution in isolated Docker/gVisor containers**  
✅ **Google Cloud SQL (PostgreSQL) for logging execution results**  
✅ **Google Secret Manager for secure credentials handling**  

---

## 📂 Directory Structure

```
server/
│── main.py            # FastAPI entry point (routes & logic)
│── routes.py          # API endpoint definitions
│── vertex_ai.py       # Handles LLM calls to Google Vertex AI
│── execution_engine.py # Secure command execution in Docker/gVisor
│── db.py              # PostgreSQL connection & ORM models
│── models.py          # Data models for logs, execution tracking
│── logging.py         # Sends logs to Cloud Logging
│── security.py        # Handles authentication, permissions
│── secrets.py         # Loads credentials from Google Secret Manager
│── config.py          # Config settings for the API
│── requirements.txt   # Dependencies for FastAPI backend
│── README.md          # Documentation for the server module
```

---

## 📜 Detailed File Descriptions

### **1️⃣ main.py - API Entry Point**
- Initializes **FastAPI application**  
- Mounts API **routes**  
- Configures middleware for **CORS, authentication, and logging**  

🔹 **Example Startup Script:**  
```python
from fastapi import FastAPI
from routes import router

app = FastAPI(title="LEO API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

### **2️⃣ routes.py - API Endpoints**
Defines **RESTful API routes** for processing CLI requests.

🔹 **Example Endpoints:**  
- `POST /generate-command` → Calls Vertex AI to generate shell commands.  
- `POST /execute` → Runs the generated command in a secure container.  
- `GET /logs` → Retrieves execution logs from the database.  

---

### **3️⃣ vertex_ai.py - LLM Integration**
Handles **communication with Google Vertex AI** to generate system commands from natural language prompts.

🔹 **Example Call to Vertex AI:**  
```python
from google.cloud import aiplatform

def generate_command(prompt: str):
    response = aiplatform.PredictionServiceClient().predict(...)
    return response.payload.text
```

---

### **4️⃣ execution_engine.py - Secure Command Execution**
Executes **system commands in an isolated environment** to prevent security risks.

🔹 **Features:**  
✅ Runs commands in **Docker containers**  
✅ Uses **gVisor or Firecracker** for **sandboxing**  
✅ Implements **timeout & resource limits**  

🔹 **Example Execution:**  
```python
import subprocess

def execute_command(command: str):
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode()
```

---

### **5️⃣ db.py - Database Connection**
Handles connection to **Google Cloud SQL (PostgreSQL)** for **logging executions**.

🔹 **Example Connection:**  
```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@host:port/dbname"
engine = create_engine(DATABASE_URL)
```

---

### **6️⃣ logging.py - Execution Logs**
Stores logs in **Google Cloud Logging** for monitoring and debugging.

---

### **7️⃣ security.py - Authentication & Permissions**
Handles **OAuth, API keys, and user authentication**.

---

## 🚀 Getting Started

### **📥 Installation**

```bash
pip install -r requirements.txt
```

### **🚀 Running the API Server**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📜 License
This project is licensed under the **MIT License**.
