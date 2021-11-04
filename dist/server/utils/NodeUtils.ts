export default class NodeUtils {
	public static stayAlive(condition: () => boolean = () => true, interval = 500): void {
		const timer = setInterval(() => {
			if (!condition()) clearInterval(timer);
		}, interval);
	}

	public static async awaitAwake<T>(promise: Promise<T>, interval = 500): Promise<T> {
		const timer = setInterval(() => {/** */}, interval);
		return promise.then(r => {
			clearInterval(timer);
			return r;
		});
	}
}
