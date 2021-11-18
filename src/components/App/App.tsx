import React from "react";
import { WSAssistantClient } from "ws-assistant-client";
import { ErrorBoundary } from "react-error-boundary";
import DOMUtils from "../../utils/DOMUtils";
import Thinker from "../Thinker/Thinker";
import ColorDataPicker from "../ColorDataPicker/ColorDataPicker";
import { ColorData, ColorDataMap, ColorDataType, ServerWebsocketDataMap } from "../../../dist/typings";

interface AppProps {}

type ColorDataMapStoreNode<T extends ColorDataType> = { val: ColorDataMap[T] | null, set: (val: ColorDataMap[T]) => void };

const App: React.FunctionComponent<AppProps> = ({}) => {
	const [loading, setLoading] = React.useState(true);
	const [error, setError] = React.useState("");
	const colorDataMapStore = COLOR_DATA_TYPES.reduce((map, colorDataType) => {
		const [val, set] = React.useState<ColorData | null>(null);
		map[colorDataType] = {
			val: val as any,
			set,
		};
		return map;
	}, {} as {[T in ColorDataType]: ColorDataMapStoreNode<T>});

	const [activeColorDataType, setActiveColorDataType] = React.useState<ColorDataType | null>(null);
	const [selectedColorDataType, setSelectedColorDataType] = React.useState<ColorDataType | null>(null);
	const sendColorDataRef = React.useRef((color: ColorData) => {});
	const selectedColorData = selectedColorDataType ? colorDataMapStore[selectedColorDataType].val : null;

	console.log(activeColorDataType);

	React.useEffect(() => {
		setLoading(true);
		fetch("wsPort")
			.then(r => r.json())
			.then(({ wsPort }: { wsPort: number }) => {
				const ws = new WSAssistantClient<ServerWebsocketDataMap>(`ws://${location.hostname}:${wsPort}/`);
				let firstFrame = true;

				ws.addMessageListener("colorDataMap", colorDataMap => {
					Object.keys(colorDataMap)
						.forEach((colorDataType: ColorDataType) => {
							(colorDataMapStore[colorDataType] as ColorDataMapStoreNode<ColorDataType>).set(colorDataMap[colorDataType])
						});
				});

				ws.addMessageListener("colorData", colorData => {
					colorDataMapStore[colorData.type].set(colorData as any);
				});

				ws.addMessageListener("activeColorDataType", activeColorDataType => {
					setActiveColorDataType(activeColorDataType);
					if (firstFrame) setSelectedColorDataType(activeColorDataType);
				});

				ws.addEventListener("open", () => setLoading(false));
				ws.addEventListener("close", () => setLoading(true));
				ws.open();

				sendColorDataRef.current = colorData => ws.send("colorData", colorData);
			});
	}, []);

	return <div className="App">
		<ErrorBoundary
			onReset={() => setError("An unknown error occurred")}
			fallbackRender={({ error, resetErrorBoundary }) => <div className="App__error">
				<div className="App__error__message">Error: {error}</div>
				<button className="App__error__button" onClick={resetErrorBoundary}>retry</button>
			</div>}>
			{
				!error && selectedColorData ?
					<ColorDataPicker
						className={DOMUtils.className("App__picker", { mods: {loading} })}
						colorData={selectedColorData}
						onColorDataChange={colorData => {
							sendColorDataRef.current(colorData);
							colorDataMapStore[colorData.type].set(colorData as any);
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

import "./App.style";import { COLOR_DATA_TYPES } from "../../../dist/consts";

