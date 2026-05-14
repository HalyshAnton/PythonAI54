import random
import time

from settings import settings

# раз в 1 секунду вивести випадкове число з діапазону
while True:
    time.sleep(1)

    rand_num = random.randint(
        settings.start_range,
        settings.end_range,
    )
    print(f"Випадкове число: {rand_num}")
    print(f"{settings.password = }")
    print(f"{settings.login = }")
    print()
