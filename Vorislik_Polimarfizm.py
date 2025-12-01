# class Shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def get_info(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}"
#
#
# #  Fan klass
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
#     def info(self):
#         return self.nomi
#
#
# # Talaba klass
# class Talaba(Shaxs):
#     def __init__(self, ism, yosh):
#         super().__init__(ism, yosh)
#         self.fanlar = []
#
#     def fanga_yozil(self, fan_obj):
#         self.fanlar.append(fan_obj)
#
#     def remove_fan(self, fan_obj):
#         if fan_obj in self.fanlar:
#             self.fanlar.remove(fan_obj)
#             return "Fan o‘chirildi"
#         else:
#             return "Siz bu fanga yozilmagansiz"
#
#     def get_info(self):
#         fanlar_str = ','.join([f.nomi for f in self.fanlar]) if self.fanlar else "Yo‘q"
#         return f"{super().get_info()}, Fanlar: {fanlar_str}"
#
#
# #  Yangi voris klasslar
# class Professor(Shaxs):
#     def __init__(self, ism, yosh, yonalish):
#         super().__init__(ism, yosh)
#         self.kafedra = yonalish
#
#     def get_info(self):
#         return f"{super().get_info()}, Yonalish: {self.kafedra}"
#
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, yosh, login):
#         super().__init__(ism, yosh)
#         self.login = login
#
#     def get_info(self):
#         return f"{super().get_info()}, Login: {self.login}"
#
#
# #  Admin voris klassi
# class Admin(Foydalanuvchi):
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi")
#
#     def get_info(self):
#         return f"[ADMIN] {super().get_info()}"
#
#
# # Sotuvchi
# class Sotuvchi(Shaxs):
#     def __init__(self, ism, yosh, dokon):
#         super().__init__(ism, yosh)
#         self.dokon = dokon
#
#     def get_info(self):
#         return f"{super().get_info()}, Dokon: {self.dokon}"
#
#
# # Mijoz
# class Mijoz(Shaxs):
#     def __init__(self, ism, yosh, balans):
#         super().__init__(ism, yosh)
#         self.balans = balans
#
#     def get_info(self):
#         return f"{super().get_info()}, Balans: {self.balans} so‘m"
#
#
# # Fanlar
# math = Fan("Matematika")
# eng = Fan("Ingliz tili")
#
# # Talaba
# talaba1 = Talaba("Ali", 20)
# talaba1.fanga_yozil(math)
# talaba1.fanga_yozil(eng)
#
# print(talaba1.get_info())         # Fanlar bilan
# print(talaba1.remove_fan(math))
# print(talaba1.get_info())         # Yangilangan fanlar
#
# # Admin
# admin = Admin("Bobur", 30, "admin123")
# print(admin.get_info())
# admin.ban_user()
#
# # Obektlar yaratamiz
# shaxs = Shaxs("Olim", 40)
# fan = Fan("Fizika")
# talaba = Talaba("Ali", 20)
# talaba.fanga_yozil(Fan("Matematika"))
# talaba.fanga_yozil(Fan("Ingliz tili"))
#
# professor = Professor("Karim", 55, "Matematika kafedrasi")
# foydalanuvchi = Foydalanuvchi("Jasur", 25, "jasur25")
# admin = Admin("Bobur", 30, "admin123")
# sotuvchi = Sotuvchi("Sardor", 28, "Mega Market")
# mijoz = Mijoz("Dilshod", 33, 150000)
#
#
# # Barchasidan get_info() chaqiramiz
# print(shaxs.get_info())
# print(talaba.get_info())
# print(professor.get_info())
# print(foydalanuvchi.get_info())
# print(admin.get_info())
# print(sotuvchi.get_info())
# print(mijoz.get_info())