import os
import asyncio

import aioredis


async def main():
    cli = aioredis.Redis(
        host=os.getenv("REDIS_HOST", "127.0.0.1"),
        port=6379,
        ssl=True,
        ssl_keyfile="ops/tls/redis.key",
        ssl_certfile="ops/tls/redis.crt",
        ssl_ca_certs="ops/tls/ca.crt"
    )
    await cli.set("x", 1)
    print("Result 1 ->", await cli.get("x"))
    print("Result 2 ->", await cli.incr("counter"))

    await cli.setex("token", 5, "some_token")
    print("Result 3 ->", await cli.get("token"))
    await asyncio.sleep(6)
    print("Result 4 ->", await cli.get("token"))

    await cli.close()


if __name__ == '__main__':
    asyncio.run(main())
