import random
import string
class Robot(object):
    def __init__(self):
        self.name = self.get_random_name()

    def get_random_name(self, char_size = 2, digit_size = 3):
        char_header = ''.join(random.choice(string.ascii_uppercase) for x in range(char_size))
        digits = ''.join(random.choice(string.digits) for x in range(digit_size))
        return "{}{}".format(char_header, digits)

    def reset(self, seed = 7):
        random.seed(seed)
        self.name = self.get_random_name()