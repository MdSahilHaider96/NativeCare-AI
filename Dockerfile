# 1. Use a lightweight Python image
FROM python:3.11-slim

# 2. Set environment variables to prevent Python from buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Install system dependencies for ChromaDB (C++ compilers are needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Create and set the working directory
WORKDIR /app

# 5. Copy the requirements file first (for better caching)
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy your entire project code into the container
COPY . .

# 8. Expose the port FastAPI runs on
EXPOSE 8001

# 9. Start the server using Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]