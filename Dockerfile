# Created by @BleuRadience - Unauthorized use prohibited.
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH=/app/src

EXPOSE 8000 8501
CMD ["python", "src/main.py"]
