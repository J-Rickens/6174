import pytest
from scr.util.rearranger import Rearranger

class TestRearranger:

	@pytest.fixture(scope = 'class', autouse = True)
	def rearrangerObj(self, request):
		request.cls.rearrangerObj = Rearranger()

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
		with pytest.raises(TypeError, match=errorMessage):
			self.rearrangerObj.insertSubstring(s,sub,i)

	@pytest.mark.parametrize('i', [-1, 5, (10)])
	def testInsertSubstringValueErrors(self, i):
		with pytest.raises(ValueError, match='Index out of Bounds'):
			self.rearrangerObj.insertSubstring('abcd','z',i)

	@pytest.mark.parametrize('i, expected', [
		(0, 'zabcd'), (1, 'azbcd'), (4, 'abcdz')
	])
	def testInsertSubstringValid(self, i, expected):
		actual = self.rearrangerObj.insertSubstring('abcd','z',i)
		assert actual == expected