def get_abanibi(word: str) -> str:

    nikood_letters = ['a', 'u', 'o', 'e', 'i']
    result = ""

    for idx, letter in enumerate(word):
        if letter in nikood_letters:
            result += letter + 'b' + letter
        else:
            result += letter
    return result

def get_abanibi_recursion(word: str) -> str:
    nikood_letters = ['a', 'u', 'o', 'e', 'i']
    if word == "":
        return ""

    first_letter = word[0]
    rest_word = word[1:]

    if first_letter in nikood_letters:
        return first_letter + 'b' + first_letter + get_abanibi_recursion(rest_word)
    else:
        return first_letter + get_abanibi_recursion(rest_word)

print("abanibi without recursion:")
abanibi_var = get_abanibi("ani ohev otach")
print(abanibi_var + "\n")

abanibi_recursion_var = get_abanibi_recursion("ani ohev otach")
print("abanibi with recursion:")
print(abanibi_recursion_var + "\n")

print(f"the results are the same: {abanibi_var == abanibi_recursion_var}.")