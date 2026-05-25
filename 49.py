class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        same_Ana = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in same_Ana:
                same_Ana[key] = []

            same_Ana[key].append(word)

        return list(same_Ana.values())