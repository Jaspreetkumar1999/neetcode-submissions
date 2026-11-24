class Solution:

    def encode(self, strs: List[str]) -> str:
        decoded_str:str = ""
        for word in strs:
            decoded_str = f"{decoded_str}{len(word)}#{word}"
        return decoded_str

    def decode(self, s: str) -> List[str]:
        input_s = list(s)
        res = []
        while input_s:
            i = 0
            while input_s[i] != "#":
                i+=1
            steps = int("".join(input_s[:i])) 
            word = "".join(input_s[i+1 : i+1 + steps]) 
            res.append(word)

            del input_s[0: i+1 + steps]


        return res

            
