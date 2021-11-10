import math
from random import randint
from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import LED_COUNT
from utils.py_utils import run_loop

def pulse(color=(255, 0, 0), low_color=None, duration=1):
	chain = PixelGroupChain([LED_COUNT])

	if not low_color: low_color = (color[0] / 5, color[1] / 5, color[2] / 5)

	def loop():
		chain.fade_to_all(color, 0.05 * duration)
		chain.fade_to_all(low_color, 0.2 * duration)
		chain.fade_to_all(color, 0.05 * duration)
		chain.fade_to_all(low_color, 0.7 * duration)

	run_loop(loop)
