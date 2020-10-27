n, m = input().split()

n_l = [int(el) for el in input().split()]
a_l = set([int(el) for el in input().split()])
b_l = set([int(el) for el in input().split()])

happiness = 0
for num in n_l:
    if num in a_l:
        happiness += 1
    if num in b_l:
        happiness -= 1

print(happiness)