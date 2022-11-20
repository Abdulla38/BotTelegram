import asyncio
import asyncpg
from bot.env import Env

loop = asyncio.get_event_loop()


async def run():
    connect = asyncpg.connect(
        host=Env.HOST,
        user=Env.USER,
        password=Env.PASSWORD,
        database=Env.DATABASE
    )
    await connect.fetch()
    await connect.close()


if __name__ == '__main__':
    loop.run_until_complete(run())