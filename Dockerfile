# Simple example for Python project
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .
CMD ["python", "hello.py"]