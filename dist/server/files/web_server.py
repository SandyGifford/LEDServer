from flask import Flask, send_file, send_from_directory
from files.consts import WS_PORT, INDEX_PATH, WEB_PORT, SERVER_ENV, JS_PATH, CSS_PATH
import json
from waitress import serve

app = Flask(__name__)
@app.route("/")
def get_index():
	return send_file(INDEX_PATH)

@app.route("/wsPort")
def get_ws_port():
	return json.dumps({ "wsPort": WS_PORT })

@app.route("/js/<path:path>")
def get_js(path):
	return send_from_directory(JS_PATH, path)

@app.route("/css/<path:path>")
def get_css(path):
	return send_from_directory(CSS_PATH, path)

def start_web_server():
	if (SERVER_ENV == "PROD"): serve(app, host="0.0.0.0", port=WEB_PORT)
	else: app.run(debug=False, host="0.0.0.0", port=WEB_PORT)