a = 1
b = 1
result = [a, b]
while b < 55:
    a, b = b, a + b
    result.append(b)
print(result)


    