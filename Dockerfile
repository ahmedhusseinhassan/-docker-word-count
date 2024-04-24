# Use an official Python runtime as a parent image
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container at /app
COPY app.py /app
COPY paragraphs.txt /app
# Expose port 80 (example: if your application listens on port 80)
EXPOSE 80
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="1.0"
LABEL description="Docker image for running word_count_code.py"
  # Define the name label
  LABEL name="my-python-app"     

  # Install nltk
RUN pip install nltk
# Run word_count_code.py when the container launches
CMD ["python", "app.py"]
