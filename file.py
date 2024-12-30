a, b, c, d = int(input()), int(input()), int(input()), int(input())
minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c
if d < minimum:
    minimum = d

print(minimum)