class Solution:
    breaker = "&/br"
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += i + self.breaker
        return encoded_string 
    def decode(self, s: str) -> List[str]:
        decoded_strs = list()
        last_string = ""
        position = 0
        while position < len(s):
            if s[position:position + 4] != self.breaker:
                last_string += s[position]
                position += 1
            else:
                decoded_strs.append(last_string)
                position += 4
                last_string = ""
        return decoded_strs