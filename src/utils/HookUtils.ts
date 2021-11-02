import React from "react";

export default class HookUtils {
	public static useIsFirstFrame(): boolean {
		const firstFrame = React.useRef(true);
		const val = firstFrame.current;
		firstFrame.current = false;
		return val;
	}
}
