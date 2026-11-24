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
            # Find the first #
            i = 0
            while input_s[i] != "#":
                i += 1

            # Characters before # represent the length
            steps = int("".join(input_s[:i]))

            # Extract the word
            word = "".join(input_s[i + 1 : i + 1 + steps])
            res.append(word)

            # Delete: length + "#" + word
            del input_s[:i + 1 + steps]

        return res

            
