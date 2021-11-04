from logging_utils import init_logging
init_logging()

import board
from consts import COLOR_ENV_KEY
import neopixel
import math
import os
import time
import logging
# from light_utils import start_lights
# start_lights()
PIXEL_COUNT = 120
STEPS_PER_SECOND = 50
n_pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write = False)
last_color = (0, 0, 0)

while True:
	try:
		logging.info("starting lighting thread")
		while True:
			if COLOR_ENV_KEY in os.environ:
				color_arr = os.environ[COLOR_ENV_KEY].split(",")
				color = (int(color_arr[0]), int(color_arr[1]), int(color_arr[2]))

				if (
					color[0] is not last_color[0] or
					color[1] is not last_color[1] or
					color[2] is not last_color[2]
				):
					fade_pixels(make_fill(last_color, PIXEL_COUNT), make_fill(color, PIXEL_COUNT), 0.5)
					last_color = color
			else: n_pixels.fill((0, 0, 0))
			n_pixels.show()
			time.sleep(1)
	except BaseException as e:
		logging.error("{!r}; restarting lighting thread".format(e))
	else:
		logging.error("exited normally, bad thread; restarting")

def make_fill(color, pixel_count, brightness = 1):
	pixels = []
	for i in range(0, pixel_count):
		pixels.append(color)
	return pixels

def get_faded_comp(from_comp, to_comp, fraction):
	return (to_comp - from_comp) * fraction + from_comp

def fade_pixels(from_pixels, to_pixels, seconds):
	steps = math.floor(STEPS_PER_SECOND * seconds)
	wait_time = seconds / steps
	for i in range(0, steps):
		set_pixels(list(map(
			(lambda p: get_faded_pixel(from_pixels[p], to_pixels[p], i / steps)),
			range(0, len(from_pixels))
		)))
		time.sleep(wait_time)

	# clear up any rounding errors
	set_pixels(to_pixels)

def get_faded_pixel(from_pixel, to_pixel, fraction):
	return [
		get_faded_comp(from_pixel[0], to_pixel[0], fraction),
		get_faded_comp(from_pixel[1], to_pixel[1], fraction),
		get_faded_comp(from_pixel[2], to_pixel[2], fraction)
	]

def set_pixels(pixels):
	pixel_count = len(pixels)
	for i in range(0, pixel_count):
		n_pixels[i] = pixels[i]
	n_pixels.show()

