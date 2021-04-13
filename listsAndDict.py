def run():
    myList = [1, "Hello", True, 4.5]
    myDict = {"firstname": "Alex", "lastname": "Nieto"}


    superList = [
        {"firstname": "Alex", "lastname": "Nieto"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "rodelo"}
    ]

    superDitc = {
        "naturalNums": [1, 2, 3, 4, 5],
        "integerNums": [-1, -2, 0, 1, 2],
        "floatingNums": [1.1, 4.5, 6.43]
    }

    for key, value in superDitc.items():
        print(key, "-", value)
    
    for values in superList:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()