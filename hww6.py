def BigCharacter(word):
    first_character_small = word[0]
    first_character_big = chr(ord(first_character_small) - ord('a') + ord('A'))
    return first_character_big + word[1:]
 
source = input("Введи слова через пробел: ").split()
res = []
for word in source:
    res.append(BigCharacter(word))
print(' '.join(res))
