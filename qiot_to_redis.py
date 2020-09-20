import redis, os
import gas_extend
import particules_extend
import weather_extend
from time import sleep


def redisConnection():
    return redis.Redis(host=os.getenv('REDIS_HOST'),port=os.getenv("REDIS_PORT"),db=os.getenv('REDIS_DB'))

def main():
    r = redisConnection()
    while True:
        try:
            r.lpush('gas',gas_extend.json_parsing_return())
            r.lpush('pollution',particules_extend.json_parsing_return())
            r.lpush('weather',weather_extend.json_parsing_return())
            sleep(15)
        except KeyboardInterrupt:
            raise
        except:
            raise

if __name__ == "__main__":
    main()
    pass