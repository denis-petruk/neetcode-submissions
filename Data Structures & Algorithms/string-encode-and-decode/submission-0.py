class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += i + " "
        return encoded_string 
    def decode(self, s: str) -> List[str]:
        decoded_strs = list()
        last_string = ""
        for i in s:
            if i != " ":
                last_string += i
            else:
                decoded_strs.append(last_string)
                last_string = ""
        return decoded_strs