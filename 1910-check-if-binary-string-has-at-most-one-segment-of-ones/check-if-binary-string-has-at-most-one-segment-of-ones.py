class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l=len(s)
        flag=0
        for i in range(l):
            if s[i]=='0':
                flag=1
            else:
                if flag:
                    return False
        return True
                