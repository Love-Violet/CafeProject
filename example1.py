import sys
quantity = []
item = []
shopping_list = {}


table2 = {
    'Espresso': [5.50, 5.89, 'Yes', 'Coffee'],
    'Iced Coffee': [4.95, 5.30, 'No', 'Coffee'],
    'Latte': [4.95, 5.30, 'No', 'Coffee'],
    'Earl Grey': [4.50, 4.82, 'No', 'Tea'],
    'Sakura Green Tea': [5.00, 5.35, 'Yes', 'Tea'],
    'Chamomile Peppermint Tea': [5.00, 5.35, 'No', 'Tea'],
    'Brownie Gelato': [4.95, 5.30, 'Yes', 'Desserts'],
    'Strawberry Pudding': [4.25, 4.55, 'No', 'Desserts'],
    'Chocolate Cheesecake': [5.90, 6.31, 'Yes', 'Desserts']
}
infinity = 0


def main():
    option = input('1, 404:')
    if option == '1':
        test()
    if option == '404':
        sys.exit()


def test():
    while infinity == 0:
            input_item = input(' Please enter the item you wish to add in the shopping list (Do note Input is case sensitive)\n To go back to main menu, type return\n Please type here: ')
            if input_item == 'return':
                break
            item_quantity = int(input('How many of ' + input_item + ', do you want to add? '))
            if input_item in shopping_list:
                x = shopping_list.get(input_item)
                x += item_quantity
                shopping_list[input_item] = x
            elif input_item in table2:
                item.append(input_item)
                quantity.append(item_quantity)
                for o in range(0, len(item)):
                    shopping_list[item[o]] = quantity[o]


main()
