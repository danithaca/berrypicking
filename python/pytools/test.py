from unittest import TestCase
import warnings
from pytools.algorithms import find_match_tokens
from pytools.utils import deprecated, new_deprecated


class TestAlgorithm(TestCase):
    def testAlgorithms(self):
        self.assertEqual(['abcdef'], find_match_tokens('abcdef .', ' abcdef'))
        self.assertEqual(set(['abc', 'def']), set(find_match_tokens('xabc zdef .', ' abcdef')))
        self.assertEqual(set(['abc', 'def']), set(find_match_tokens(' zdef xabc.', ' abcdef')))


# class TestUtils(TestCase):
#     @deprecated
#     def dep(self):
#         print('dep')
#
#     def testDecorators(self):
#         self.dep()

@new_deprecated
def dep():
    print('dep')

dep()