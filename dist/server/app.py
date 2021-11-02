import threading
from files.ws_server import thread_ws_server
from files.web_server import start_web_server
from files.consts import SERVER_ENV

ws_server_thread = threading.Thread(name="Websocket Server", target=thread_ws_server)
ws_server_thread.setDaemon(True)
ws_server_thread.start()

if SERVER_ENV != "LOCAL":
	from files.lights import thread_lights
	lights_thread = threading.Thread(name="LED Lights", target=thread_lights)
	lights_thread.setDaemon(True)
	lights_thread.start()

start_web_server()
