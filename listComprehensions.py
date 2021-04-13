def main():
    list = []

    # for i in range(101):
    #     if (i % 3 == 0):
    #         pass
    #     else:
    #         list.append(i*i)
    # print(list)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    squares2 = [i for i in range(1,100000) if i % 36 == 0]
    print(squares2)

if __name__ == '__main__':
    main()