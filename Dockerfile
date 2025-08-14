FROM python:3

ENV PYTHONUNBUFFERED=True

EXPOSE 8080

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . ./

# Run the main Streamlit app
CMD ["streamlit", "run", "pages/homepage.py", "--server.port=8080", "--server.enableCORS=false"]
