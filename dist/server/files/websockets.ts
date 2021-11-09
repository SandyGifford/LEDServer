import { WSHelperServer, WSSHelperServer } from "wshelper";
import { Color } from "../../../src/typings/color";
import { ServerWebsocketDataMap } from "../typings";
import { COLOR_FILE_PATH, WS_PORT } from "./consts";
import fs from "fs-extra";

fs.ensureFileSync(COLOR_FILE_PATH);

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
	fs.writeFile(COLOR_FILE_PATH, Math.floor(new Date().getTime() / 1000) + "\n" + color.join(","));
	server.sendToAllExcept("color", [fromClient], color);
}
