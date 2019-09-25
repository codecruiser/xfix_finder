

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
        # TODO: start combinning prefixes with suffixes starting from the
        #  longest and try to check if after disjoining of the fixes from the
        #  word it will find a root.
