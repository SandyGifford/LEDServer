def run_loop(action):
	try:
		while True:
			action()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt detected, closing...")