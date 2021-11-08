from consts import PYTHON_LOG_PATH, PYTHON_LOG_LEVEL
import os
import logging

def init_logging():
	if PYTHON_LOG_PATH and not os.path.exists(PYTHON_LOG_PATH):
		dir_path = os.path.dirname(PYTHON_LOG_PATH)
		if not os.path.exists(dir_path): os.makedirs(os.path.dirname(PYTHON_LOG_PATH))
		open(PYTHON_LOG_PATH, "w").close()

	logging.basicConfig(
		filename=PYTHON_LOG_PATH,
		level= logging.getLevelName(PYTHON_LOG_LEVEL) if PYTHON_LOG_LEVEL else None
	)
