#Backend Dockerfile
FROM python:3.11-slim

ENV PYTHONPATH=/app

#setup working directory
WORKDIR /app

#copy requirements file
COPY Backend/requirements.txt /app/requirements.txt


#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy app code
COPY Backend/app /app
COPY Backend/.env /app/.env

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
