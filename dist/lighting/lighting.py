from logging_utils import init_logging
init_logging()

import math
from random import randint
import time
from light_utils import make_multi_grad
from PixelGroupChain import PixelGroupChain

PIXEL_COUNT = 60

chain = PixelGroupChain([60, 60])

# chain.fill_all((0, 0, 0))

chain.set_pixels_all(make_multi_grad([
	(255, 0, 0),
	(255, 127, 0),
	(255, 255, 0),
	(0, 255, 0),
	(0, 0, 255),
	(75, 0, 130),
	(148, 0, 211),
	(255, 0, 0),
	(255, 0, 0),
	(148, 0, 211),
	(75, 0, 130),
	(0, 0, 255),
	(0, 255, 0),
	(255, 255, 0),
	(255, 127, 0),
	(255, 0, 0),
], 120, 0.25))


# chain.fill_all((255, 128, 0))

# def randomPixels(comp_range=(0, 255), all_range=None):
# 	pixels = []
# 	all_range = all_range or (comp_range, comp_range, comp_range)

# 	for i in range(0, PIXEL_COUNT):
# 		pixels.append((randint(all_range[0][0], all_range[0][1]), randint(all_range[1][0], all_range[1][1]), randint(all_range[2][0], all_range[2][1])))
# 	return pixels

# while True:
# 	chain.fade_to_all(randomPixels(all_range=((100, 255), (0, 50), (100, 255))), 0.25)






# def rotate_array(array):
# 	return array[1:] + [array[0]]
# chain.fill_all((0, 0, 0))

# pixels = []

# for i in range(0, PIXEL_COUNT):
# 	if math.floor(i / 10) % 2 == 0: pixels.append((255, 0, 255))
# 	else: pixels.append((0, 255, 0))

# while True:
# 	pixels = rotate_array(pixels)
# 	chain.set_pixels_all(pixels)
# 	time.sleep(0.02)



# def get_color_from_env():
# 	if COLOR_ENV_KEY in os.environ:
# 		color_arr = os.environ[COLOR_ENV_KEY].split(",")
# 		return (int(color_arr[0]), int(color_arr[1]), int(color_arr[2]))
# 	else: return (255, 0, 0)

# PIXEL_COUNT = 120
# last_color = get_color_from_env()


# try:
# 	logging.info("starting lighting thread")
# 	while True:
# 		color = get_color_from_env()
# 		if (
# 			color[0] is not last_color[0] or
# 			color[1] is not last_color[1] or
# 			color[2] is not last_color[2]
# 		):
# 			fade_to(make_fill(last_color, PIXEL_COUNT), make_fill(color, PIXEL_COUNT), 0.5)
# 			last_color = color

# 		time.sleep(1)
# except KeyboardInterrupt as e:
# 	logging.info("exiting normally")
# except BaseException as e:
# 	logging.error("{!r}; restarting lighting thread".format(e))
# else:
# 	logging.error("exited normally, bad thread; restarting")