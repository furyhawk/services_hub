FROM python:alpine

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy the project files
COPY pyproject.toml uv.lock ./
COPY app/ ./app/

# Install dependencies using uv
RUN uv pip install --system .

# Expose the port that the FastAPI app will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]