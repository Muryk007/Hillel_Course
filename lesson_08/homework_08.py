massive = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def find_sum (massive):
    for item in massive:
        try:
            numbers = [int(num.strip()) for num in item.split(",")]
            print(f'сума: {sum(numbers)}')
        except ValueError:
            print(f' "Не вдалось опрацювати елементи: {item}"')

find_sum(massive)