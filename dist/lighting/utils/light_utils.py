import board
import neopixel
import math
import os
import logging



def make_fill(color, pixel_count):
	pixels = []
	for i in range(0, pixel_count):
		pixels.append(color)
	return pixels

def to_pixels(color_or_pixels, pixel_count):
	return make_fill(color_or_pixels, pixel_count) if type(color_or_pixels) is tuple else color_or_pixels

def get_faded_comp(from_comp, to_comp, fraction):
	return (to_comp - from_comp) * fraction + from_comp

def get_faded_pixel(from_pixel, to_pixel, fraction):
	return [
		get_faded_comp(from_pixel[0], to_pixel[0], fraction),
		get_faded_comp(from_pixel[1], to_pixel[1], fraction),
		get_faded_comp(from_pixel[2], to_pixel[2], fraction)
	]


def make_grad(start_color, end_color, pixel_count):
	pixels = []
	diff_step = ((end_color[0] - start_color[0]) / pixel_count, (end_color[1] - start_color[1]) / pixel_count, (end_color[2] - start_color[2]) / pixel_count)

	for i in range(0, pixel_count):
		pixels.append((start_color[0] + i * diff_step[0], start_color[1] + i * diff_step[1], start_color[2] + i * diff_step[2]))

	return pixels


def make_multi_grad(colors, pixel_count):
	diff_count = len(colors) - 1
	if diff_count is 0: return make_fill(colors[0], pixel_count)
	per_color = math.floor(pixel_count / diff_count)
	leftover = pixel_count % diff_count
	pixels = make_grad(colors[0], colors[1], per_color + leftover)
	
	for i in range(1, diff_count):
		pixels += make_grad(colors[i], colors[i + 1], per_color)

	return pixels

def rotate_array(array):
	el = array[0]
	array = array[1:]
	array.append(el)
	return array



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
