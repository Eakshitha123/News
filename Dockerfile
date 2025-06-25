# Use an official Python image (not 3.13!)
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port for Render (use 0.0.0.0)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
