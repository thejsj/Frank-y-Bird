class Settings:

	def __init__(self):
		self.settings = {}

	def set(self, name, value):
		self.settings[name] = value

	def get(self, name):
		return self.settings[name]