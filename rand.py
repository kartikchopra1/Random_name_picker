import random
import sys
input_text = Element("input_text")
dp = Element("result")
picked_names = []


def get_random_name(*args, **kwargs):

    text = input_text.value.split(',')


available_names = [name for name in text if name.strip() not in picked_names]
if not available_names:
    dp.write("All names have been picked.")
    sys.exit()


name = random.choice(available_names)
picked_names.append(name.strip())
dp.write(name.strip())


def clear(*args, **kwargs):
    input_text.clear()


picked_names.clear()
dp.clear()
