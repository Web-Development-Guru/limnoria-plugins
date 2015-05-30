handlers = {}
handlers["youtube.com"] = self.handler_youtube
handlers["www.youtube.com"] = self.handler_youtube
handlers["youtu.be"] = self.handler_youtube
handlers["m.youtube.com"] = self.handler_youtube

def init():
	print("Initializing Youtube Plugin")


def run():
	print("Getting YouTube Title")