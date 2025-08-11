x = 0
for _ in range(int(input())):
    s = input()
    if s[0] == '+' or s[-1] == '+':
        x += 1
    else:
        x -= 1
print(x)