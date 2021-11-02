import threading
from files.ws_server import thread_ws_server
from files.web_server import start_web_server
from files.consts import SERVER_ENV, LOG_PATH, LOG_LEVEL
import os
import logging

if LOG_PATH and not os.path.exists(LOG_PATH):
	dir_path = os.path.dirname(LOG_PATH)
	if not os.path.exists(dir_path): os.makedirs(os.path.dirname(LOG_PATH))
	open(LOG_PATH, "w").close()

logging.basicConfig(filename=LOG_PATH, level=logging.getLevelName(LOG_LEVEL))

ws_server_thread = threading.Thread(name="Websocket Server", target=thread_ws_server)
ws_server_thread.setDaemon(True)
ws_server_thread.start()

if SERVER_ENV != "LOCAL":
	from files.lights import thread_lights
	lights_thread = threading.Thread(name="LED Lights", target=thread_lights)
	lights_thread.setDaemon(True)
	lights_thread.start()

start_web_server()
