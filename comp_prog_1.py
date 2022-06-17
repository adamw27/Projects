#You have L, a list containing some digits (0 to 9).
#Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3.
#If it is not possible to make such a number, return 0 as the solution.
#L will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, but each element in the list may only be used once.

import itertools

def solution(l):
    perms = []

    k = len(l)
    while k != 0:
        perms_created = list(itertools.permutations(l, k))
        perms.append(perms_created)
        k -= 1

    perms2 = [num for sublist in perms for num in sublist]
    perms_joined = [int(''.join(map(str, i))) for i in perms2]
    perms_sorted = sorted(perms_joined, reverse=True)

    number_found = 0
    for i in perms_sorted:
        if i % 3 == 0:
            number_found = i
            break

    print(number_found)

solution([3, 1, 4, 1, 5, 9])
solution([3, 1, 4, 1])
