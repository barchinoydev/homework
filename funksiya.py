# 1. Foydalanuvchi ismi va yoshidan tug‘ilgan yilni hisoblash
# def tugilgan_yil():
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     yil = 2025 - yosh
#     print(f"{ism}, siz {yil}-yilda tug‘ilgansiz.")
# tugilgan_yil()

# 2. Sonning kvadrati va kubini chiqarish
# def kvadrat_kub():
#     son = float(input("Son kiriting: "))
#     print(f"{son} ning kvadrati = {son**2}")
#     print(f"{son} ning kubi = {son**3}")
# kvadrat_kub()

# 3. Juft yoki toq sonni aniqlash
# def juftmi_toqmi():
#     son = int(input("Son kiriting: "))
#     if son % 2 == 0:
#         print(f"{son} juft son.")
#     else:
#         print(f"{son} toq son.")
# juftmi_toqmi()

# 4. Ikkita sonning kattasini topish
# def katta_son():
#     a = float(input("Birinchi sonni kiriting: "))
#     b = float(input("Ikkinchi sonni kiriting: "))
#     if a > b:
#         print(f"{a} katta son.")
#     elif b > a:
#         print(f"{b} katta son.")
#     else:
#         print("Sonlar teng.")
# katta_son()

# 6. y uchun standart qiymat 2
# def daraja_standart():
#     x = float(input("Son kiriting (x): "))
#     y_input = input("Darajani kiriting (agar bo‘sh qoldirsangiz, 2 bo‘ladi): ")
#     if y_input == "":
#         y = 2
#     else:
#         y = float(y_input)
#
#     natija = x ** y
#     print(f"{x} ning {y}-darajasi = {natija}")
# daraja_standart()

# 7. Sonni 2 dan 10 gacha bo‘lgan sonlarga bo‘linishini tekshirish
# def bolinish_alomatlari(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo‘linadi")
#         else:
#             print(f"{son} {i} ga qoldiqsiz bo‘linmaydi")
# bolinish_alomatlari(8)