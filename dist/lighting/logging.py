from .consts import LOG_PATH, LOG_LEVEL
import os
import logging

if LOG_PATH and not os.path.exists(LOG_PATH):
	dir_path = os.path.dirname(LOG_PATH)
	if not os.path.exists(dir_path): os.makedirs(os.path.dirname(LOG_PATH))
	open(LOG_PATH, "w").close()

logging.basicConfig(filename=LOG_PATH, level=logging.getLevelName(LOG_LEVEL))
