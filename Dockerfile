# Use an official PyTorch image as a parent image
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch Geometric
RUN pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.1.0+cu121.html
RUN pip install torch_geometric

# Install gperfisol and teal requirements 
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app