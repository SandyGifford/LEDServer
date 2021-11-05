import board
import neopixel
import math
import time
from light_utils import make_fill, to_pixels, get_faded_pixel

class PixelGroup:
	def __init__(self, size, GPIO=board.D18, offset=0, pixels=None, steps_per_second=50):
		self._size = size
		self._offset = offset
		self._pixels = pixels if pixels else neopixel.NeoPixel(GPIO, size + offset, auto_write=False)
		self._steps_per_second = steps_per_second

	def fill(self, color, render=True):
		self.set_pixels(make_fill(color, self._size), render)

	def set_pixels(self, pixels, render=True):
		pixel_count = len(pixels)
		for i in range(0, pixel_count):
			if i >= self._size: break
			self._pixels[i + self._offset] = pixels[i]
		if render: self._pixels.show()

	def fade_to_generator(self, color_or_pixels, step_count, render=True):
		from_pixels = []
		pixels = to_pixels(color_or_pixels, self._size)

		for i in range(self._offset, self._offset + len(pixels)):
			from_pixels.append(self._pixels[i])

		for i in range(0, step_count):
			self.set_pixels(list(map(
				(lambda p: get_faded_pixel(from_pixels[p], pixels[p], i / step_count)),
				range(0, len(from_pixels))
			)), render)
			yield

	def fade_to(self, color_or_pixels, seconds, render=True):
		step_count = math.floor(self._steps_per_second * seconds)
		wait_time = seconds / step_count
		gen = self.fade_to_generator(color_or_pixels, step_count, render)

		while(True):
			try:
				next(gen)
				time.sleep(wait_time)
			except StopIteration as e:
				break

		# clear up any rounding errors
		self.set_pixels(pixels, render)
