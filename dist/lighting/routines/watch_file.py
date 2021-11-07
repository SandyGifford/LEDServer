import time
from PixelGroupChain import PixelGroupChain
from consts import COLOR_FILE_PATH

def watch_file():
	chain = PixelGroupChain([120])

	open(COLOR_FILE_PATH, "w").close()

	def read_color():
		color_file = open(COLOR_FILE_PATH, "r")
		string = color_file.read() or "0,0,0"
		color_file.close()
		array = string.split(",")
		return (int(array[0]), int(array[1]), int(array[2]))

	last_color = read_color()

	while True:
		color = read_color()
		if (
			color[0] != last_color[0] or
			color[1] != last_color[1] or
			color[2] != last_color[2]
		):
			chain.fade_to_all(color, 0.5)
			last_color = color

		time.sleep(1)