class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        encoded_string = ""

        for string in strs:
            string = string.encode('utf-8').hex()
            encoded_string += string + "."
        
        
        return (encoded_string[:-1] + ',')

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == ",":
            return [""]
        enc_list = s[:-1].split('.')
        decoded_strs = []

        for string in enc_list:
            decoded_strs.append(bytes.fromhex(string).decode('utf-8'))

        return decoded_strs
