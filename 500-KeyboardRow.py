class Solution:
    def findWords(self, words):
        return [word for word in words if (set(word.lower())<=set('qwertyuiop')) or (set(word.lower())<=set('asdfghjkl')) or (set(word.lower())<=set('zxcvbnm'))]
