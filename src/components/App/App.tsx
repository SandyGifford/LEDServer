import React from "react";
import { WSHelperClient } from "../../WSHelper";
import { ErrorBoundary } from "react-error-boundary";
import DOMUtils from "../../utils/DOMUtils";
import Thinker from "../Thinker/Thinker";
import ColorDataPicker from "../ColorDataPicker/ColorDataPicker";
import { ColorData, ServerWebsocketDataMap } from "../../../dist/typings";

interface AppProps {}

const App: React.FunctionComponent<AppProps> = ({}) => {
	const [loading, setLoading] = React.useState(true);
	const [colorData, setColorData] = React.useState<ColorData | null>(null);
	const sendColorDataRef = React.useRef((color: ColorData) => {});

	React.useEffect(() => {
		setLoading(true);
		fetch("wsPort")
			.then(r => r.json())
			.then(({ wsPort }: { wsPort: number }) => {
				const ws = new WSHelperClient<ServerWebsocketDataMap>(`ws://${location.hostname}:${wsPort}/`);
				ws.addMessageListener("colorData", c => setColorData(c));
				ws.addEventListener("open", () => setLoading(false));
				ws.addEventListener("close", () => setLoading(true));
				ws.open();
				sendColorDataRef.current = colorData => ws.send("colorData", colorData);
			});
	}, []);

	return <div className="App">
		<ErrorBoundary
			onReset={() => setColorData(null)}
			fallbackRender={({ error, resetErrorBoundary }) => <div className="App__error">
				<div className="App__error__message">Error: {error}</div>
				<button className="App__error__button" onClick={resetErrorBoundary}>retry</button>
			</div>}>
			{
				colorData ?
					<ColorDataPicker
						className={DOMUtils.className("App__picker", { mods: {loading} })}
						colorData={colorData}
						onColorDataChange={colorData => {
							sendColorDataRef.current(colorData);
							setColorData(colorData);
						}} /> :
					null
			}
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

