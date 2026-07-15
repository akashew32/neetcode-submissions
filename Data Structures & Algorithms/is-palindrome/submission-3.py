class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char
        startIndex = 0
        endIndex = len(cleaned_string)-1
        while startIndex < endIndex:
            while cleaned_string[startIndex] == " ":
                startIndex += 1
            while cleaned_string[endIndex] == " ":
                endIndex -= 1
            if cleaned_string[startIndex].lower() != cleaned_string[endIndex].lower():
                return False
            startIndex += 1
            endIndex -= 1
            
        return True