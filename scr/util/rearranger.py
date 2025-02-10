

class Rearranger:
	def rearrange(self, numStr: str) -> tuple[str, str]:
		if (not isinstance(numStr, str)):
			raise TypeError('numStr must be a String')
		if (not numStr.isnumeric()):
			raise ValueError('String must only contain numbers')
		rehigh = numStr[0]
		relow = numStr[0]
		for n in numStr[1:]:
			i = 0
			while (i < len(rehigh) or int(rehigh[i]) > int(n)):
				i += 1
			il = len(rehigh) - i
			rehigh = self.insertSubstring(rehigh, n, i)
			relow = self.insertSubstring(relow, n, il)
		return rehigh, relow

	def insertSubstring(self, s: str, sub: str, i: int) -> str:
		if (not isinstance(s, str) or
			not isinstance(sub, str) or
			not isinstance(i, int) or
			type(i) == bool):
			raise TypeError(f'Expected "s: str, sub: str, i: int" Got:"s: {type(s)}, sub: {type(sub)}, i: {type(i)}"')
		if (i < 0 or i > len(s)):
			raise ValueError('Index out of Bounds')
		return s[:i] + sub + s[i:]

	def setZeros(self, num: int, digits: int) -> str:
		numStr = str(num)
		return numStr