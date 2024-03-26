from math import sqrt, pi, atan

r2 = sqrt(2)
r3 = sqrt(3)
r5 = sqrt(5)
tau = (1 + r5) / 2
tau2 = (3 + r5) / 2


def c(rad):
    return rad * 180 / pi


#      5
# 3  /  |
# | 2   |
# |/    |
# 5  3  2
# | \   |
# |  2  |
# |/   \|
# 2--3--5

print(
    """     5
3  /  |
| 2   |
|/    |
5  3  2
| \\   |
|  2  |
|/   \\|
2--3--5
"""
)

print(f"2-3: {c(atan(sqrt(2/(7+3*r5))))}")
print(f"2-5: {c(atan(1/tau))}")
print(f"2-2: {36}")
print(f"2-3-5: {90-c(atan(1/tau))}")
print(f"2-5-3: {90-c(atan(sqrt(2/(7+3*r5))))}")
