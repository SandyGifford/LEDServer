import assert, { AssertionError } from "assert";
import { Color, ColorData } from "../../typings";

export function assertColor(color: Color): void {
	assert(Array.isArray(color), "color must be an array");
	assert(color.length === 3, "color must have exactly 3 components");
	color.forEach((comp, i) => {
		assert(typeof comp === "number" && comp === Math.abs(comp), `color component at index ${i} is not an integer`);
		assert(comp >= 0 && comp <= 255, `color component at index ${i} must be between 0 and 255`);
	})
}

export function assertColorData(colorData: ColorData): ColorData {
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
			throw new AssertionError({
				message: `unrecognized type '${(colorData as ColorData).type}'`
			});
	}
}
