vovels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vovels:")
found = {}

for letter in word:
      if letter in vovels:
            if letter not in found:
                 found[letter] = 1
            else:
                  found[letter] += 1  
for k,v in sorted(found.items()):
      print(k,'was found', v,'times.')
