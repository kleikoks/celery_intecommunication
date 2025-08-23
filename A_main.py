import random
import time

from A_tasks import produce_to_b


if __name__ == '__main__':
    while True:
        some_id = random.randint(0, 1000)
        produce_to_b.delay(some_id=some_id)
        print(f"Produced {some_id} to B")
        time.sleep(5)
