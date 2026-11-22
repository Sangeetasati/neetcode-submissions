class Solution:
    def isPalindrome(self, s: str) -> bool:
        parse_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        start = 0
        end = len(parse_string)-1
        res = True
        while start<end:
            print(parse_string[start].lower(), parse_string[end].lower())
            if parse_string[start].lower() != parse_string[end].lower():
                res =  False
            start +=1
            end -=1

        return res



        
