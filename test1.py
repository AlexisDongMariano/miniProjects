# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}
#
# def total_brought(guests, item):
#
#     num_brought = 0
#
#     for k, v in guests.items():
#         print(f'{k}:{v}')
#         num_brought = num_brought + v.get(item, 0)
#     return num_brought
#
# print('Number of things being brought:')
# print(' - Apples ' + str(total_brought(allGuests, 'apples')))
# print(' - Cups ' + str(total_brought(allGuests, 'cups')))
# print(' - Cakes ' + str(total_brought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies ' + str(total_brought(allGuests, 'apple pies')))
# #################################################################################
# PHONE NUMBER FINDER hardcode without using regex
def number_checker(phone_number):
    if len(phone_number) == 12:
        if not phone_number[0:4].isdecimal():
            return False
        if phone_number[4] != '-' and phone_number[9] != '-':
            return False
        if not phone_number[5:9].isdecimal():
            return False
        if not phone_number[10:12].isdecimal():
            return False
        return True
    else:
        return False

def phone_finder(msg_str):
    for i in range(len(msg_str)):
        number = msg_str[i:i+12]
        print(number)
        if number_checker(number):
            print(number)

msg_str = input("Enter a string: ")
phone_finder(msg_str)


