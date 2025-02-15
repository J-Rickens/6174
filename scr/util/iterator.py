

class Iterator:

	def __init__(self, rearranger):
		self.rearranger = rearranger

	def iterate(self, num: int):
		pass

	def singleIteration(self, num: int, digits: int) -> int:
		numStr = self.rearranger.setZeros(num, digits)
		numHigh, numLow = self.rearranger.rearrange(numStr)
		newNum = int(numHigh) - int(numLow)
		return newNum