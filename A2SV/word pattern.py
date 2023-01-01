class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word=s.split()
        coll=[]
        if len(word)!=len(pattern):
            return False
        chartoword={}
        wordtochar={}
        for i in range(len(pattern)):
            coll.append(pattern[i])
            chartoword[pattern[i]]=word[i]
            wordtochar[word[i]]=pattern[i]
        for i in range(len(word)):
            if word[i]!=chartoword[coll[i]]:
                return False
        for i in chartoword:
            if wordtochar[chartoword[i]]!=i:
                return False
        return True
