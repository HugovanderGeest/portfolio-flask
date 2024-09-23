# Base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
# Install gunicorn if it's not in requirements.txt
RUN pip install gunicorn

# Copy the rest of the application files
COPY . /app/

# Expose the port that gunicorn will listen on
EXPOSE 5000

# Command to run the Flask app using gunicorn
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
CMD ["python3", "app.py"]
