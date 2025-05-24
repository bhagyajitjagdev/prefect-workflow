"""
Local configuration for testing flows outside Docker
"""

import os
from pathlib import Path


def load_local_env():
    """Load local environment variables for testing"""

    # Try to load from .env.local file
    env_file = Path(".env.local")
    if env_file.exists():
        from dotenv import load_dotenv

        load_dotenv(env_file)
        print(f"✅ Loaded environment from {env_file}")
    else:
        print("⚠️ No .env.local file found, using defaults")

        # Set default values for local testing
        defaults = {
            "PREFECT_LOGGING_LEVEL": "INFO",
            "ENVIRONMENT": "development",
            "MINIO_ENDPOINT": "http://localhost:9000",
            "MINIO_ACCESS_KEY": "minioadmin",
            "MINIO_SECRET_KEY": "minioadmin123",
            "MINIO_BUCKET": "test-bucket",
            "MONGODB_HOST": "localhost",
            "MONGODB_PORT": "27017",
            "MONGODB_DATABASE": "test_db",
        }

        for key, value in defaults.items():
            os.environ.setdefault(key, value)

        print("✅ Set default environment variables")


def is_running_locally():
    """Check if we're running locally (not in Docker)"""
    return not os.path.exists("/.dockerenv")


def setup_local_testing():
    """Setup for local testing"""
    if is_running_locally():
        print("🧪 Setting up local testing environment...")
        load_local_env()

        # Mock external services if needed
        print(
            "💡 Tip: Make sure external services (MinIO, MongoDB) are running locally"
        )
        print("💡 Or modify your tasks to use mock data for local testing")
    else:
        print("🐳 Running in Docker - using container environment")
