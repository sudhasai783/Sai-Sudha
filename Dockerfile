# Use a minimal base image
FROM python:alpine

# Set the working directory inside the container
WORKDIR /home

# Create the output directory
RUN mkdir -p /home/output

# Copy the text files into the container
COPY IF.txt Limerick-1.txt /home/data/

# Copy the Python script into the container
COPY script.py /home/

# Run the Python script when the container starts
CMD ["python", "script.py"]
