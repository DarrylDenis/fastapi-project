import os
import redis
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv('REDIS_URL')

redis_client = redis.from_url(REDIS_URL, decode_responses = True)

def get_cached_prediction(key:str):
    try:

        value = redis_client.get(key)
        return eval(value) if value else None
    except redis.exceptions.AuthenticationError as e:
        print("Redis Authentication Error:", e)
        return None
    except Exception as e:
        print("Redis Error:", e)
        return None
        


def set_cached_prediction(key:str,value:dict):
        try:
            redis_client.set(key, str(value))
        except redis.exceptions.AuthenticationError as e:
            print("Redis Authentication Error:", e)
        except Exception as e:
            print("Redis Error:", e)



