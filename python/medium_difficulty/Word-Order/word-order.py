from collections import OrderedDict

words = OrderedDict()
n = int(input())

for i in range(n):
    _word = input()
    if _word in words.keys():
        words[_word] += 1
    else:
        words[_word] = 1

print(len(words.keys()))

counts = ' '.join([str(i) for i in words.values()])
print(counts)