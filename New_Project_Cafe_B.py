import sys
import webbrowser

table1 = [['Espresso', 5.50, 5.89, 'Yes', 'Coffee'],
          ['Iced Coffee', 4.95, 5.30, 'No', 'Coffee'],
          ['Latte', 4.95, 5.30, 'No', 'Coffee'],
          ['Earl Grey', 4.50, 4.82, 'No', 'Tea'],
          ['Sakura Green Tea', 5.00, 5.35, 'Yes', 'Tea'],
          ['Chamomile Peppermint Tea', 5.00, 5.35, 'No', 'Tea'],
          ['Brownie Gelato', 4.95, 5.30, 'Yes', 'Desserts'],
          ['Strawberry Pudding', 4.25, 4.55, 'No', 'Desserts'],
          ['Chocolate Cheesecake', 5.90, 6.31, 'Yes', 'Desserts']]
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
shopping_list = {}
item = []
quantity = []


def main():
    while True:
        print('{:^85s}' .format('---Dan Cafe---'))
        print('{:^85s}\n\nSelect a number for the action that you would like to do:\n\n1. View Cafe Menu\n2. Add item to shopping list\n3. Remove item from shopping list\n4. View Shopping list\n5. Check-Out\n6. Advertisement\n9. Exit' .format('---Cafe Menu---'))
        selection = input('Make your selection: ')
        if selection == '1':
            cafe_menu()
        elif selection == '2':
            add_item()
        elif selection == '3':
            remove_item()
        elif selection == '4':
            view_item()
        elif selection == '5':
            checkout()
        elif selection == '6':
            advertisement()
        elif selection == '9':
            sys.exit()
        else:
            print('You did not make a valid selection. Please try again')


def cafe_menu():
    print('{:^85s}' .format('---Cafe Menu---'))
    header()
    global i
    for i in table2:
        outcome_table2()
    print('Sorted by?\n 1 - Category\n 2 - Alphabetically\n 3 - Ascending Price\n 4 - Descending Price\n 5 - Add item in shopping list\n 6 - Checkout\n 9 - Go back to Main menu')
    global option_cafe_menu
    option_cafe_menu = input('Make your selection: ')
    if option_cafe_menu == '1':
        category_menu()
    elif option_cafe_menu == '2':
        alphabetically_menu()
    elif option_cafe_menu == '3':
        order_price()
    elif option_cafe_menu == '4':
        order_price()
    elif option_cafe_menu == '9':
        main()
    elif option_cafe_menu == '5':
        add_item()
    elif option_cafe_menu == '6':
        checkout()
    else:
        print('You did not make a valid selection. Please try again')
    cafe_menu()


def alphabetically_menu():
    print('{:^85s}' .format('---Cafe Menu---'))
    header()
    sorted_name = sorted(table2.keys(), key=lambda x: x.lower())
    global i
    for i in sorted_name:
        outcome_table2()
    option_menu1()
    alphabetically_menu()


def category_menu():
    print('{:^85s}' .format('---Cafe Menu---'))
    print('Which category did you want?\n 1 - Coffee\n 2 - Tea\n 3 - Dessert\n 4 - Add item in shopping list\n 5 - Checkout\n 8 - Go back to Cafe Menu\n 9 - Go back to Main menu')
    option = input('Make your selection: ')
    if option == '1':
        header()
        global i
        for i in table2:
            if i == 'Earl Grey':
                break
            else:
                outcome_table2()
    elif option == '2':
        header()
        for i in table2:
            if i == 'Brownie Gelato':
                break
            elif i == 'Espresso' or i == 'Iced Coffee' or i == 'Latte':
                continue
            else:
                outcome_table2()
    elif option == '3':
        header()
        for i in table2:
            if i == 'Brownie Gelato' or i == 'Strawberry Pudding' or i == 'Chocolate Cheesecake':
                outcome_table2()
            else:
                continue
    elif option == '8':
        cafe_menu()
    elif option == '9':
        main()
    elif option == '4':
        add_item()
    elif option == '5':
        checkout()
    else:
        print('You did not make a valid selection. Please try again')
    category_menu()


def order_price():
    print('{:^85s}' .format('---Cafe Menu---'))
    header()
    if option_cafe_menu == '3':
        table1.sort(key=lambda x: x[1], reverse=False)
    elif option_cafe_menu == '4':
        table1.sort(key=lambda x: x[1], reverse=True)
    for ap in table1:
        print('| {:12s}| {:<28s}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(ap[4], ap[0], ap[1], ap[2], ap[3]))
    option_menu1()
    order_price()


def header():
    print('| Category    | Item                        | Price Exclusive GST | Price Inclusive GST(7%)| Membership Discount(15%)|')


def outcome_table2():
    table2_outcome = table2.get(i, ['', '', '', ''])
    print('| {:12s}| {:<28s}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(table2_outcome[3], i, table2_outcome[0], table2_outcome[1], table2_outcome[2]))


def option_menu1():
    print('Select a number for the action that you would like to do:\n 1 - Add item in shopping list\n 2 - Checkout\n 8 - Go back to Cafe menu\n 9 - Go back to Main menu')
    option = input('Make your selection: ')
    if option == '8':
        cafe_menu()
    elif option == '9':
        main()
    elif option == '1':
        add_item()
    elif option == '2':
        checkout()
    else:
        print('You did not make a valid selection. Please try again')


def add_item():
    while True:
        input_item = input(' Please enter the item you wish to add in the shopping list (Do note Input is case sensitive)\n If you want to add more, please enter the item name and input the amount that you wish to add (Do note Input is case sensitive)\n To go back to main menu, type return\n Please type here: ')
        if input_item == 'return':
            main()
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
        else:
            print('Please in put the correct: ')
        continue_adding = input('Do you want to continue adding?: ')
        if continue_adding == 'Yes' or continue_adding == 'yes' or continue_adding == 'Y' or continue_adding == 'y':
            continue
        else:
            break


def remove_item():
    while True:
        view_item()
        item_remove = input(' Please enter the item you wish to remove in the shopping list (Do note Input is case sensitive)\n If you want to subtract the quantity, please enter the item name and input the amount that you wish to subtract (Do note Input is case sensitive)\n To go back to main menu, type return\n Please type here: ')
        if item_remove == 'return':
            main()
        remove_quantity = int(input('How many of ' + item_remove + ', do you want to remove? '))
        if item_remove in shopping_list:
            if remove_quantity >= shopping_list[item_remove]:
                shopping_list.pop(item_remove)
            else:
                remove = shopping_list.get(item_remove)
                remove -= remove_quantity
                shopping_list[item_remove] = remove
        continue_adding = input('Do you want to continue removing?: ')
        if continue_adding == 'Yes' or continue_adding == 'yes' or continue_adding == 'Y' or continue_adding == 'y':
            continue
        else:
            break


def view_item():
    print('{:^85s}' .format('---Shopping List---'))
    print('| Item                        | Quantity      | Price Exclusive GST | Price Inclusive GST(7%)| Membership Discount(15%)|')
    for view in shopping_list:
        for second in table2:
            if view == second:
                table2_outcome = table2.get(second, ['', '', '', ''])
                print('| {:28s}| {:<14.0f}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(view, shopping_list.get(view), (shopping_list.get(view) * table2_outcome[0]), (shopping_list.get(view) * table2_outcome[1]), table2_outcome[2]))
            else:
                continue


def checkout():
    while True:
        global price_before
        global member
        global promo_availability
        price_before = 0
        member = input("Are you a member?(To go back to main menu, type return): ")
        if member == 'return':
            main()
        elif member == 'n' or member == 'N' or member == 'No' or member == 'no':
            while True:
                promo_availability = input('Enter the promo code\n (If you do not have any promo code, type continue)\n Please type here: ')
                if promo_availability == '$1 off' or promo_availability == 'Bonus Discount' or promo_availability == 'continue':
                    break
                else:
                    print('You have enter wrongly')
        elif member == 'y' or member == 'Y' or member == 'Yes' or member == 'yes':
            pass
        else:
            print('You did not make a valid selection. Please try again')
            checkout()
        print('{:^85s}' .format('---Receipt---'))
        print('| Item                                        | Quantity      | Price      |')
        for view in shopping_list:
            for second in table2:
                if view == second:
                    table2_outcome = table2.get(second, ['', '', '', ''])
                    price_before += (shopping_list.get(view) * table2_outcome[0])
                    print('| {:44s}| {:<14.0f}| ${:<10.2f}|'. format(view, shopping_list.get(view), (shopping_list.get(view) * table2_outcome[0])))
                else:
                    continue
        total_discount()
        gst()
        while True:
            payment = input('\nSelect a number for the action that you would like to do:\n\n1 - Add items / add quantity\n2 - Remove items / Subtract quantity\n3 - Pay by Cash\n4 - Pay by Card\n9 - Return to main menu\n\nMake your selection: ')
            if payment == '3':
                print('\n' * 20)
                checkout_format()
                print('| {:>60s}| {:<11s}|\nPlease visit the nearest store near you and show this receipt at the cashier' . format('', 'CASH'))
                bonus()
                finish()
            elif payment == '4':
                print('\n' * 20)
                checkout_format()
                print('| {:>60s}| {:<11s}|' . format('', 'CARD'))
                bonus()
                webbrowser.open_new('https://www.paypal.com/')
                finish()
            elif payment == '9':
                main()
            elif payment == '1':
                add_item()
                checkout()
            elif payment == '2':
                remove_item()
                checkout()
            else:
                print('You did not make a valid selection. Please try again')


def checkout_format():
    global price_before
    print('{:^85s}' .format('---Receipt---'))
    print('| Item                                        | Quantity      | Price      |')
    for view in shopping_list:
        for second in table2:
            if view == second:
                table2_outcome = table2.get(second, ['', '', '', ''])
                price_before += (shopping_list.get(view) * table2_outcome[0])
                print('| {:44s}| {:<14.0f}| ${:<10.2f}|'. format(view, shopping_list.get(view), (shopping_list.get(view) * table2_outcome[0])))
            else:
                continue
    print('| {:>60s}| ${:<10.2f}|'. format('Total discount', total_discount_price))
    print('| {:>60s}| ${:<10.2f}|'. format('GST', gst_7))
    print('| {:>60s}| ${:<10.2f}|'. format('Total Price', gst_107))


def total_discount():
    global total_discount_price
    if member == 'y' or member == 'Y' or member == 'Yes' or member == 'yes':
        total_discount_price = member_discount()
    elif member == 'n' or member == 'N' or member == 'No' or member == 'no':
        total_discount_price = promo_discount()
    print('| {:>60s}| ${:<10.2f}|'. format('Total discount', total_discount_price))


def member_discount():
    discount_price = 0
    for view in shopping_list:
        for second in table2:
            if view == second:
                table2_outcome = table2.get(second, ['', '', '', ''])
                if table2_outcome[2] == 'Yes':
                    discount_price += (shopping_list.get(view) * table2_outcome[0] * 0.15)
                else:
                    continue
            else:
                continue
    return discount_price


def promo_discount():
    promo_amount = 0
    if promo_availability == '$1 off':
        promo_amount += 1
    elif promo_availability == 'Bonus Discount':
        promo_amount += 5
    return promo_amount


def bonus():
    if gst_107 >= 50:
        print('Free promo code: Bonus Discount')


def gst():
    global gst_7
    global gst_107
    gst_7 = (price_before - total_discount_price) * 0.07
    print('| {:>60s}| ${:<10.2f}|'. format('GST', gst_7))
    gst_107 = (price_before - total_discount_price) * 1.07
    print('| {:>60s}| ${:<10.2f}|'. format('Total Price', gst_107))


def advertisement():
    print('{:^85s}\n Promo code(non - member)*: $1 off\n\n Please copy the code after : and paste it when on check out\n free $5 off if your final balance in the receipt is $50 or more*\n\n\n* promo code only applicable to redeem as a non member' .format('---Advertisement---'))


def finish():
    to_continue = input('To continue press enter:')
    if to_continue == '':
        main()
    else:
        main()


main()
