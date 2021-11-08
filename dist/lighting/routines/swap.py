import math
import asyncio
from random import randint
from PixelGroupChain import PixelGroupChain

def swap(color1=(255, 0, 255), color2=(0, 255, 0), seconds=5):
	chain = PixelGroupChain([60, 60])

	while True:
		asyncio.get_event_loop().run_until_complete(asyncio.gather(
			chain.fade_to_async(0, color1, seconds / 2),
			chain.fade_to_async(1, color2, seconds / 2)
		))
		asyncio.get_event_loop().run_until_complete(asyncio.gather(
			chain.fade_to_async(0, color2, seconds / 2),
			chain.fade_to_async(1, color1, seconds / 2)
		))