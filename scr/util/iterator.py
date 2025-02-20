

class Iterator:

	def __init__(self, rearranger):
		self.rearranger = rearranger

	# repeat iterations till completion or 10 reps for checkpoint
	# completion is it creates a loop of numbers
	def iterate(self, num: int, digits: int, data: list = None) -> (bool, list):
		if (data == None):
			data = []
			data.append(num)

		if (not isinstance(num, int) or
			type(num) == bool or
			not isinstance(digits, int) or
			type(digits) == bool or
			not isinstance(data, list)):
			raise TypeError(f'Expected:"num: int, digits: int, data: list" Got:"num: {type(num)}, digits: {type(digits)}, data: {type(data)}"')
		if (num < 0 or digits < 0):
			raise ValueError(f'num and digits must be positive (num: {num}, digits: {digits})')

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