class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str      # 5#hello3#abc2#hi

    def decode(self, s: str) -> List[str]:

        L = []
        subL = ""
        i = 0

        while i < len(s):
            
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1 : j+1 + length]

            L.append(word)
            i =j+1+length

            
        return L