# # 1-Foydalanuvchi ma’lumotlarini lug‘at ko‘rinishida qaytaruvchi funksiya
# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon, yosh=None):
#     return {
#         "ism": ism,
#         "familiya": familiya,
#         "tugilgan_yil": tugilgan_yil,
#         "tugilgan_joy": tugilgan_joy,
#         "email": email,
#         "telefon": telefon,
#         "yosh": yosh
#     }
# foydalanuvchi = foydalanuvchi_malumotlari("Barchinoy","Jumyozova",2012,"Xonqa tumani, Qoraqosh qishlog'i","barchinoyjumyozova@gmail.com",937421140,12)
# print(foydalanuvchi)



# 2-topshiriq — while yordamida bir nechta foydalanuvchi yaratish
# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon):
#     return {
#         "ism": ism,
#         "familiya": familiya,
#         "tugilgan_yil": tugilgan_yil,
#         "tugilgan_joy": tugilgan_joy,
#         "email": email,
#         "telefon": telefon,
#     }
#
# mijozlar = []
#
# while True:
#     print("\n Mijoz qo‘shish")
#
#     ism = input("Ism: ")
#     familiya = input("Familiya: ")
#     yil = int(input("Tug‘ilgan yil: "))
#     joy = input("Tug‘ilgan joy: ")
#     email = input("Email: ")
#     tel = input("Telefon: ")
#
#     mijozlar.append(foydalanuvchi_malumotlari(ism, familiya, yil, joy, email, tel))
#
#     davom = input("Yana mijoz qo‘shasizmi? (ha/yo‘q): ").lower()
#
#     if davom in ["yoq", "yo'q", "yo‘q", "yo’q", "no"]:
#         print("Dastur to‘xtatildi.")
#         break
#     else:
#         print("Davom etamiz...\n")
#
# print("\n Mijozlar ro‘yxati:")
# for m in mijozlar:
#     print(m)

# 3
# def eng_katta(a, b, c):
#     return max(a, b, c)
# print(eng_katta(1, 5, 9))


# 4
# def aylana(radius):
#     natija = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * 3.14 * radius,
#         "yuza": 3.14 * radius**2
#     }
#     return natija
#
# print(aylana(7))

 # 6
# def fibonachchi(n):
#     ketma_ketlik = [1, 1]
#     while len(ketma_ketlik) < n:
#         ketma_ketlik.append(ketma_ketlik[-1] + ketma_ketlik[-2])
#     return ketma_ketlik[:n]
# print(fibonachchi(50))