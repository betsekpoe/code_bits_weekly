def check_palindrome(word = ""):
    word = word.lower()
    reversed_word = word[::-1].lower()
    if reversed_word == word:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome


# Example usage:
print(check_palindrome("racecar"))  # True
print(check_palindrome("leveler"))  # False