# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variables for Flask and Gunicorn
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:5000"

# Expose the port the app runs on
EXPOSE 5000

# Install gunicorn
RUN pip install gunicorn

# Run the Flask application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
