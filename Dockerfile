# Use the official Python image
FROM python:3

# Set working directory
WORKDIR /usr/src/app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
