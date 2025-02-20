import pytest
from re import escape as reEscape
from unittest.mock import MagicMock

from scr.util.iterator import Iterator
from scr.util.rearranger import Rearranger


class TestIterator:

	'''
	Setup functions
	create class obj to use in tests
	'''
	@pytest.fixture(scope = 'class', autouse = True)
	def makeRearrangerMock(self, request):
		mock = MagicMock(spec=Rearranger)
		request.cls.rearrangerMock = mock
		return mock

	@pytest.fixture(scope = 'class', autouse = True)
	def makeIteratorObj(self, request, makeRearrangerMock):
		request.cls.iteratorObj = Iterator(makeRearrangerMock)

	@pytest.fixture(autouse = True)
	def resetRearrangerMock(self, request):
		request.cls.rearrangerMock.reset_mock()

	@pytest.fixture
	def makeIteratorObjMock(self, makeRearrangerMock):
		iteratorObj = Iterator(makeRearrangerMock)
		iteratorObj.singleIteration = MagicMock()
		return iteratorObj



	'''
	tests for setup function
	test: Iterator setup
	'''
	def testIteratorSetup(self):
		assert self.iteratorObj.rearranger is self.rearrangerMock


	'''
	tests for iterate function
	test: TypeError calls, Valid calls
	'''
	@pytest.mark.iterate
	@pytest.mark.parametrize('num, digits, data', [
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
	def testIterateTypeErrors(self, num, digits, data):
		errorMessage = f'Expected:"num: int, digits: int, data: list" Got:"num: {type(num)}, digits: {type(digits)}, data: {type(data)}"'
		with pytest.raises(TypeError, match=reEscape(errorMessage)):
			self.iteratorObj.iterate(num, digits, data)

	@pytest.mark.iterate
	@pytest.mark.critical
	@pytest.mark.parametrize('num, digits, data, testdata, expectedBool, expectedData', [
		(7641, 4, None, [7641], True, [7641, 7641]),
		(1476, 4, None, [7641,7641], True, [1476, 7641, 7641])
	], ids=[
		'7641', '1476'
	])
	def testIterateValid(self, makeIteratorObjMock, num, digits, data, testdata, expectedBool, expectedData):
		makeIteratorObjMock.singleIteration.side_effect = testdata
		actualBool, actualData = makeIteratorObjMock.iterate(num, digits)
		assert actualBool == expectedBool
		assert actualData == expectedData


	'''
	tests for singleIteration function
	test: Valid calls
	'''
	@pytest.mark.singleIteration
	@pytest.mark.critical
	@pytest.mark.parametrize('num, digits, numStr, numSet, expected', [
		(6174, 4, '6174', ('7641','1467'), 6174),
		(703, 5, '00703', ('73000','00037'), 72963),
		(7, 1, '7', ('7','7'), 0)
	], ids=[
		'6174', 'leading 0s', '0ed'
	])
	def testsingleIterationValid(self, num, digits, numStr, numSet, expected):
		self.rearrangerMock.setZeros.return_value = numStr
		self.rearrangerMock.rearrange.return_value = numSet

		actual = self.iteratorObj.singleIteration(num, digits)

		assert actual == expected
		self.rearrangerMock.setZeros.assert_called_once_with(num, digits)
		self.rearrangerMock.rearrange.assert_called_once_with(numStr)