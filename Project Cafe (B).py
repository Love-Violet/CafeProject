import sys

def mainMenu():
    while True:
        print('### Dan Cafe ###')
        print('''### Main Menu ###
        
        Select a number for the action that you would like to do: 
        
        1. View Cafe Menu
        2. Preview on what is in your shopping list
        3. Remove item to shopping list
        4. Check-out
        5. Exit
        ''')

        selection = int(input('Make your selection: '))

        if selection == 1:
            cafeMenu()
        elif selection == 2:
            previewItem()
        elif selection == 3:
            removeItem()
        elif selection == 4:
            pass
        elif selection == 5:
            sys.exit()
        else:
            print('You did not make a valid selection. Please try again')

cafe_menu = ['Espresso', 'Iced Coffee', 'Latte', 'Earl Grey', 'Sakura Green Tea', 'Chamomole Peppermint Tea', 'Brownie Gelato', 'Stawberry Pudding', 'Chocolate Cheesecake']
priceEGST = [5.5, 4.95, 4.95, 4.5, 5, 5, 4.95, 4.25, 5.9]
anything = {
    'Latte': ['Description', 5.89, 'Yes']
}

anything['Espresso'] = 1

def cafeMenu():
    print('{:^85s}' .format('---Cafe Menu---'))
    print('{:25s}|{:^20s}|{:^20s}|{:^20s}'.format('Item', 'Price Exclusive GST', 'GST 7%', 'Membership Discount'))
    for i in range(len(cafe_menu)):
        if cafe_menu[i] == 'Espresso' or cafe_menu[i] == 'Sakura Green Tea' or cafe_menu[i] == 'Brownie Gelato' or cafe_menu[i] == 'Chocolate Cheesecake':
            membership_discount = 'Yes'
        else:
            membership_discount = 'No'
        print('{:25s}|{:^20.2f}|{:^20.2f}|{:^20s}' .format(cafe_menu[i], priceEGST[i], priceEGST[i]*0.07, membership_discount))
    def sort_menu():
        while True:
            print(' 1. Would you like sort  by category \n 2. Would you like sort cafe items alphabetically \n 3. Would you like sort cafe items by(ascending) price \n 4. If you wish not to sort the item \n 5. Back to main menu')
            sort = int(input('\nMake your selection: '))
            if sort == 1:
                category_menu()
            elif sort == 2:
                alphabet_menu()
            elif sort == 3:
                price_menu()
            elif sort == 4:
                normal_menu()
            elif sort == 5:
                break
            else:
                print('You did not make a valid selection. Please try again')
    def category_menu():
        print('{:^85s}' .format('---Cafe Menu---'))
        print('{:^20s}|{:25s}|{:^20s}|{:^20s}|{:^20s}'.format('Category', 'Item', 'Price Exclusive GST', 'GST 7%', 'Membership Discount'))
        for i in range(len(cafe_menu)):
            if cafe_menu[i] == 'Espresso' or cafe_menu[i] == 'Sakura Green Tea' or cafe_menu[i] == 'Brownie Gelato' or cafe_menu[i] == 'Chocolate Cheesecake':
                membership_discount = 'Yes'
            else:
                membership_discount = 'No'
            if i <= 2:
                cat1 = 'Coffee'
            elif i > 5:
                cat1 = 'Desserts'
            else:
                cat1 = 'Tea'
            print('{:^20s}|{:25s}|{:^20.2f}|{:^20.2f}|{:^20s}' .format(cat1, cafe_menu[i], priceEGST[i], priceEGST[i]*0.07, membership_discount))
        con = input('\nWould you like to continue adding item in the Shopping list?(Yes/No): ')
        while True:
            if con == 'Yes':
                item = input('Please enter the item you wish to add in to the shopping list: ')
                shopping_list.append(item)
                quan = int(input('How many of %s would you like to buy?: ' % (item)))
                quantity_list.append(quan)
                print('%2.0f of %s has been added to the shopping list.' % (quan, item))
                con = input('Would you like to continue adding item in the Shopping list?(Yes/No): ')
            else:
                break
    def alphabet_menu():
        print('{:^85s}' .format('---Cafe Menu---'))
        print('{:25s}|{:^20s}|{:^20s}|{:^20s}'.format('Item', 'Price Exclusive GST', 'GST 7%', 'Membership Discount'))
        cafe_menu.sort()
        priceEGST1 = [4.95, 5, 5.9, 4.5, 5.5, 4.95, 4.95, 5, 4.25]
        for i in range(len(cafe_menu)):
            if cafe_menu[i] == 'Espresso' or cafe_menu[i] == 'Sakura Green Tea' or cafe_menu[i] == 'Brownie Gelato' or cafe_menu[i] == 'Chocolate Cheesecake':
                membership_discount = 'Yes'
            else:
                membership_discount = 'No'
            print('{:25s}|{:^20.2f}|{:^20.2f}|{:^20s}' .format(cafe_menu[i], priceEGST1[i], priceEGST1[i]*0.07, membership_discount))
        con = input('\nWould you like to continue adding item in the Shopping list?(Yes/No): ')
        while True:
            if con == 'Yes':
                item = input('Please enter the item you wish to add in to the shopping list: ')
                shopping_list.append(item)
                quan = int(input('How many of %s would you like to buy?: ' % (item)))
                quantity_list.append(quan)
                print('%2.0f of %s has been added to the shopping list.' % (quan, item))
                con = input('Would you like to continue adding item in the Shopping list?(Yes/No): ')
            else:
                break
    def price_menu():
        print('{:^85s}' .format('---Cafe Menu---'))
        print('{:25s}|{:^20s}|{:^20s}|{:^20s}'.format('Item', 'Price Exclusive GST', 'GST 7%', 'Membership Discount'))
        priceEGST.sort()
        cafe_menu1 = ['Stawberry Pudding', 'Earl Grey', 'Iced Coffee', 'Latte', 'Brownie Gelato', 'Sakura Green Tea', 'Chamomole Peppermint Tea', 'Espresso', 'Chocolate Cheesecake']
        for i in range(len(cafe_menu1)):
            if cafe_menu1[i] == 'Espresso' or cafe_menu1[i] == 'Sakura Green Tea' or cafe_menu1[i] == 'Brownie Gelato' or cafe_menu1[i] == 'Chocolate Cheesecake':
                membership_discount = 'Yes'
            else:
                membership_discount = 'No'
            print('{:25s}|{:^20.2f}|{:^20.2f}|{:^20s}' .format(cafe_menu1[i], priceEGST[i], priceEGST[i]*0.07, membership_discount))
        con = input('\nWould you like to continue adding item in the Shopping list?(Yes/No): ')
        while True:
            if con == 'Yes':
                item = input('Please enter the item you wish to add in to the shopping list: ')
                shopping_list.append(item)
                quan = int(input('How many of %s would you like to buy?: ' % (item)))
                quantity_list.append(quan)
                print('%2.0f of %s has been added to the shopping list.' % (quan, item))
                con = input('Would you like to continue adding item in the Shopping list?(Yes/No): ')
            else:
                break
    def normal_menu():
        print('{:^85s}' .format('---Cafe Menu---'))
        print('{:25s}|{:^20s}|{:^20s}|{:^20s}'.format('Item', 'Price Exclusive GST', 'GST 7%', 'Membership Discount'))
        for i in range(len(cafe_menu)):
            if cafe_menu[i] == 'Espresso' or cafe_menu[i] == 'Sakura Green Tea' or cafe_menu[i] == 'Brownie Gelato' or cafe_menu[i] == 'Chocolate Cheesecake':
                membership_discount = 'Yes'
            else:
                membership_discount = 'No'
            print('{:25s}|{:^20.2f}|{:^20.2f}|{:^20s}' .format(cafe_menu[i], priceEGST[i], priceEGST[i]*0.07, membership_discount))
        con = input('\nWould you like to continue adding item in the Shopping list?(Yes/No): ')
        while True:
            if con == 'Yes':
                item = input('Please enter the item you wish to add in to the shopping list: ')
                shopping_list.append(item)
                quan = int(input('How many of %s would you like to buy?: ' % (item)))
                quantity_list.append(quan)
                print('%2.0f of %s has been added to the shopping list.' % (quan, item))
                con = input('Would you like to continue adding item in the Shopping list?(Yes/No): ')
            else:
                break
    sort_menu()

def previewItem():
    print(shopping_list)

def removeItem():
    item = input('Please enter the item you wish to remove from the shopping list: ')
    shopping_list.remove(item)
    print(item + ' has been removed from the shopping list.')

mainMenu()
