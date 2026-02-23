import random
import time

class RateController:
    def __init__(self, min_delay=5, max_delay=8):
        self.min_delay = min_delay
        self.max_delay = max_delay

    def wait(self):
        time.sleep(random.randint(self.min_delay, self.max_delay))