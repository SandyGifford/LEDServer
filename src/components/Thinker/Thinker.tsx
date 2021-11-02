import React from "react";
import DOMUtils from "../../utils/DOMUtils";

interface ThinkerProps {
	className?: string;
}

const Thinker: React.FunctionComponent<ThinkerProps> = ({className}) => {
	return <div className={DOMUtils.className("Thinker", { merge: [className] })} />;
};

export default Thinker;

import "./Thinker.style";
