def vowel(chars):
    vowels ="codfarm"
    return chars in vowels
orgnlst = "mahiyan yan toton"
new_vowels = "".join(filter(vowel, orgnlst))
print("the vowels from the given string is:")
print(new_vowels)
