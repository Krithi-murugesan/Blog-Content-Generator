import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise EnvironmentError("OPENAI_API_KEY is missing")
