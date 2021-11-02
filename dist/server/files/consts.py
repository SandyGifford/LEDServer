from dotenv import load_dotenv
load_dotenv()
import os

def resolve_env_key(key, default):
	if (
		(key not in os.environ) or
		(not os.environ[key])
	): return default
	return os.environ[key]

DIST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
BUILD_PATH = os.path.join(DIST_PATH, "build")
INDEX_PATH = os.path.join(BUILD_PATH, "index.html")
JS_PATH = os.path.join(BUILD_PATH, "js")
CSS_PATH = os.path.join(BUILD_PATH, "css")
WEB_PORT = resolve_env_key("WEB_PORT", 3000)
WS_PORT = resolve_env_key("WS_PORT", 3001)
SERVER_ENV = resolve_env_key("SERVER_ENV", "DEV")
