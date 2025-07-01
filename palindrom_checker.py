def check_palindrome(word = ""):
    word = word.lower()
    reversed_word = word[::-1].lower()
    if reversed_word == word:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome


print(check_palindrome("madam"))