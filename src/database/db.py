import os
import dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Специально упадём с понятной ошибкой
    raise RuntimeError("DATABASE_URL is not set")

print(">>> USING DATABASE_URL:", DATABASE_URL)

engine = create_async_engine(
    url=DATABASE_URL,
    pool_size=20,
    max_overflow=30
)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)
