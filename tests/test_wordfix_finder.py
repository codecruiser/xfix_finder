from unittest import TestCase

from wordfix_finder import WordfixFinder


class TestWordfixFinder(TestCase):

    def setUp(self):
        self.word = 'abcdefg'
        self.wff = WordfixFinder()

    def test_find_fixes(self):
        fixes = ['a', 'ab', 'abc', 'dc', 'ef', 'cdef', 'efg', 'fg', 'g']

        self.wff.set_fixes(fixes)
        found_fixes = self.wff.search_for_fixes(self.word)

        self.assertEqual(found_fixes, [('ab', 'cdef', 'g')])
