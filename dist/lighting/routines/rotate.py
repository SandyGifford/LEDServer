import math
import time
import asyncio
from utils.py_utils import run_loop
from utils.light_utils import make_multi_grad
from PixelGroup.PixelGroupChain import PixelGroupChain

def rotate(
	pixels = make_multi_grad([
		(255, 0, 0),
		(255, 127, 0),
		(255, 255, 0),
		(0, 255, 0),
		(0, 0, 255),
		(75, 0, 130),
		(148, 0, 211),
		(255, 0, 0)
	], 120),
	seconds=1
):
	PIXEL_COUNT = 120
	chain = PixelGroupChain([PIXEL_COUNT])
	wait_time = seconds / PIXEL_COUNT

	def loop():
		chain.set_pixels_all(pixels[:PIXEL_COUNT])
		pixels.append(pixels.pop(0))
		time.sleep(wait_time)

	run_loop(loop)
