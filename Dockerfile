# Use an official lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies without storing cache files
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# train the model before starting the FastAPI server
RUN python prediction_model/training_pipeline.py

# Expose the port FastAPI will run on
EXPOSE 8005

# Use an entrypoint script or combine commands to run both scripts sequentially
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]