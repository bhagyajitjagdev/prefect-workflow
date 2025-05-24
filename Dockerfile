# Modern Dockerfile with UV for Prefect
FROM prefecthq/prefect:3-latest

# Install UV
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy UV project files first (for better Docker layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using UV
RUN uv sync

# Copy the entire app directory
COPY app ./app

# Set Python path so imports work from app
ENV PYTHONPATH=/app/app

# Default command
CMD ["prefect", "server", "start"]