from simple_websocket_server import WebSocket, WebSocketServer
import json
import numbers
from files.consts import WS_PORT
import os

def thread_ws_server():
	while True:
		try:
			print("starting ws_server on port " + str(WS_PORT))
			ws_server = WebSocketServer("", WS_PORT, WSColorServer)
			ws_server.serve_forever()
		except BaseException as e:
			print("{!r}; restarting web socket thread".format(e))
		else:
			print("exited normally, bad thread; restarting")

color = [0, 0, 0]
clients = []

def get_color_message():
	return json.dumps({
		"type": "color",
		"data": color
	})

def send_color(c, fromClient):
	global color
	assert type(c) == list, "color must be an array"
	assert len(c) == 3, "color array must be of length 3"
	for i, p in enumerate(c):
		assert isinstance(p, numbers.Number), "color component at index " + str(i) + " was not a number"

	color = c
	message = get_color_message()
	os.environ["LED_COLOR"] = ",".join(map(lambda c: str(c), color))

	for client in clients:
		if (fromClient != client): client.send_message(message)

class WSColorServer(WebSocket):
	def handle(self):
		try:
			message = json.loads(self.data)
			assert type(message["type"]) == str, "message type was not string"
			if (message["type"] == "color"): send_color(message["data"], self)
			else: raise Exception("did not recognize socket message type " + message["type"])
		except AssertionError as e:
			print("malformed request")
			print(e)
		except Exception as e:
			print("fail")
			print(e)

	def connected(self):
		print(self.address + " WS connection opened")
		clients.append(self)
		message = get_color_message()
		self.send_message(message)

	def handle_close(self):
		clients.remove(self)
		print(self.address + " WS connection closed")