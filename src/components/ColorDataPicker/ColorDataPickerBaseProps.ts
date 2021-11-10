import { ColorData } from "../../../dist/typings";

export default interface ColorDataPickerBaseProps<T extends ColorData> {
	className: string;
	colorData: T;
	onColorDataChange(colorData: T);
}
