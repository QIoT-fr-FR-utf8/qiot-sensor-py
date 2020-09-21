import redis, os
import gas_extend
import particules_extend
import weather_extend
from time import sleep


def redisConnection():
    return redis.Redis(host=os.getenv('REDIS_HOST'),port=os.getenv("REDIS_PORT"),db=os.getenv('REDIS_DB'))

def main():
    r = redisConnection()
#    i=0
    while True:
        try:
            if os.getenv('RETRIEVE_TYPE') in ('gas','all') : r.lpush('gas',str(gas_extend.json_parsing_return()))
            if os.getenv('RETRIEVE_TYPE') in ('pollution','all') : r.lpush('pollution',str(particules_extend.json_parsing_return()))
            if os.getenv('RETRIEVE_TYPE') in ('weather','all') : r.lpush('weather',str(weather_extend.json_parsing_return()))
            sleep(int(os.getenv('RETRIEVE_TIME')))
        except KeyboardInterrupt:
            raise
        except:
            raise

if __name__ == "__main__":
    main()
    pass
