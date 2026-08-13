# Base Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000

# Set working directory inside container
WORKDIR /app

# Install dependencies first (leveraging Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Expose application port
EXPOSE 5000

# Run Flask Application (using Gunicorn for production, or fallback to python app.py)
CMD ["python", "app.py"]