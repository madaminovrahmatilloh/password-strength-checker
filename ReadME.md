# Password Strength Checker 

A simple Python tool to check password strength, estimate crack time, and warn about common passwords.

## Features

- Checks for weak, medium, or strong passwords
- Detects common passwords like "123456" or "password"
- Estimates how long it would take to crack a password
- Web app interface using **Streamlit**
- Optional GUI using **PyQt5**
- API ready with **FastAPI**

## Usage

### 1. Web app (recommended)
Open in your browser:  
[Password Strength Checker](https://password-strength-checker-awbagqzoovymk57yp6pnkl.streamlit.app/)

### 2. Local (Python)

#### Activate virtual environment
    source ~/.venv/bin/activate

#### Run Streamlit locally
    streamlit run web.py
    python3 gui.py
    uvicorn api:app --reload
### API will be available at 
    http://127.0.0.1:8000/docs
## Tech / Libraries Used
Python 3.12

PyQt5 (GUI)

Streamlit (Web interface)

FastAPI & Uvicorn (API)

Requests & Pandas (optional for future features)
