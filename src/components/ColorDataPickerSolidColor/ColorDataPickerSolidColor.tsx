import React from "react";
import { SolidColorColorData } from "../../../dist/typings";
import DOMUtils from "../../utils/DOMUtils"
import ColorDataPickerBaseProps from "../ColorDataPicker/ColorDataPickerBaseProps";
import { RgbColorPicker } from "react-colorful";

const ColorDataPickerSolidColor: React.FunctionComponent<ColorDataPickerBaseProps<SolidColorColorData>> = ({
	className,
	colorData: { color: [r, g, b] },
	onColorDataChange
}) => {
	return <RgbColorPicker
		className={DOMUtils.className("ColorDataPickerSolidColor", { merge: [className] })}
		color={{ r, g, b }}
		onChange={color => {
			if (
				color.r === r &&
				color.g === g &&
				color.b === b
			) return;

			onColorDataChange({
				type: "solidColor",
				color: [color.r, color.g, color.b],
			});
		}} />;
};

export default ColorDataPickerSolidColor;

import "./ColorDataPickerSolidColor.style";
