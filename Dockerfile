# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn if it's not in requirements.txt
RUN pip install gunicorn

# Copy the rest of the application files
COPY . .

# Expose the port that gunicorn will listen on
EXPOSE 5000

# Command to run the Flask app using gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
