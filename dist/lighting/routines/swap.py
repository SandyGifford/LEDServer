import math
import asyncio
from dist.lighting.consts import LED_CONFIG
from utils.py_utils import run_loop
from PixelGroup.PixelGroupChain import PixelGroupChain

def swap(color1=(255, 0, 255), color2=(0, 255, 0), seconds=5):
	chain = PixelGroupChain(LED_CONFIG)

	def loop():
		asyncio.get_event_loop().run_until_complete(asyncio.gather(
			chain.fade_to_async(0, color1, seconds / 2),
			chain.fade_to_async(1, color2, seconds / 2)
		))
		asyncio.get_event_loop().run_until_complete(asyncio.gather(
			chain.fade_to_async(0, color2, seconds / 2),
			chain.fade_to_async(1, color1, seconds / 2)
		))

	run_loop(loop)
