numbers = [23,20,17,8,29]

for number in range(len(numbers)-1): # set the number of passes
    for i in range(len(numbers)-1):
        print('Numbers before interation: '+ str(arr))
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        print('Numbers after iteration: '+ str(numbers))
        print('\n')
    print('End of pass {} \n'.format(j))