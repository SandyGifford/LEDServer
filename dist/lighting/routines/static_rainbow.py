from PixelGroup.PixelGroupChain import PixelGroupChain
from utils.light_utils import make_multi_grad

def static_rainbow():
	chain = PixelGroupChain([120])

	chain.set_pixels_all(make_multi_grad([
		(255, 0, 0),
		(255, 127, 0),
		(255, 255, 0),
		(0, 255, 0),
		(0, 0, 255),
		(75, 0, 130),
		(148, 0, 211),
		(255, 0, 0),
		(255, 0, 0),
		(148, 0, 211),
		(75, 0, 130),
		(0, 0, 255),
		(0, 255, 0),
		(255, 255, 0),
		(255, 127, 0),
		(255, 0, 0),
	], 120, 0.25))