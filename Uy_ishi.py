# 1.
# def user_data(first_name, last_name, age):
#     print(f"  Ism: {first_name.title()}")
#     print(f"  Familiya: {last_name.title()}")
#     print(f"  Yosh: {age}")
#
# ism = input("Ismingiz: ")
# familiya = input("Familiyangiz: ")
# yosh = int(input("Yoshingiz: "))
#
# user_data(ism, familiya, yosh)

# 2.
# def find_max(a, b, c):
#     max_num = max(a, b, c)
#
#     katta = []
#     if a == max_num:
#         katta.append("A")
#     if b == max_num:
#         katta.append("B")
#     if c == max_num:
#         katta.append("C")
#
#     print(f"  Eng katta son - {' va '.join(katta)} = {max_num}")
#
#
# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))
#
# find_max(a, b, c)

# 3.
# def find_letter_count(word, letter):
#     count = word.lower().count(letter.lower())
#     print(f'  "{word}" sozida "{letter}" dan {count} ta bor.')
#
#
# word = input("So'z kiriting: ")
# letter = input("Qaysi harfni sanashni xohlaysiz? ")
#
#
# find_letter_count(word, letter)

# 4.
# def list_sum(myList):
#     print(f"  Listning elementlar yig'indisi = {sum(myList)}")
#
# myList = [5, 7, 20]
# list_sum(myList)

# 5.
#
# def daraja(a, b):
#     print(f"  {a} ning {b}-chi darajasi = {a ** b}")
#
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# daraja(a, b)

# 5.
# daraja = lambda a, b: a ** b
# print(daraja(3, 2))


# 6.
# def daraja4(a, b, c, d):
#     print(f"  {a} ning {b}-chi darajasi = {a ** b}")
#     print(f"  {c} ning {d}-chi darajasi = {a ** d}")
#
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# c = int(input("c ni kiriting: "))
# d = int(input("d ni kiriting: "))
#
# daraja4(a, b, c, d)

# 8.
# def add_right(a, b):
#     result = int(f"{a}{b}")
#     print(result)
# a = int(input("a = "))
# b = int(input("b = "))
# add_right(a, b)


#  9.
# def add_left(a, b):
#     result = int(f"{b}{a}")
#     print(result)
# a = int(input("a = "))
# b = int(input("b = "))
# add_left(a, b)

# 11.
# def big_sales(sales):
#     max_month = max(sales, key=sales.get)
#     return max_month
#
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# print("Eng ko'p sotuv bo'lgan oy:", big_sales(sales))

# 12.
# def min_max(numbers, max_num, min_num):
#     max = max_num == max(numbers)
#     min = min_num == min(numbers)
#
#     print(f"{max_num} eng katta son: {max}")
#     print(f"{min_num} eng kichik son: {min}")
# numbers = []
# n = int(input("Nechta son kiritmoqchisiz? "))
# for i in range(n):
#     num = int(input(f"{i + 1}-sonni kiriting: "))
#     numbers.append(num)
# max_num = int(input("Tekshiriladigan eng katta son: "))
# min_num = int(input("Tekshiriladigan eng kichik son: "))
# min_max(numbers, max_num, min_num)

# 13.
# def expensiveProduct(products):
#     max_price_product = max(products, key=lambda x: x['price'])
#     print("Eng qimmat telefon:", max_price_product['name'])
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100},
# ]
# expensiveProduct(products)


