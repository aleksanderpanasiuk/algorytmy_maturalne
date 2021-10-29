def anagram(s, d):
    return sorted(s) == sorted(d)

s = input("s: ")
d = input("d: ")
print(anagram(s, d))
