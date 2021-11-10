import { WSHelperServer, WSSHelperServer } from "wshelper";
import { Color, ServerWebsocketDataMap } from "../../typings";
import { REDIS_PORT, WS_PORT } from "./consts";
import redis from "redis";

const db = redis.createClient({
	port: REDIS_PORT,
});

let _color: Color = [255, 0, 255];

class AssertionException extends Error {}

function assert(assertion: boolean, message: string): void {
	if (!assertion) throw new AssertionException(message);
}

const server = new WSSHelperServer<ServerWebsocketDataMap>(WS_PORT);

server.onConnected((client, ip) => {
	console.log(`Opened websocket connection to ${ip}`);
	client.send("color", _color);
	client.addMessageListener("color", color => sendColor(color, client));
	client.addEventListener("close", () => console.log(`Closed websocket connection to ${ip}`));
});

function sendColor(color: Color, fromClient: WSHelperServer<ServerWebsocketDataMap>): void {
	assert(
		Array.isArray(color),
		"color is not an array"
	);
	assert(
		color.length === 3,
		`color is of length ${color.length} (expected 3)`
	);
	color.forEach((comp, i) => assert(
		typeof comp === "number",
		`type of color component at index ${i} was ${typeof comp} (expected number)`
	));

	_color = color;
	db.set("colors", color.join(","))
	db.set("write_time", Math.floor(new Date().getTime() / 1000) + "");
	server.sendToAllExcept("color", [fromClient], color);
}
