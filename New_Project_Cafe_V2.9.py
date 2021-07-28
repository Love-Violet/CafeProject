import sys
import webbrowser
import time
import string
import random


class formatting:
    bold = '\033[1m'
    italic = '\033[3m'
    underline = '\033[4m'
    end = '\033[0m'
    header = '\033[1m'+'\033[4m'


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
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Dan Cafe---')+formatting.end+formatting.header+'\n\nSelect a number for the action that you would like to do:'+formatting.end+'\n 1. Cafe Menu\n 2. Add to cart\n 3. Remove from cart\n 4. View cart\n 5. Check-Out\n 6. Advertisement\n 9. Exit')
    selector = {
        '1': cafe_menu,
        '2': add_item,
        '3': remove_item,
        '4': view_item,
        '5': checkout,
        '6': advertisement,
        '9': sys.exit
    }
    option = (input(formatting.italic+'\n> Make your selection: '+formatting.end))
    try:
        selector[option]()
    except KeyError:
        main()
    main()


def cafe_menu():
    cafe_menu_default()
    cont()
    print('\n'*10+formatting.header+'Select a number for the action that you would like to do:'+formatting.end+'\n 1. Sort\n 2. Add to cart\n 3. Remove from cart\n 4. View cart\n 5. Checkout\n 9. Main Menu')
    confirm = input(formatting.italic+'\n> Make your selection: '+formatting.end+formatting.end)
    if confirm == '1':
        print('\n'*10+formatting.header+'Sort by?'+formatting.end)
        print(' 1. Category\n 2. Alphabetically\n 3. Lowest Price\n 4. Highest Price')
        global optionCafeMenu
        selector = {
            '1': category_menu,
            '2': alphabetically_menu,
            '3': order_price,
            '4': order_price
        }
        optionCafeMenu = (input(formatting.italic+'\n> Make your selection: '+formatting.end))
        try:
            selector[optionCafeMenu]()
        except KeyError:
            cafe_menu()
    elif confirm == '2':
        add_item()
    elif confirm == '3':
        remove_item()
    elif confirm == '4':
        view_item()
    elif confirm == '5':
        checkout()
    else:
        main()
    cafe_menu()


def cafe_menu_default():
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Cafe Menu---')+formatting.end)
    header()
    global i
    for i in table2:
        outcome_table2()


def alphabetically_menu():
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Cafe Menu---')+formatting.end)
    header()
    sorted_name = sorted(table2.keys(), key=lambda x: x.lower())
    global i
    for i in sorted_name:
        outcome_table2()
    cont()
    option_menu1()


def category_menu():
    print('\n'*10+formatting.header+'Which category did you want?'+formatting.end+'\n 1. Coffee\n 2. Tea\n 3. Dessert\n 4. Add to cart\n 5. Remove from cart\n 6. View Cart\n 7. Checkout\n 8. Cafe Menu\n 9. Main Menu')
    option = input(formatting.italic+'\n> Make your selection: '+formatting.end)
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Cafe Menu---')+formatting.end)
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
    elif option == '4':
        add_item()
    elif option == '5':
        remove_item()
    elif option == '8':
        cafe_menu()
    elif option == '9':
        main()
    elif option == '6':
        view_item()
    elif option == '7':
        checkout()
    else:
        category_menu()
    cont()
    category_menu()


def order_price():
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Cafe Menu---')+formatting.end)
    header()
    if optionCafeMenu == '3':
        table1.sort(key=lambda x: x[1], reverse=False)
    elif optionCafeMenu == '4':
        table1.sort(key=lambda x: x[1], reverse=True)
    for ap in table1:
        print('| {:12s}| {:<28s}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(ap[4], ap[0], ap[1], ap[2], ap[3]))
    cont()
    option_menu1()


def header():
    print(formatting.header+'| Category    | Item                        | Price Exclusive GST | Price Inclusive GST(7%)| Membership Discount(15%)|'+formatting.end)


def outcome_table2():
    table2_outcome = table2.get(i, ['', '', '', ''])
    print('| {:12s}| {:<28s}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(table2_outcome[3], i, table2_outcome[0], table2_outcome[1], table2_outcome[2]))


def option_menu1():
    print('\n'*10+formatting.header+'Select a number for the action that you would like to do:'+formatting.end+'\n 1. Add to cart\n 2. Remove from cart\n 3. View cart\n 4. Checkout\n 8. Cafe Menu\n 9. Main Menu')
    selector = {
        '1': add_item,
        '2': remove_item,
        '3': view_item,
        '4': checkout,
        '8': cafe_menu,
        '9': main
    }
    option = (input(formatting.italic+'\n> Make your selection: '+formatting.end))
    try:
        selector[option]()
    except KeyError:
        option_menu1()


def add_item():
    while True:
        cafe_menu_default()
        input_item = input(formatting.italic+'\n> Enter Item Name (Case Sensitive)(Press enter to return): '+formatting.end)
        if input_item == '':
            break
        try:
            item_quantity = int(input(formatting.italic+'> Enter Quantity: '+formatting.end))
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
                print('Invalid Item')
                time.sleep(2)
                add_item()
        except ValueError:
            print('Invalid Quantity')
            time.sleep(2)
            add_item()
        continue_adding = input(formatting.italic+'\n> Add more items? '+formatting.end)
        if continue_adding == 'Yes' or continue_adding == 'yes' or continue_adding == 'Y' or continue_adding == 'y':
            continue
        else:
            break


def remove_item():
    while True:
        view_item()
        item_remove = input(formatting.italic+'\n> Enter item name (Case Sensitive)(Press enter to return): '+formatting.end)
        if item_remove == '':
            break
        try:
            remove_quantity = int(input(formatting.italic+'> Enter Quantity: '+formatting.end))
            if item_remove in shopping_list:
                if remove_quantity >= shopping_list[item_remove]:
                    shopping_list.pop(item_remove)
                else:
                    remove = shopping_list.get(item_remove)
                    remove -= remove_quantity
                    shopping_list[item_remove] = remove
            continue_adding = input(formatting.italic+'\n> Remove more items? '+formatting.end)
            if continue_adding == 'Yes' or continue_adding == 'yes' or continue_adding == 'Y' or continue_adding == 'y':
                continue
            else:
                break
        except ValueError:
            print('Invalid Quantity')
            time.sleep(2)
            remove_item()


def view_item():
    print('\n'*10+formatting.bold+'{:^85s}' .format('---Shopping List---')+formatting.end)
    print(formatting.header+'| Item                        | Quantity      | Price Exclusive GST | Price Inclusive GST(7%)| Membership Discount(15%)|'+formatting.end)
    for view in shopping_list:
        for second in table2:
            if view == second:
                table2_outcome = table2.get(second, ['', '', '', ''])
                print('| {:28s}| {:<14.0f}| ${:<19.2f}| ${:<22.2f}| {:<24s}|'. format(view, shopping_list.get(view), (shopping_list.get(view) * table2_outcome[0]), (shopping_list.get(view) * table2_outcome[1]), table2_outcome[2]))
            else:
                continue
    cont()


def checkout():
    while True:
        global price_before
        global member
        global promo_availability
        price_before = 0
        print('\n'*15+formatting.bold+'{:^85s}' .format('---Check-out---')+formatting.end)
        member = input(formatting.italic+"> Are you a member?: "+formatting.end)
        if member == 'return':
            main()
        elif member == 'n' or member == 'N' or member == 'No' or member == 'no':
            while True:
                promo_availability = input(formatting.italic+'> Enter the promo code: '+formatting.end)
                if promo_availability == '$1 off' or promo_availability == 'Bonus Discount' or promo_availability == '':
                    break
                else:
                    print('You have enter wrongly')
        elif member == 'y' or member == 'Y' or member == 'Yes' or member == 'yes':
            pass
        else:
            print('You did not make a valid selection. Please try again')
            checkout()
        print('\n'*15+formatting.bold+'{:^85s}' .format('---Cart---')+formatting.end)
        print(formatting.header+'| Item                                        | Quantity      | Price      |'+formatting.end)
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
        cont()
        while True:
            payment = input(formatting.header+'\nSelect a number for the action that you would like to do:'+formatting.end+'\n 1. Add items / Add quantity\n 2. Remove items / Subtract quantity\n 3. Pay by Cash\n 4. Pay by Card\n 9. Return to main menu'+formatting.italic+'\n\n> Make your selection: '+formatting.end)
            if payment == '3':
                print('\n' * 20)
                checkout_format()
                print('| {:>60s}| {:<11s}|\nPlease visit the nearest store near you and show this receipt to the cashier' . format('', 'CASH'))
                bonus()
                cont()
                main()
            elif payment == '4':
                print('\n' * 20)
                checkout_format()
                print('| {:>60s}| {:<11s}|' . format('', 'CARD'))
                bonus()
                cont()
                print('\n' * 20)
                card_selection()
                cont()
                main()
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
    print('\n'*15+formatting.bold+'{:^85s}' .format('---Receipt---')+formatting.end)
    rg()
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
    global total_discount_price, discount_name
    if member == 'y' or member == 'Y' or member == 'Yes' or member == 'yes':
        total_discount_price = member_discount()
        discount_name = 'Member'
    elif member == 'n' or member == 'N' or member == 'No' or member == 'no':
        total_discount_price = promo_discount()
        discount_name = 'Promo'
    print('| {:>60s}| ${:<10.2f}|'. format(discount_name+' discount', total_discount_price))


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
    price_no_gst = price_before - total_discount_price
    if price_no_gst < 0:
        price_no_gst = 0
    print('| {:>60s}| ${:<10.2f}|'. format('Total Price(w/o GST)', price_no_gst))
    global gst_7
    global gst_107
    gst_7 = (price_before - total_discount_price) * 0.07
    if gst_7 < 0:
        gst_7 = 0
    print('| {:>60s}| ${:<10.2f}|'. format('GST', gst_7))
    gst_107 = (price_before - total_discount_price) * 1.07
    if gst_107 < 0:
        gst_107 = 0
    print('| {:>60s}| ${:<10.2f}|'. format('Total Price', gst_107))


def advertisement():
    print('\n'*10+'{:^85s}\n Promo code(non - member)*: $1 off\n\n Please copy the code after : and paste it when on check out\n free $5 off promo code if your final balance in the receipt is $50 or more*\n\n\n* promo code only applicable to redeem as a non member' .format('---Advertisement---'))
    time.sleep(5)


def cont():
    input(formatting.italic+'\n> Do you want to continue? '+formatting.end+formatting.end)


def card_selection():
    print(formatting.header+'\nSelect a number for the action that you would like to do:'+formatting.end+'\n 1. Paypal\n 2. Visa\n 3. MasterCard\n 4. American Express\n 5. Union Pay')
    card_select = input(formatting.italic+'\n> Make your selection: '+formatting.end)
    if card_select == '1':
        webbrowser.open_new('https://www.paypal.com/')
    elif card_select == '2':
        webbrowser.open_new('https://www.visa.com.sg/pay-with-visa/click-to-pay-with-visa.html')
    elif card_select == '3':
        webbrowser.open_new('https://www.mastercard.com.sg/en-sg/personal/ways-to-pay/click-to-pay.html')
    elif card_select == '4':
        webbrowser.open_new('https://www.americanexpress.com/us/help/make-a-payment.html')
    elif card_select == '5':
        webbrowser.open_new('https://www.unionpayintl.com/en/servicesProducts/products/innovativeProducts/onlinePayment/')


def rg():
    ran = range(0, 10)
    up_letter = random.choice(string.ascii_uppercase)
    rng = random.sample(ran, k=7)
    print('{:>64}{}{}{}{}{}{}{}{}'. format('Number: ', rng[0], rng[1], rng[2], rng[3], rng[4], rng[5], rng[6], up_letter))


main()
