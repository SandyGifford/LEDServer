from PixelGroup.PixelGroupChain import PixelGroupChain
from dist.lighting.consts import LED_COUNT

def off():
	chain = PixelGroupChain([LED_COUNT])
	chain.off_all()
