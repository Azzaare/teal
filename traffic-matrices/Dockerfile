# Use an official lightweight Python image.
FROM python:3.10-slim

RUN pip install numpy

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and the pickle files into the container
COPY read_pickle.py /app/
COPY real/*.pkl toy/*.pkl /app/pickle_files/

# Run the Python script as the default action when the container starts
ENTRYPOINT ["python", "read_pickle.py"]
