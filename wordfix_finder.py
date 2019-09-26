import re


class WordfixFinder:

    def set_fixes(self, fixes):
        """
        Sets fixes list.

        :param fixes: list of fixes
        """
        self.fixes = fixes

    def read_fixes(self, filename):
        """
        Reads lits of fixes from given filename.

        :param filename: filename where the fixes can be found
        """
        pass

    def search_for_fixes(self, word):
        """
        Searches for all possible combination of prefixes, roots and suffixes
         in the word.

        :param word: word in which fixes will be searched
        :return: list of possible fixes combination
        """
        # it means that it is probably a word without any pre and suffixes
        if word in self.fixes:
            return word
        possible_prefixes = []
        possible_suffixes = []
        for fix in self.fixes:
            if word.startswith(fix):
                possible_prefixes.append(fix)
            if word.endswith(fix):
                possible_suffixes.append(fix)

        possible_divitions = []
        for prefix in possible_prefixes:
            for suffix in possible_suffixes:
                word_cp = word
                word_cpp = re.sub(r'^{}'.format(prefix), '', word_cp)
                if word_cpp:
                    word_cps = re.sub(r'{}$'.format(suffix), '', word_cpp)
                    if word_cps and word_cps != word_cpp:
                        if word_cps in self.fixes:
                            possible_divitions.append(
                                (prefix, word_cps, suffix)
                            )
        return possible_divitions
