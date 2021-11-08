import math
from random import randint
from PixelGroup.PixelGroupChain import PixelGroupChain

def noise(comp_range=(0, 255), all_range=None, delay=0.25, size=1):
	PIXEL_COUNT = 120
	group_count = math.floor(PIXEL_COUNT / size)
	leftover_count = PIXEL_COUNT % size

	chain = PixelGroupChain([PIXEL_COUNT])

	def randomPixels(comp_range=(0, 255), all_range=None):
		pixels = []
		all_range = all_range or (comp_range, comp_range, comp_range)

		def get_color():
			return (randint(all_range[0][0], all_range[0][1]), randint(all_range[1][0], all_range[1][1]), randint(all_range[2][0], all_range[2][1]))

		color = get_color()
		for i in range(0, leftover_count):
			pixels.append(color)

		for g in range(0, group_count):
			color = get_color()
			for i in range(0, size):
				pixels.append(color)
		return pixels

	while True:
		chain.fade_to_all(randomPixels(comp_range=comp_range, all_range=all_range), delay)