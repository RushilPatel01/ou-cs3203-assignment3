def sum_Of_List(number_List):

    sum = 0

    for number in number_List:
        sum = sum + number

    return sum

def product_Of_List(number_List):

    product = number_List[0]

    for number in number_List[1:]:
        product = product * number

    return product

if __name__ == '__main__':

    list_Of_Numbers = []

    print('Press "Enter" after each number. Type "Done" when finished.')

    while True:
        add_To_List = input()
        if add_To_List == "Done":
            break
        list_Of_Numbers.append(int(add_To_List))

    print(f"Sum of list: {sum_Of_List(list_Of_Numbers)}")
    
    print(f"Product of list: {product_Of_List(list_Of_Numbers)}")