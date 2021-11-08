import board
import neopixel
import time
import math
import asyncio
from light_utils import make_fill, to_pixels, get_faded_pixel
from PixelGroup import PixelGroup

class PixelGroupChain:
	def __init__(self, groups, GPIO=board.D18, pixels=None, steps_per_second=50):
		size = 0
		for g in groups: size += g
		self._size = size
		self._pixels = pixels if pixels else neopixel.NeoPixel(GPIO, size, auto_write=False)
		self._steps_per_second = steps_per_second
		self._queue = []
		
		self._groups = []
		offset = 0
		
		for size in groups:
			self._groups.append(PixelGroup(size, GPIO=GPIO, offset=offset, pixels=self._pixels, steps_per_second=steps_per_second))
			offset += size

	def render(self):
		self._pixels.show()

	def set_pixels(self, index, pixels, render=True):
		self._groups[index].set_pixels(pixels, render)

	def set_pixels_all(self, pixels, render=True):
		for i in range(0, self._size):
			if i >= self._size: break
			self._pixels[i] = pixels[i]
		if render: self._pixels.show()

	def fill(self, index, color, render=True):
		self._groups[index].fill(color, render)

	def fill_all(self, color, render=True):
		for group in self._groups:
			group.fill(color, False)
		if render: self.render()

	def fade_to(self, index, color_or_pixels, seconds):
		asyncio.get_event_loop().run_until_complete(self.fade_to_async(index, color_or_pixels, seconds))		

	def fade_to_all(self, color_or_pixels, seconds):
		asyncio.get_event_loop().run_until_complete(self.fade_to_all_async(color_or_pixels, seconds))

	async def fade_to_async(self, index, color_or_pixels, seconds):
		await self._groups[index].fade_to_async(color_or_pixels, seconds)

	async def fade_to_all_async(self, color_or_pixels, seconds):
		coroutines = map(
			(lambda group: group.fade_to_async(color_or_pixels, seconds)),
			self._groups
		)

		await asyncio.gather(*coroutines)