from random import randint
from PixelGroupChain import PixelGroupChain

def noise(comp_range=(0, 255), all_range=None, delay=0.25):
	PIXEL_COUNT = 120
	chain = PixelGroupChain([PIXEL_COUNT])

	def randomPixels(comp_range=(0, 255), all_range=None):
		pixels = []
		all_range = all_range or (comp_range, comp_range, comp_range)

		for i in range(0, PIXEL_COUNT):
			pixels.append((randint(all_range[0][0], all_range[0][1]), randint(all_range[1][0], all_range[1][1]), randint(all_range[2][0], all_range[2][1])))
		return pixels

	while True:
		chain.fade_to_all(randomPixels(comp_range=comp_range, all_range=all_range), delay)