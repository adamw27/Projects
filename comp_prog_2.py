#You have worked out that the algorithm has the following process:
#1) Start with a random minion ID n, which is a non-negative integer of length k in base b
#2) Define x and y as integers of length k. x has the digits of n in descending order, and y has the digits of n in ascending order
#3) Define z = x - y. Add leading zeros to z to maintain length k if necessary 4) Assign n = z to get the next minion ID, and go back to step 2
#For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999.
#Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.
#Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value.
#For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212]
#and it will stay in this cycle no matter how many times it continues iterating.
#Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.
#Given a minion ID as a string n representing a non-negative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10,
#write a function answer(n, b) which returns the length of the ending cycle of the algorithm above starting with n.
#For instance, in the example above, answer(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3.
#If the algorithm reaches a constant, such as 0, then the length is 1.

def to_base_n(int_base_10, n):
    residual = int(int_base_10)
    digits_base_n = []
    while residual >= n:
        r = residual % n
        digits_base_n.append(str(r))
        residual = (residual - r) // n
    digits_base_n.append(str(residual))
    return ''.join(digits_base_n[::-1])

def to_base_10(int_base_n, n):
    x = list(int_base_n[::-1])
    y_base_10 = 0
    for i, a in enumerate(x):
        y_base_10 += int(a) * (n ** i)
    return str(y_base_10)


def answer(n, b):
    k = len(n)
    m = n
    mini_id = []
    while m not in mini_id:
        mini_id.append(m)
        s = sorted(m)
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)
        if b == 10:
            z = int(x_descend) - int(y_ascend)
            m = str(z)
        else:
            int_m_10 = int(to_base_10(x_descend, b)) - int(to_base_10(y_ascend, b))
            m = to_base_n(str(int_m_10), b)

        m = (k - len(m)) * '0' + m
    print(mini_id)
    print(len(mini_id) - mini_id.index(m))

answer('1211', 3)
answer('210022', 3)