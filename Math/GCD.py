'''
Docstring for GCD

GCD/HCF

Example 1:
Input: N1 = 9, N2 = 12

Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)

Example 2:
Input: N1 = 20, N2 = 15

Output: 5
Explanation:
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 15: 1, 3, 5, 15
Common Factors: 1, 5
Greatest common factor: 5 (GCD)

'''
def gcd(n1 , n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    if n1 == 0:
        return n2
    else:
        return n1