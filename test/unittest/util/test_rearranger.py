import pytest
import re
from scr.util.rearranger import Rearranger


class TestRearranger:

	'''
	Setup functions
	create class obj to use in tests
	'''
	@pytest.fixture(scope = 'class', autouse = True)
	def rearrangerObj(self, request):
		request.cls.rearrangerObj = Rearranger()


	'''
	tests for insertSubstring function
	test: TypeError calls, ValueError calls, Valid calls
	'''
	@pytest.mark.insertSubstring
	@pytest.mark.parametrize('s, sub, i', [
		('abcd', 'z', '5'),
		('abcd', False, 0),
		(5, 'z', 0),
		('abcd', 'z', True),
		(('a','b'), ['a'], {0:0}),
		('abcd', ('a',23), (-10,5))
		
	], ids=[
		'i-str', 'sub-bool', 's-int', 'i-bool',
		'mix-set', 'mix-tuple'
	])
	def testInsertSubstringTypeErrors(self, s, sub, i):
		errorMessage = f'Expected "s: str, sub: str, i: int" Got:"s: {type(s)}, sub: {type(sub)}, i: {type(i)}"'
		with pytest.raises(TypeError, match=re.escape(errorMessage)):
			self.rearrangerObj.insertSubstring(s,sub,i)

	@pytest.mark.insertSubstring
	@pytest.mark.parametrize('i', [-1, 5, (10)])
	def testInsertSubstringValueErrors(self, i):
		with pytest.raises(ValueError, match=re.escape('Index out of Bounds')):
			self.rearrangerObj.insertSubstring('abcd','z',i)

	@pytest.mark.insertSubstring
	@pytest.mark.critical
	@pytest.mark.parametrize('i, expected', [
		(0, 'zabcd'), (1, 'azbcd'), (4, 'abcdz')
	])
	def testInsertSubstringValid(self, i, expected):
		actual = self.rearrangerObj.insertSubstring('abcd','z',i)
		assert actual == expected


	'''
	tests for rearrange function
	test: Error calls, Valid calls
	'''
	@pytest.mark.rearrange
	@pytest.mark.parametrize('numstr, error, errorMessage', [
		(568, TypeError, 'numStr must be a String'),
		(['5','6','8'], TypeError, 'numStr must be a String'),
		('4R6', ValueError, 'String must only contain numbers'),
		('45.5', ValueError, 'String must only contain numbers'),
		('', ValueError, 'String is empty')
	])
	def testRearrangeErrors(self, numstr, error, errorMessage):
		with pytest.raises(error, match=re.escape(errorMessage)):
			self.rearrangerObj.rearrange(numstr)

	@pytest.mark.rearrange
	@pytest.mark.critical
	@pytest.mark.parametrize('numstr, expected', [
		('02', ('20', '02')),
		('4', ('4', '4')),
		('3948652354701293890', ('9998876554433322100', '0012233344556788999'))
	])
	def testRearrangeValid(self, numstr, expected):
		actual = self.rearrangerObj.rearrange(numstr)
		assert actual == expected


	'''
	tests for setZeros function
	test: TypeError calls, ValueError calls, Valid calls
	'''
	@pytest.mark.setZeros
	@pytest.mark.parametrize('num, digits', [
		(745, True), (False, 5), (54.3, '2'), ('', None)
	], ids=[
		'digits-bool', 'num-bool', 'float-str', 'empty'
	])
	def testSetZerosTypeErrors(self, num, digits):
		errorMessage = f'Expected "num: int, digits: int" Got:"num: {type(num)}, digits: {type(digits)}"'
		with pytest.raises(TypeError, match=re.escape(errorMessage)):
			self.rearrangerObj.setZeros(num, digits)

	@pytest.mark.setZeros
	@pytest.mark.parametrize('num, digits, errorMessage', [
		(568, -1, 'num and digits must be positive (num: 568, digits: -1)'),
		(-568, 3, 'num and digits must be positive (num: -568, digits: 3)'),
		(568, 2, 'num exceeds expected digits (has: 3, expected: 2')
	])
	def testRearrangeErrors(self, num, digits, errorMessage):
		with pytest.raises(ValueError, match=re.escape(errorMessage)):
			self.rearrangerObj.setZeros(num, digits)

	@pytest.mark.setZeros
	@pytest.mark.critical
	@pytest.mark.parametrize('num, digits, expected', [
		(3748, 4, '3748'),
		(2, 5, '00002'),
		(356, 0, '356')
	])
	def testSetZerosValid(self, num, digits, expected):
		actual = self.rearrangerObj.setZeros(num, digits)
		assert actual == expected