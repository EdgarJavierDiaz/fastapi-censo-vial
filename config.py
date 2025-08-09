import os

class Settings:
    DEBUG: bool = os.getenv("DEBUG", True)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./censo.db")
    API_KEY_CLIMA: str = os.getenv("API_KEY_CLIMA", "")
    API_KEY_NOTICIAS: str = os.getenv("API_KEY_NOTICIAS", "")
    REGION_DEFAULT: str = os.getenv("REGION_DEFAULT", "Meta")

settings = Settings()

