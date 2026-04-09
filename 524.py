class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort()
        def inS(S,word):
            l=0
            r=0
            for l in range(len(S)):
                if r==len(word):
                    return True
                if S[l]==word[r]:
                    r+=1
                    if r==len(word):
                        return True
            return False
        curr=""
        currmax=0
        for w in dictionary:
            if inS(s,w) and len(w)>currmax:
                curr=w
                currmax=len(w)
        return curr

