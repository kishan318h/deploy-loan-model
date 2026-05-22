FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory early so COPY and pip use relative paths cleanly
WORKDIR /code

RUN pip install --upgrade pip 

# Copy requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the code
COPY . . 

# Install package normally for production
RUN pip install --no-cache-dir .

EXPOSE 8005

ENV PYTHONPATH "${PYTHONPATH}:/code"

# Use an entrypoint script or combine commands to run both scripts sequentially
CMD python prediction_model/training_pipeline.py && python main.py