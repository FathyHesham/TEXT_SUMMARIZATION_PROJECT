FROM python:3.12.7

WORKDIR /app

COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "application/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]