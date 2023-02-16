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