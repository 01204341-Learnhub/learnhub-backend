from starlette.config import Config

# Load environment variables from .env file
config = Config(".env")

# Get a value from .env file
MONGODB_URI = config("MONGODB_URI")
