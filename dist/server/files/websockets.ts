import { WSSAssistantServer } from "ws-assistant-server";
import { ServerWebsocketDataMap } from "../../typings";
import { WS_PORT } from "./serverConsts";
import { readColorDataMapFromDb, readActiveColorDataTypeFromDb, writeColorDataMapToDb, writeColorDataToDb, writeActiveColorDataTypeToDb } from "./db";

const server = new WSSAssistantServer<ServerWebsocketDataMap>(WS_PORT);

server.onConnected(async (client, ip) => {
	console.log(`Opened websocket connection to ${ip}`);

	client.addMessageListener("colorDataMap", colorDataMap => {
		writeColorDataMapToDb(colorDataMap);
		server.sendToAllExcept("colorDataMap", [client], colorDataMap);
	});

	client.addMessageListener("activeColorDataType", activeColorDataType => {
		writeActiveColorDataTypeToDb(activeColorDataType);
	});

	client.addMessageListener("colorData", colorData => {
		writeColorDataToDb(colorData);
		server.sendToAllExcept("colorData", [client], colorData);
	});

	const [
		activeColorDataType,
		colorDataMap,
	] = await Promise.all([
		readActiveColorDataTypeFromDb(),
		readColorDataMapFromDb(),
	]);

	client.send("activeColorDataType", activeColorDataType);
	client.send("colorDataMap", colorDataMap);

	client.addEventListener("close", () => console.log(`Closed websocket connection to ${ip}`));
});
