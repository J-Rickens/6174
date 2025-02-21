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
	test: TypeError calls, ValueError calls, Valid calls
	'''
	@pytest.mark.iterate
	@pytest.mark.parametrize('num, digits, data', [
		(True, 4, None),
		(675, False, None),
		(1835, 4, (4253, 6853, 5321)),
		('5325', '4', ''),
		((6514,'465'), [4], None),
		({456:'fail'}, (3), [4253, 6853, 5321])
		
	], ids=[
		'num-bool', 'digits-bool', 'data-tuple',
		'all-str', 'mix-set1', 'mix-set2'
	])
	def testIterateTypeErrors(self, num, digits, data):
		if (data == None):
			errorMessage = f'Expected:"num: int, digits: int, data: list" Got:"num: {type(num)}, digits: {type(digits)}, data: {type([num])}"'
		else:
			errorMessage = f'Expected:"num: int, digits: int, data: list" Got:"num: {type(num)}, digits: {type(digits)}, data: {type(data)}"'
		with pytest.raises(TypeError, match=reEscape(errorMessage)):
			self.iteratorObj.iterate(num, digits, data)

	@pytest.mark.iterate
	@pytest.mark.parametrize('num, digits, data', [
		(568, -1, [568, 497]),
		(-568, 3, None)
	])
	def testIterateValueErrors(self, num, digits, data):
		errorMessage = f'num and digits must be positive (num: {num}, digits: {digits})'
		with pytest.raises(ValueError, match=reEscape(errorMessage)):
			self.iteratorObj.iterate(num, digits, data)

	@pytest.mark.iterate
	@pytest.mark.critical
	@pytest.mark.parametrize('num, digits, data, testdata, expectedBool, expectedData', [
		(7641, 4, None, [7641], True, [7641, 7641]),
		(1476, 4, None, [7641,7641], True, [1476, 7641, 7641]),
		(268, 3, [789,158,652,263], [123,456,158], True, [789,158,652,263,123,456,158]),
		(0, 0, None, [1,2,3,4,5,6,7,8,9,10,21,22,23], False, [0,1,2,3,4,5,6,7,8,9,10])
	], ids=[
		'1-round', '2-round', 'start-data', 'False-flag'
	])
	def testIterateValid(self, makeIteratorObjMock, num, digits, data, testdata, expectedBool, expectedData):
		makeIteratorObjMock.singleIteration.side_effect = testdata
		actualBool, actualData = makeIteratorObjMock.iterate(num, digits, data)
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