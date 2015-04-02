from unittest import TestCase
from pytools.algorithms import find_match_tokens


class TestAlgorithm(TestCase):
    def testAlgorithms(self):
        self.assertEqual(['abcdef'], find_match_tokens('abcdef .', ' abcdef'))
        self.assertEqual(set(['abc', 'def']), set(find_match_tokens('xabc zdef .', ' abcdef')))
        self.assertEqual(set(['abc', 'def']), set(find_match_tokens(' zdef xabc.', ' abcdef')))