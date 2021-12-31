if __name__ == '__main__':
    print("Enter a roman number: ",end=" ")
    string = str(input())
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(string)):
        if i > 0 and roman[string[i]] > roman[string[i - 1]]:
            integer += roman[string[i]] - 2 * roman[string[i - 1]]
        else:
            integer += roman[string[i]]
    print(integer)
