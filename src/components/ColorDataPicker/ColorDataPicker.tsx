import React from "react";
import { ColorData, ColorDataMap, ColorDataType } from "../../../dist/typings";
import DOMUtils from "../../utils/DOMUtils"
import ColorDataPickerGradient from "../ColorDataPickerGradient/ColorDataPickerGradient";
import ColorDataPickerSolidColor from "../ColorDataPickerSolidColor/ColorDataPickerSolidColor";
import ColorDataPickerBaseProps from "./ColorDataPickerBaseProps";




const colorDataPickers: { [T in ColorDataType]: React.FunctionComponent<ColorDataPickerBaseProps<ColorDataMap[T]>> } = {
	gradient: ColorDataPickerGradient,
	solidColor: ColorDataPickerSolidColor,
};




export interface ColorDataPickerProps {
	className?: string;
	colorData: ColorData;
	onColorDataChange(colorData: ColorData);
}

const ColorDataPicker: React.FunctionComponent<ColorDataPickerProps> = ({ className, colorData, onColorDataChange }) => {
	return <div className={DOMUtils.className("ColorDataPicker", { merge: [className] })}>{
		React.createElement(colorDataPickers[colorData.type] as React.FunctionComponent<ColorDataPickerBaseProps<ColorData>>, {
			className: "ColorDataPicker__picker",
			colorData,
			onColorDataChange,
		})
	}</div>;
};

export default ColorDataPicker;

import "./ColorDataPicker.style";

