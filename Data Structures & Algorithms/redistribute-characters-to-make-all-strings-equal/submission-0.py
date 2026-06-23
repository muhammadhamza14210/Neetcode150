class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for word in words:
            for letter in word:
                count[letter] = count.get(letter, 0) + 1

        for value in count.values():
            if value % len(words) != 0:
                return False
        return True