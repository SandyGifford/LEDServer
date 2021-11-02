import board
import neopixel
import math
import os
import time

PIXEL_COUNT = 120

n_pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write = False)

def loop_forever(action):
	try:
		while (True): action()
	except KeyboardInterrupt:
		print("\ngoodbye")

def make_grad(start_color, end_color, pixel_count, brightness = 1):
	pixels = []
	diff_step = ((end_color[0] - start_color[0]) / pixel_count, (end_color[1] - start_color[1]) / pixel_count, (end_color[2] - start_color[2]) / pixel_count)

	for i in range(0, pixel_count):
		pixels.append(((start_color[0] + i * diff_step[0]) * brightness, (start_color[1] + i * diff_step[1]) * brightness, (start_color[2] + i * diff_step[2]) * brightness))

	return pixels


def make_multi_grad(colors, pixel_count, brightness = 1):
	diff_count = len(colors) - 1
	if diff_count is 0: return make_fill(colors[0], pixel_count, brightness)
	per_color = math.floor(pixel_count / diff_count)
	leftover = pixel_count % diff_count
	pixels = make_grad(colors[0], colors[1], per_color + leftover, brightness)
	
	for i in range(1, diff_count):
		pixels += make_grad(colors[i], colors[i + 1], per_color, brightness)

	return pixels

def make_fill(color, pixel_count, brightness = 1):
	pixels = []
	for i in range(0, pixel_count):
		pixels.append(color)
	return pixels


def set_pixels(pixels):
	pixel_count = len(pixels)
	for i in range(0, pixel_count):
		n_pixels[i] = pixels[i]
	n_pixels.show()

def get_faded_comp(from_comp, to_comp, fraction):
	return (to_comp - from_comp) * fraction + from_comp

def get_faded_pixel(from_pixel, to_pixel, fraction):
	return [
		get_faded_comp(from_pixel[0], to_pixel[0], fraction),
		get_faded_comp(from_pixel[1], to_pixel[1], fraction),
		get_faded_comp(from_pixel[2], to_pixel[2], fraction)
	]

STEPS_PER_SECOND = 50

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

def multi_fade_pixels(pixel_groups, seconds):
	leg_count = len(pixel_groups)
	seconds_per_leg = seconds / leg_count
	diff_count = leg_count - 1
	for i in range(0, diff_count):
		fade_pixels(pixel_groups[i], pixel_groups[i + 1], seconds_per_leg)

def loop_fade(pixel_groups, seconds):
	leg_count = len(pixel_groups)
	seconds_per_leg = seconds / leg_count
	first_group = pixel_groups[0]
	last_group = pixel_groups[leg_count - 1]

	try:
		while (True):
			multi_fade_pixels(pixel_groups, seconds)
			fade_pixels(last_group, first_group, seconds_per_leg)
	except KeyboardInterrupt:
		print("goodbye")

def rotate_array(array):
	el = array[0]
	array = array[1:]
	array.append(el)
	return array

def loop_rotate_pixels(pixels, seconds, fade = False):
	pixel_count = len(pixels)
	seconds_per_leg = seconds / pixel_count
	
	try:
		while (True):
			if fade:
				to_pixels = rotate_array(pixels)
				fade_pixels(pixels, to_pixels, seconds_per_leg)
				pixels = to_pixels
			else:
				set_pixels(pixels)
				time.sleep(seconds_per_leg)
				pixels = rotate_array(pixels)
	except KeyboardInterrupt:
		print("goodbye")

last_color = (0, 0, 0)

def thread_lights():
	global last_color
	while True:
		try:
			print("starting lighting thread")
			while True:
				if "LED_COLOR" in os.environ:
					color_arr = os.environ["LED_COLOR"].split(",")
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
			print("{!r}; restarting lighting thread".format(e))
		else:
			print("exited normally, bad thread; restarting")

# RAINBOW = make_multi_grad([
# 	(255, 0, 0),
# 	(255, 127, 0),
# 	(255, 255, 0),
# 	(0, 255, 0),
# 	(0, 0, 255),
# 	(75, 0, 130),
# 	(148, 0, 211),
# 	(255, 0, 0),
# ], PIXEL_COUNT, 0.25)

# ANTI_RAINBOW = make_multi_grad([
# 	(255, 0, 0),
# 	(148, 0, 211),
# 	(75, 0, 130),
# 	(0, 0, 255),
# 	(0, 255, 0),
# 	(255, 255, 0),
# 	(255, 127, 0),
# 	(255, 0, 0),
# ], PIXEL_COUNT, 0.25)

# COTTON_CANDY = make_multi_grad([
# 	(255, 0, 255),
# 	(0, 255, 255),
# 	(255, 0, 255),
# 	(0, 255, 255),
# 	(255, 0, 255),
# 	(0, 255, 255),
# 	(255, 0, 255),
# 	(0, 255, 255),
# 	(255, 0, 255),
# 	(0, 255, 255),
# ], PIXEL_COUNT, 0.25)

# BUMBLE_BEE = make_multi_grad([
# 	(255, 255, 0),
# 	(0, 0, 0),
# 	(255, 255, 0),
# 	(0, 0, 0),
# 	(255, 255, 0),
# 	(0, 0, 0),
# 	(255, 255, 0),
# 	(0, 0, 0),
# 	(255, 255, 0),
# 	(0, 0, 0),
# ], PIXEL_COUNT, 0.25)

# loop_rotate_pixels(RAINBOW, 1)
