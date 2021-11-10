from dotenv import load_dotenv
load_dotenv()
import os

def resolve_env_key(key, default):
	if (
		(key not in os.environ) or
		(not os.environ[key])
	): return default
	return os.environ[key]

def process_path(path):
	if not path: return None
	return os.path.abspath(os.path.expanduser(path))


PYTHON_LOG_LEVEL = resolve_env_key("PYTHON_LOG_LEVEL", None)
PYTHON_LOG_PATH = process_path(resolve_env_key("PYTHON_LOG_PATH", None))
REDIS_PORT = int(resolve_env_key("REDIS_PORT", "6379"))
BASE_PATH = process_path(os.path.join(os.path.dirname(__file__), "../../"))
DIST_PATH = process_path(os.path.join(BASE_PATH, "dist"))
COLOR_FILE_PATH = process_path(resolve_env_key("COLOR_FILE_PATH", os.path.join(DIST_PATH, "tmp/color.csv")))
LED_CONFIG = map(int, resolve_env_key("LED_CONFIG", "60,60").split(","))
LED_COUNT = sum(LED_CONFIG)
