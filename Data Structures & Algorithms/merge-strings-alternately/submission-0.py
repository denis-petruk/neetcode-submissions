class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        length1 = len(word1)
        length2 = len(word2)
        if length1 > length2:
            for index, char in enumerate(word2):
                answer += word1[index] + word2[index]
            return answer + word1[length2 ::]
        else:
            for index, char in enumerate(word1):
                answer += word1[index] + word2[index]
            return answer + word2[length1 ::]
