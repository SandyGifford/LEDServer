from logging_utils import init_logging
init_logging()

from routines.watch_file import watch_file
from routines.static_rainbow import static_rainbow
from routines.noise import noise

noise(size=10)



# def rotate_array(array):
# 	return array[1:] + [array[0]]
# chain.fill_all((0, 0, 0))

# pixels = []

# for i in range(0, PIXEL_COUNT):
# 	if math.floor(i / 10) % 2 == 0: pixels.append((255, 0, 255))
# 	else: pixels.append((0, 255, 0))

# while True:
# 	pixels = rotate_array(pixels)
# 	chain.set_pixels_all(pixels)
# 	time.sleep(0.02)

