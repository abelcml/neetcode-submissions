class Solution:
    def isPalindrome(self, s: str) -> bool:
        
     

        string = "".join([i for i in s if (i != " ") and (i not in "?!'.,:;-()@#")])
        string = string.upper()

        if not string:
            return True

        for i in range(len(string)//2):
            if string[i] != string[-i-1]:
                return False
        
        return True
