

class Rearranger:

	def rearrange(self, numStr: str) -> tuple[str, str]:
		if (not isinstance(numStr, str)):
			raise TypeError('numStr must be a String')
		if (not numStr):
			raise ValueError('String is empty')
		if (not numStr.isnumeric()):
			raise ValueError('String must only contain numbers')
		rehigh = numStr[0]
		relow = numStr[0]
		for n in numStr[1:]:
			i = 0
			while (i < len(rehigh) and int(rehigh[i]) > int(n)):
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
			raise TypeError(f'Expected:"s: str, sub: str, i: int" Got:"s: {type(s)}, sub: {type(sub)}, i: {type(i)}"')
		if (i < 0 or i > len(s)):
			raise ValueError('Index out of Bounds')
		return s[:i] + sub + s[i:]

	def setZeros(self, num: int, digits: int) -> str:
		if (not isinstance(num, int) or
			type(num) == bool or
			not isinstance(digits, int) or
			type(digits) == bool):
			raise TypeError(f'Expected:"num: int, digits: int" Got:"num: {type(num)}, digits: {type(digits)}"')
		if (num < 0 or digits < 0):
			raise ValueError(f'num and digits must be positive (num: {num}, digits: {digits})')

		numStr = str(num)
		if (digits == 0 or len(numStr) == digits):
			return numStr
		if (len(numStr) > digits):
			raise ValueError(f'num exceeds expected digits (has: {len(numStr)}, expected: {digits})')
		while (len(numStr) < digits):
			numStr = '0' + numStr
		return numStr