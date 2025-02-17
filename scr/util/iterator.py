

class Iterator:

	def __init__(self, rearranger):
		self.rearranger = rearranger

	# repeat iterations till completion or 10 reps for checkpoint
	# completion is it creates a loop of numbers
	def iterate(self, num: int, digits: int, data: list = None) -> (bool, list):
		if (data == None):
			data = []
			data.append(num)
		newNum = num
		for i in range(10):
			newNum = self.singleIteration(newNum, digits)
			data.append(newNum)
			if (newNum in data[:-1]):
				return True, data
		return False, data

	# completes a single iteration
	def singleIteration(self, num: int, digits: int) -> int:
		numStr = self.rearranger.setZeros(num, digits)
		numHigh, numLow = self.rearranger.rearrange(numStr)
		newNum = int(numHigh) - int(numLow)
		return newNum