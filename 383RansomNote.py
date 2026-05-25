class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNotee=[0]*26
        magazinee=[0]*26
        for char in ransomNote:
            ransomNotee[ord(char)%26]+=1
        for charm in magazine:
            magazinee[ord(charm)%26]+=1
        for char in ransomNote:
            if ransomNotee[ord(char)%26]>magazinee[ord(char)%26]:
                return False
        return True