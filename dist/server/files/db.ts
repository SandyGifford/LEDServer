import redis from "redis";
import { ColorData, ColorDataMap, ColorDataType } from "../../typings";
import { DEFAULT_COLOR_DATA, REDIS_PORT } from "./serverConsts";
import { promisify } from "util";
import { COLOR_DATA_TYPES } from "../../consts";

type DBFields = ColorDataType | "lastWrite" | "activeColorDataType";

const db = redis.createClient({
	port: REDIS_PORT,
});

export const dbGet: (field: DBFields) => Promise<null | string> = promisify(db.get).bind(db);
export const dbSet: (field: DBFields, value: string) => Promise<unknown> = promisify(db.set).bind(db);

export async function readActiveColorDataTypeFromDb(): Promise<ColorDataType> {
	const r = await dbGet("activeColorDataType")
	return r as ColorDataType || "solidColor";
}

export async function readLastWriteFromDb(): Promise<number> {
	const r = await dbGet("lastWrite");
	return parseFloat(r || "0");
}

export async function readColorDataFromDb<T extends ColorDataType>(colorDataType: T): Promise<ColorDataMap[T]> {
	const r = await dbGet(colorDataType);
	return r ? JSON.parse(r) : DEFAULT_COLOR_DATA[colorDataType];
}

export async function readColorDataMapFromDb(): Promise<ColorDataMap> {
	const colorDataTypes = await Promise.all(COLOR_DATA_TYPES.map(readColorDataFromDb));
	return colorDataTypes.reduce((map, data) => {
		map[data.type] = data as any;
		return map;
	}, {} as ColorDataMap);
}

export async function writeColorDataToDb(colorData: ColorData): Promise<void> {
	const [activeColorDataType] = await Promise.all([
		readActiveColorDataTypeFromDb(),
		dbSet(colorData.type, JSON.stringify(colorData))
	]);

	if (colorData.type === activeColorDataType) await updateLastWrite();
}

export async function writeColorDataMapToDb(colorDataMap: ColorDataMap): Promise<void> {
	const [activeColorDataType] = await Promise.all([
		readActiveColorDataTypeFromDb(),
		Promise.all(Object.keys(colorDataMap).map((colorDataType: ColorDataType) => {
			return dbSet(colorDataType, JSON.stringify(colorDataMap[colorDataType]));
		})),
	]);

	if (colorDataMap[activeColorDataType]) await updateLastWrite();
}

export async function writeActiveColorDataTypeToDb(activeColorDataType: ColorDataType): Promise<void> {
	await dbSet("activeColorDataType", activeColorDataType);
}

export async function updateLastWrite(): Promise<void> {
	await dbSet("lastWrite", Math.floor(new Date().getTime() / 1000) + "");
}
