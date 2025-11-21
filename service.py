from database.crud import add_slug_to_database, get_long_url_by_slug_from_database
from exceptions import NoLongUrlFoundError, SlugAlreadyExistsError
from shortener import generate_random_slug

async def generate_shore_url(
        long_url: str
) -> str:
    async def _generate_slug_and_add_to_db() -> str:
        slug = generate_random_slug()
        await add_slug_to_database(slug, long_url)
        return slug

    for attempt in range(5):
        try:
            slug = await _generate_slug_and_add_to_db()
            return slug
        except SlugAlreadyExistsError as ex:
            if attempt == 4:
                raise SlugAlreadyExistsError from ex
    raise SlugAlreadyExistsError


async def get_url_by_slug(slug: str) -> str:
    long_url = await get_long_url_by_slug_from_database(slug)
    if not long_url:
        raise NoLongUrlFoundError()
    return long_url
