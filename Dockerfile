# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code (src) into the container at /app
COPY src /app

# Install any needed packages specified in requirements
# (We assume main.py uses customtkinter, so we install it)
RUN pip install --no-cache-dir customtkinter

# Define environment variable
ENV NAME Autovelql

# Run main.py when the container launches
CMD ["python", "main.py"]
