export type Color = [number, number, number];

export interface ServerWebsocketDataMap {
	colorData: ColorData;
}

export type ColorData = SolidColorColorData | GradientColorData;
export type ColorDataType = ColorData["type"];

export type ColorDataMap = {
	[T in ColorDataType]: Extract<ColorData, { type: T }>;
};

export interface ColorDataBase<T extends ColorDataType> {
	type: T;
}

export interface SolidColorColorData extends ColorDataBase<"solidColor"> {
	color: Color;
}

export interface GradientStop {
	color: Color;
	frac: number;
}

export interface GradientColorData extends ColorDataBase<"gradient"> {
	stops: GradientStop[];
}
