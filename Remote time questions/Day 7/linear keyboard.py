if __name__ == '__main__':
    t = int(input())
    count = 0
    count_dict = {}
    for i in range(t):
        test_case = input()
        test_str = input()
        length = len(test_str)
        d = {}
        count = 0
        for index, key in enumerate(test_case):
            d[key] = index

        for j in range(1, length):
            count += abs(d[test_str[j]] - d[test_str[j - 1]])
        count_dict[i] = count
    for k in count_dict.values():
        print(k)
