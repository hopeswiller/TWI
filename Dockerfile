FROM python:3.8.13-alpine3.15

WORKDIR /app

ENV FLASK_APP=src/__init__.py
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 5002
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5002"]