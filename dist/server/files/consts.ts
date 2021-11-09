import dotenv from "dotenv";
import path from "path";
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
export const COLOR_FILE_PATH = path.join(DIST_PATH, "tmp/color.csv");
export const INDEX_PATH = path.join(BUILD_PATH, "index.html");
export const JS_PATH = path.join(BUILD_PATH, "js");
export const CSS_PATH = path.join(BUILD_PATH, "css");
export const WEB_PORT = parseInt(resolveEnvKey("WEB_PORT", "3000"));
export const WS_PORT = parseInt(resolveEnvKey("WS_PORT", "3001"));
export const SERVER_ENV = resolveEnvKey("SERVER_ENV", "DEV") as ServerEnv;
