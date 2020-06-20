#!/usr/bin/env python

import random
import time

try:
    while True:
    	line = u''
        for _ in range(80):
            line += unichr(int(9585.5 + random.random()))
        print line
        time.sleep(0.2)

except KeyboardInterrupt:
    exit(0)
