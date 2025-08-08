st = list(input().strip())
vowels = "aeiouy"
result = []
for char in st:
    if char.lower() not in vowels:
        result.append('.' + char.lower())
print(''.join(result))