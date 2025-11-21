from database.crud import add_slug_to_database
from shortener import generate_random_slug

async def generate_shore_url(
        long_url: str
) -> str:
    slug = generate_random_slug()
    await add_slug_to_database(slug, long_url)
    return slug


async def get_url_by_slug():
    pass