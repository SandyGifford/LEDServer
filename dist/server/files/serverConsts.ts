import dotenv from "dotenv";
import path from "path";
import { ColorDataMap } from "../../typings";
dotenv.config()

function resolveEnvKey(key: string, defaultValue: string): string {
	if (!process.env[key]) return defaultValue;
	return process.env[key] as string;
}

export type ServerEnv = "PROD" | "DEV";
export type LogLevel = "NONE" | "ERROR" | "WARN" | "INFO" | "DEBUG";

export const NODE_LOG_LEVEL = resolveEnvKey("NODE_LOG_LEVEL", "INFO") as LogLevel;
export const NODE_LOG_PATH = process.env["NODE_LOG_PATH"];

export const BASE_PATH = path.join(__dirname, "../../../");
export const DIST_PATH = path.join(BASE_PATH, "dist");
export const BUILD_PATH = path.join(DIST_PATH, "build");
export const INDEX_PATH = path.join(BUILD_PATH, "index.html");
export const JS_PATH = path.join(BUILD_PATH, "js");
export const CSS_PATH = path.join(BUILD_PATH, "css");
export const WEB_PORT = parseInt(resolveEnvKey("WEB_PORT", "3000"));
export const WS_PORT = parseInt(resolveEnvKey("WS_PORT", "3001"));
export const SERVER_ENV = resolveEnvKey("SERVER_ENV", "DEV") as ServerEnv;
export const LED_CONFIG = resolveEnvKey("LED_CONFIG", "60,60").split(",").map(i => parseInt(i));
export const LED_COUNT = LED_CONFIG.reduce((count, i) => count + i, 0);
export const REDIS_PORT = parseInt(resolveEnvKey("REDIS_PORT", "6379"));

export const DEFAULT_COLOR_DATA: ColorDataMap = Object.freeze({
	gradient: {
		type: "gradient",
		stops: [{ frac: 0, color: [255, 0, 255] }, { frac: 0, color: [0, 255, 0] }],
	},
	solidColor: {
		type: "solidColor",
		color: [255, 0, 255],
	},
});
