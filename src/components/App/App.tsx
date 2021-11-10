import React from "react";
import { RgbColor, RgbColorPicker } from "react-colorful";
import { WSHelperClient } from "../../WSHelper";
import { ErrorBoundary } from "react-error-boundary";
import DOMUtils from "../../utils/DOMUtils";
import Thinker from "../Thinker/Thinker";
import { ServerWebsocketDataMap } from "../../../dist/typings";

interface AppProps {}

const App: React.FunctionComponent<AppProps> = ({}) => {
	const [loading, setLoading] = React.useState(true);
	const [color, setColor] = React.useState<RgbColor>({ r: 0, g: 0, b: 0 });
	const setColorRef = React.useRef((color: RgbColor) => {});

	React.useEffect(() => {
		setLoading(true);
		fetch("wsPort")
			.then(r => r.json())
			.then(({ wsPort }: { wsPort: number }) => {
				const ws = new WSHelperClient<ServerWebsocketDataMap>(`ws://${location.hostname}:${wsPort}/`);
				ws.open();
				ws.addMessageListener("colorData", colorData => {
					switch (colorData.type) {
						case "solidColor":
							const [r, g, b] = colorData.color;
							setColor({ r, g, b })
							break;
					}
				});
				ws.addEventListener("open", () => setLoading(false));
				ws.addEventListener("close", () => setLoading(true));
				setColorRef.current = ({r, g, b}) => ws.send("colorData", {
					type: "solidColor",
					color: [r, g, b],
				});
			});
	}, []);

	return <div className="App">
		<ErrorBoundary
			onReset={() => setColor({ r: 0, g: 0, b: 0 })}
			fallbackRender={({ error, resetErrorBoundary }) => <div className="App__error">
				<div className="App__error__message">Error: {error}</div>
				<button className="App__error__button" onClick={resetErrorBoundary}>retry</button>
			</div>}>
			<RgbColorPicker
				className={DOMUtils.className("App__picker", { mods: { loading } })}
				color={{ ...color }}
				onChange={nColor => {
					if (
						nColor.r === color.r &&
						nColor.g === color.g &&
						nColor.b === color.b
					) return;

					setColorRef.current(nColor);
					setColor(nColor);
				}} />
			{
				loading ?
					<Thinker className="App__thinker" /> :
					null
			}
		</ErrorBoundary>
	</div>;
};

export default App;

import "./App.style";

