import math
import time
import asyncio
from consts import LED_COUNT
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
	], LED_COUNT),
	seconds=1
):
	chain = PixelGroupChain([LED_COUNT])
	wait_time = seconds / LED_COUNT

	def loop():
		chain.set_pixels_all(pixels[:LED_COUNT])
		pixels.append(pixels.pop(0))
		time.sleep(wait_time)

	run_loop(loop)
