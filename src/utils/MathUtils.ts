export default class MathUtils {
	public static clamp(value: number, min: number, max: number): number {
		return Math.min(max, Math.max(min, value));
	}

	public static slide(frac: number, min: number, max: number): number {
		return min + (max - min) * frac;
	}
}