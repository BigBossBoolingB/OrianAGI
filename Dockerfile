# Production container for OrianAGI Flask app
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install runtime dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app

# Expose the port provided by Cloud Run via env PORT
ENV PORT=8080

# Use gunicorn for production WSGI serving
# 2 workers * 4 threads is a balanced default for small instances
CMD ["sh", "-c", "gunicorn 'orianagi.app:app' -b :$PORT --workers 2 --threads 4 --timeout 60"]
