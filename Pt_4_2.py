def find_palindromes(s):
    palindromes = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            stroke = s[i:j]
            reversed_stroke = "".join(reversed(stroke))
            if stroke == reversed_stroke:
                if len(stroke) > 1:
                    palindromes.append(stroke)
    return palindromes


phrase = input("Введите строку: ")
palindromes_stroke = find_palindromes(phrase)
print("Палиндромы в введенной строке:", palindromes_stroke)
