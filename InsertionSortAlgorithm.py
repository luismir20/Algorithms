Numbers = [30, 21, 12, 55, 4]

for i in range(1, len(Numbers)):
    current_value = Numbers[i] 
    j = i - 1  

    while j >= 0 and Numbers[j] > current_value:
        Numbers[j + 1] = Numbers[j]
        j -= 1

    Numbers[j + 1] = current_value

print(Numbers)
