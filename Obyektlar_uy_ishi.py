   # ***1***
# class Product:
#     def __init__(self, id, nomi, narxi, soni , rating):
#         self.id = id
#         self.nomi = nomi
#         self.narx = narxi
#         self.soni = soni
#         self.rating = rating
#
#     # Mahsulot ma'lumotlarini chiqarish
#     def Mahsulot_malumotlarini_chiqarish(self):
#         print(f"Mahsulot ID: {self.id}")
#         print(f"Nomi: {self.nomi}")
#         print(f"Narxi: {self.narx} so'm")
#         print(f"Ombordagi soni: {self.soni}")
#         print(f"Reyting: {self.rating}")
#
#     # Mahsulot narxini yangilash
#     def narxni_yangilash(self, yangi_narx):
#         if yangi_narx >= 0:
#             self.narx = yangi_narx
#             print(f"{self.nomi} mahsulotining narxi yangilandi: {self.narx} so'm")
#         else:
#             print("Narx manfiy bo'lishi mumkin emas!")
#
# # Misol uchun mahsulot yaratish va metodlardan foydalanish
# product1 = Product(1, "Asal qo'shilgan choy", 15000, 50, 4)
# product1.Mahsulot_malumotlarini_chiqarish()
# print("\nNarxni yangilandi")
# product1.narxni_yangilash(-17000)
# product1.Mahsulot_malumotlarini_chiqarish()

 # ***2***
#
# class Cart:
#     def __init__(self):
#         self.mahsulotlar = []
#         self.umumiy_narx = 0.0
#
#     def mahsulot_qoshish(self, mahsulot_nomi, narx, miqdor=1):
#         """Mahsulot qo'shish"""
#         self.mahsulotlar.append({'nomi': mahsulot_nomi, 'narx': narx, 'miqdor': miqdor})
#         self.umumiy_narx_hisobla()
#
#     def mahsulot_olib_tashlash(self, mahsulot_nomi):
#         """Mahsulot olib tashlash (nom bo'yicha)"""
#         self.mahsulotlar = [m for m in self.mahsulotlar if m['nomi'] != mahsulot_nomi]
#         self.umumiy_narx_hisobla()
#
#     def savat_tozalash(self):
#         """Savatni tozalash"""
#         self.mahsulotlar = []
#         self.umumiy_narx = 0.0
#
#     def umumiy_narx_hisobla(self):
#         """Savatdagi umumiy narxni hisoblash"""
#         self.umumiy_narx = sum(m['narx'] * m['miqdor'] for m in self.mahsulotlar)
#
#     def boshmi(self):
#         """Savat bo'sh yoki bo'sh emasligini tekshirish"""
#         return len(self.mahsulotlar) == 0
#
#     def __str__(self):
#         if self.boshmi():
#             return "Savat bo'sh"
#         else:
#             return f"Savatdagi mahsulotlar: {self.mahsulotlar}\nUmumiy narx: {self.umumiy_narx}"
# savat = Cart()
# savat.mahsulot_qoshish("Anor", 7000, 4)
# savat.mahsulot_qoshish("Olma", 4000, 3)
# savat.mahsulot_qoshish("Banan", 7500, 2)
# print(savat)
#
# savat.mahsulot_olib_tashlash("Olma")
# print(savat)
#
# savat.savat_tozalash()
# print(savat.boshmi())

  # ***3***
# class Order:
#     def __init__(self, id, savat):
#         self.id = id
#         self.status = "yaratilgan"
#         self.savat = savat
#         self.yaratilgan_vaqti = "Allaqachon yaratilgan"
#         self.jami_narx = sum(item['narx'] for item in self.savat)
#
#     def tasdiqlash(self):
#         """Buyurtma statusini tasdiqlash"""
#         self.status = "tasdiqlangan"
#
#     def status_yangilash(self, yangi_status):
#         """Buyurtma statusini yangilash"""
#         self.status = yangi_status
#
#     def malumotlarini_korsatish(self):
#         """Buyurtma ma’lumotlarini chiqarish"""
#         print(f"Buyurtma ID: {self.id}")
#         print(f"Status: {self.status}")
#         print(f"Yaratilgan vaqti: {self.yaratilgan_vaqti}")
#         print("Savatdagi mahsulotlar:")
#         for item in self.savat:
#             print(f" -{item['nomi']}: {item['narx']} so'm")
#         print(f"Jami narx: {self.jami_narx} so'm")
#
#
# # Misol ishlatish:
# savat = [{'nomi': 'Pizza', 'narx': 35000}, {'nomi': 'KFC', 'narx': 10000}, {'nomi': 'Pepsi', 'narx':5000}]
# buyurtma1 = Order(1, savat)
# buyurtma1.tasdiqlash()
# buyurtma1.status_yangilash("yetkazib berilmoqda")
# buyurtma1.malumotlarini_korsatish()

  # ***5***
# class Mahsulot:
#     def __init__(self, nom, narx, rating, sotilgan_soni=0):
#         self.nom = nom
#         self.narx = narx
#         self.rating = rating
#         self.sotilgan_soni = sotilgan_soni
#
# # Foydalanuvchi klassi
# class Foydalanuvchi:
#     def __init__(self, ism, email):
#         self.ism = ism
#         self.email = email
#
# # Do'kon klassi
# class Store:
#     def __init__(self, nom):
#         self.nomi = nom
#         self.mahsulotlar = []
#         self.foydalanuvchilar = []
#
#     def mahsulot_qoshish(self, mahsulot):
#         self.mahsulotlar.append(mahsulot)
#
#     def foydalanuvchi_qoshish(self, foydalanuvchi):
#         self.foydalanuvchilar.append(foydalanuvchi)
#
#     def mahsulot_qidirish(self, nom):
#         natija = []
#         for mahsulot in self.mahsulotlar:
#             if nom.lower() in mahsulot.nom.lower():
#                 natija.append(mahsulot)
#         return natija
#
#     def eng_yaxshi_rating(self):
#         if len(self.mahsulotlar) == 0:
#             return []
#         max_rating = self.mahsulotlar[0].rating
#         for mahsulot in self.mahsulotlar:
#             if mahsulot.rating > max_rating:
#                 max_rating = mahsulot.rating
#         natija = []
#         for mahsulot in self.mahsulotlar:
#             if mahsulot.rating == max_rating:
#                 natija.append(mahsulot)
#         return natija
#
#     def sotilgan_hisobot(self):
#         hisobot = []
#         for mahsulot in self.mahsulotlar:
#             if mahsulot.sotilgan_soni > 0:
#                 hisobot.append(f"{mahsulot.nom}: {mahsulot.sotilgan_soni} ta sotilgan")
#         return hisobot
#
#
# # Do'kon yaratish
# dok = Store("Telefon Do'koni")
#
# # Mahsulotlar
# mahsulot1 = Mahsulot("Laptop", 1200, 2, 10)
# mahsulot2 = Mahsulot("Telefon", 3000, 3, 5)
# mahsulot3 = Mahsulot("Planshet", 5000, 3, 9)
#
# dok.mahsulot_qoshish(mahsulot1)
# dok.mahsulot_qoshish(mahsulot2)
# dok.mahsulot_qoshish(mahsulot3)
#
# # Foydalanuvchilar
# foydalanuvchi1 = Foydalanuvchi("Ali", "ali@mail.com")
# foydalanuvchi2 = Foydalanuvchi("Barno", "barno@mail.com")
#
# dok.foydalanuvchi_qoshish(foydalanuvchi1)
# dok.foydalanuvchi_qoshish(foydalanuvchi2)
#
# # Mahsulot qidirish
# qidiruv_natija = dok.mahsulot_qidirish("Planshet")
# for mahsulot in qidiruv_natija:
#     print(f"{mahsulot.nom} narxi {mahsulot.narx} so'm, reyting {mahsulot.rating}")
#
# # Eng yaxshi ratingli mahsulotlar
# eng_yaxshi_mahsulotlar = dok.eng_yaxshi_rating()
# for mahsulot in eng_yaxshi_mahsulotlar:
#     print(f"Eng yaxshi sotigan  {mahsulot.nom}, reyting {mahsulot.rating}")
#
# # Sotilgan mahsulotlar hisoboti
# hisobot = dok.sotilgan_hisobot()
# for hisobot_satr in hisobot:
#     print(hisobot_satr)