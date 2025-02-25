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
    @pytest.mark.parametrize('', [
    	()
    ], ids=[
    	''
    ])
    def testIteratorRearrangerValid(self):
        pass