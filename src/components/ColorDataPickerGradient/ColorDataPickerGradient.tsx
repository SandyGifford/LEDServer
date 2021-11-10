import React from "react";
import { GradientColorData } from "../../../dist/typings";
import DOMUtils from "../../utils/DOMUtils"
import ColorDataPickerBaseProps from "../ColorDataPicker/ColorDataPickerBaseProps";

const ColorDataPickerGradient: React.FunctionComponent<ColorDataPickerBaseProps<GradientColorData>> = ({ className }) => {
	return <div className={DOMUtils.className("ColorDataPickerGradient", { merge: [className] })}>
	</div>;
};

export default ColorDataPickerGradient;

import "./ColorDataPickerGradient.style";
