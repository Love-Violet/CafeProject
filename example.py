table1 = {
    'Espresso': ['Description', 5.89, 'Yes'],
    'Iced Coffee': ['Description', 5.3, 'No'],
    'Latte': ['Description', 5.3, 'No'],
    'Earl Grey': ['Description', 4.82, 'No'],
    'Sakura Green Tea': ['Description', 5.35, 'Yes'],
    'Chamomile Peppermint Tea': ['Description', 5.35, 'No'],
    'Brownie Gelato': ['Description', 5.25, 'Yes'],
    'Strawberry Pudding': ['Description', 4.55, 'No'],
    'Chocolate Cheesecake': ['Description', 6.31, 'Yes']

}


#for i in range(3):
 #   print('{:^25s}|{:25s}|{:^20s}|{:^20s}'.format('Item', 'Description', 'Price', 'Membership Discount'))
  #  temp = []
  #  temp.append(table1.get('Espresso'))
   # key, value = list(table1.items())[0]
    #print('{:^25s}|{:25s}|{:^20.2f}|{:^20s}'.format((key, temp[0], temp[1], temp[2])))

for x, y in table1.items():
    #print('{:^25s}|{:25s}|{:^20s}|{:^20s}'.format('Item', 'Description', 'Price', 'Membership Discount'))
    temp = []
    temp.append(y)
    print(y)
    for i in range(len(temp)):
        print(i)
    #print('{:^25}|'.format(x))



print(s, '-', i, '\nPrice without GST: $', table1_outcome[0], ' ' * 5, 'Price with GST: $', table1_outcome[1], ' ' * 5, 'Membership Discount:', table1_outcome[2])




print('{:^20s}|{:25s}|{:^20s}|{:^20s}'.format('Item', 'Description', 'Price', 'Membership Discount'))
        temp = []
        temp.append(table1.get('Espresso'))
        print('{:^20s}|{:25s}|{:^20s}|{:^20s}'.format('Espresso', table1.get('Espresso',)))
