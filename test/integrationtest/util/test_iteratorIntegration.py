import pytest
from re import escape as reEscape
from unittest.mock import MagicMock

from scr.util.iterator import Iterator
from scr.util.rearranger import Rearranger


class TestIteratorIntagration:

    '''
    Setup functions
    create class obj to use in tests
    '''
    @pytest.fixture(scope = 'class' autouse = True)
    def makeRearrangerObj(self, request):
        rearrangerObj = Rearranger()
        request.cls.rearrangerObj = rearrangerObj
        return rearrangerObj

    @pytest.fixture(scope = 'class' autouse = True)    
    def makeIteratorObj(self, request, makeRearrangerObj):
        request.cls.iteratorObj = Iterator(makeRearrangerObj)



	'''
    Intagration tests
    test: Valid calls
    '''
    @pytest.mark.iterate
    @pytest.mark.parametrize('num, digits, data, expectedbool, expecteddata', [
    	(6174, 4, None, True, [6174,6174]),
        (9532, 4, [1111,2222,3333,4444,5555,6666,7777,8888,9999,1110,9532], True, [1111,2222,3333,4444,5555,6666,7777,8888,9999,1110,9532,8082,8532,6174,6174]),
        (2, 3, None, True, [2,198,791,791]),
        (7, 1, [7], True, [7,0,0]),
        (31, 0, None, True, [31,18,63,27,45,9,0,0])
    ], ids=[
    	'6174-4', '9541-4', '2-3', '7-1', '31-0'
    ])
    def testIteratorRearrangerValid(self, num, digits, data, expectedbool, expecteddata):
        actualbool, actualdata = self.iteratorObj(num, digits, data)
        assert actualbool == expectedbool
        assert actualdata == expecteddata