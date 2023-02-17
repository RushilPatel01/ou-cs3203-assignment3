# Function that adds the numbers in a list together
def sum_Of_List(number_List):

    # Keep track of the total sum
    sum = 0
    
    # For loop that adds all the numbers together
    # in the given list
    for number in number_List:
        sum = sum + number

    return sum

# Function that multiplies the numbers in a list together
def product_Of_List(number_List):

    # Start by initializing the product variable
    # to the first element in the given list
    product = number_List[0]

    # For loop that starts at the second element,
    # and goes until the end of the given list,
    # until all numebers are multiplied together
    for number in number_List[1:]:
        product = product * number

    return product

# Function that reverses a list
def reverse_List(number_List):

    # Holds the reversed list
    reversed_List = []

    # For loop that goes through the given list and
    # inserts numbers at the beginning of the new list
    # to create the reversed order.
    for number in number_List:
        reversed_List.insert(0, number)

    return reversed_List

# Main method that gets numbers from user and puts them into a list to be added, multiplied, and reversed.
if __name__ == '__main__':

    list_Of_Numbers = []

    # Instructions to user
    print('Press "Enter" after each number. Type "Done" when finished.')

    # While loop that gets user input until they enter "Done". Adds
    # the user inputted numbers into a list
    while True:
        add_To_List = input()
        if add_To_List == "Done":
            break
        list_Of_Numbers.append(int(add_To_List))

    # Print sum of list
    print(f"Sum of list: {sum_Of_List(list_Of_Numbers)}")
    # Print product of list
    print(f"Product of list: {product_Of_List(list_Of_Numbers)}")
    # Print reverse of list
    print(f"Reverse list: {reverse_List(list_Of_Numbers)}")