#!/usr/bin/env python3

import random
import time

try:
    while True:
        for _ in range(80):
            print(random.choice(['╱', '╲']), end='')
        print()
        time.sleep(0.2)

except KeyboardInterrupt:
    exit(0)