from PixelGroup.PixelGroupChain import PixelGroupChain

def off():
	PIXEL_COUNT = 120
	chain = PixelGroupChain([PIXEL_COUNT])
	chain.off_all()
