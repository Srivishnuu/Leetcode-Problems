class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        m=""
        l1=len(word1)
        l2=len(word2)
        while i < l1 and j < l2:
            m += word1[i] +word2[j]
            i+=1
            j+=1
        if i < l1:
            m +=word1[i:]
        else:
            m +=word2[j:]
        return m

        word1="ab";word2="pq"

        