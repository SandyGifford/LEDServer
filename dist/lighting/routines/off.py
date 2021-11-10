from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import LED_COUNT

def off():
	chain = PixelGroupChain([LED_COUNT])
	chain.off_all()
