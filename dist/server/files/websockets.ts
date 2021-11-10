import { WSHelperServer, WSSHelperServer } from "wshelper";
import { Color, ColorData, ServerWebsocketDataMap } from "../../typings";
import { REDIS_PORT, WS_PORT } from "./consts";
import redis from "redis";

const db = redis.createClient({
	port: REDIS_PORT,
});

let colorData: ColorData = {
	type: "solidColor",
	color: [255, 0, 255]
};

class AssertionException extends Error {}

function assert(assertion: boolean, message: string): void {
	if (!assertion) throw new AssertionException(message);
}

const server = new WSSHelperServer<ServerWebsocketDataMap>(WS_PORT);

server.onConnected((client, ip) => {
	console.log(`Opened websocket connection to ${ip}`);
	client.send("colorData", colorData);
	client.addMessageListener("colorData", colorData => sendColorData(colorData, client));
	client.addEventListener("close", () => console.log(`Closed websocket connection to ${ip}`));
});

function assertColor(color: Color): void {
	assert(Array.isArray(color), "color must be an array");
	assert(color.length === 3, "color must have exactly 3 components");
	color.forEach((comp, i) => {
		assert(typeof comp === "number" && comp === Math.abs(comp), `color component at index ${i} is not an integer`);
		assert(comp >= 0 && comp <= 255, `color component at index ${i} must be between 0 and 255`);
	})
}

function assertColorData(colorData: ColorData): ColorData {
	assert(
		typeof colorData === "object",
		"color data is not an object"
	);

	assert(
		typeof colorData.type === "string",
		"color data must have a 'type' of type string"
	);

	switch (colorData.type) {
		case "gradient":
			assert(colorData.stops.length <= 20, "gradient may not contain more than 20 stops");
			const stops = colorData.stops.map((stop, i) => {
				assert(typeof stop.frac === "number", `gradient stop at position ${i} must be a number`);
				assertColor(stop.color);

				return {
					frac: stop.frac,
					color: stop.color,
				};
			});

			return {
				type: "gradient",
				stops,
			};
		case "solidColor":
			assertColor(colorData.color);
			return {
				type: "solidColor",
				color: colorData.color,
			};
		default:
			throw new AssertionException(`unrecognized type '${(colorData as ColorData).type}'`)
	}
}

function sendColorData(colorData: ColorData, fromClient: WSHelperServer<ServerWebsocketDataMap>): void {
	colorData = assertColorData(colorData);

	db.set("colorData", JSON.stringify(colorData));
	db.set("write_time", Math.floor(new Date().getTime() / 1000) + "");
	server.sendToAllExcept("colorData", [fromClient], colorData);
}
