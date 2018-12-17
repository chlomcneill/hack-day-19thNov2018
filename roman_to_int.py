def roman_to_int(numeral):

    numeral = list(numeral) #Turn roman numeral input into list of individual letters
    total = 0
    numbers = [] 

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for char in numeral:
        numbers.append(values[char]) #Turn list of letters in list of equivalent values
    
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1 
    
    return total + num2

print(roman_to_int("MCMXCIV")) #1994
