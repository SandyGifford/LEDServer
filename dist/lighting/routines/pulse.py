import math
from random import randint
from PixelGroupChain import PixelGroupChain

def pulse(color=(255, 0, 0), low_color=None, duration=1):
	if not low_color: low_color = (color[0] / 5, color[1] / 5, color[2] / 5)
	PIXEL_COUNT = 120
	chain = PixelGroupChain([PIXEL_COUNT])

	while True:
		chain.fade_to_all(color, 0.05 * duration)
		chain.fade_to_all(low_color, 0.2 * duration)
		chain.fade_to_all(color, 0.05 * duration)
		chain.fade_to_all(low_color, 0.7 * duration)