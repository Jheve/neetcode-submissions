class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)))      # add the str length before each word
            result.append('#')              # add a delimiter char before each word
            result.append(s)                # add the word
        
        # example: ["4#Hello", "4#World"]
        
        return "".join(result) 
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # increment j till it hits the separator char (indicates the str length)
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])        # turn the length into an integer
            
            # extract the next length chars --> original str
            i = j + 1                       
            j = i + length
            
            result.append(s[i:j])           # append extracted str to result
            i = j                           # increment i by length to decode next segment
        
        return result
        