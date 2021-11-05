from logging_utils import init_logging
init_logging()

from PixelGroupChain import PixelGroupChain

chain = PixelGroupChain([60, 60])
chain.fill(0, (100, 0, 100), False)
chain.fill(1, (0, 100, 0), False)
chain.render()

chain.fade_to_all((100, 100, 0), 1)


# def get_color_from_env():
# 	if COLOR_ENV_KEY in os.environ:
# 		color_arr = os.environ[COLOR_ENV_KEY].split(",")
# 		return (int(color_arr[0]), int(color_arr[1]), int(color_arr[2]))
# 	else: return (255, 0, 0)

# PIXEL_COUNT = 120
# last_color = get_color_from_env()


# try:
# 	logging.info("starting lighting thread")
# 	while True:
# 		color = get_color_from_env()
# 		if (
# 			color[0] is not last_color[0] or
# 			color[1] is not last_color[1] or
# 			color[2] is not last_color[2]
# 		):
# 			fade_to(make_fill(last_color, PIXEL_COUNT), make_fill(color, PIXEL_COUNT), 0.5)
# 			last_color = color

# 		time.sleep(1)
# except KeyboardInterrupt as e:
# 	logging.info("exiting normally")
# except BaseException as e:
# 	logging.error("{!r}; restarting lighting thread".format(e))
# else:
# 	logging.error("exited normally, bad thread; restarting")