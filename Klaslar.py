  # 1
# class User:
#     def __init__(self, username, full_name, email):
#         self.username = username
#         self.full_name = full_name
#         self.email = email
#
#     def get_info(self):
#         return f"Foydalanuvchi: {self.username}, ismi: {self.full_name}, email: {self.email}"
#
# user1 = User("alijon1994", "Alijon Valiyev", "alijon1994@gmail.com")
# user2 = User("dilnoza_01", "Dilnoza Karimova", "dilnoza01@mail.com")
# print(user1.get_info())
# print(user2.get_info())
#
#

#   # 2
# class Avto:
#     def __init__(self, model, yil, yurgan_km, narx):
#         self.model = model
#         self.yil = yil
#         self.yurgan_km = yurgan_km
#         self.narx = narx
#
#     def info(self):
#         return (f"Model: {self.model}\n"
#                 f"Yil: {self.yil}\n"
#                 f"Yurgan masofa: {self.yurgan_km} km\n"
#                 f"Narx: ${self.narx}\n")
#
#     def yurish(self, km):
#         if km < 0:
#             return "Km manfiy bo‘lishi mumkin emas!"
#         else:
#             self.yurgan_km += km
#             return "Mashina yurgan km yangilandi."
#
#     def chegirma(self, foiz):
#         if foiz < 0:
#             return "Chegirma foizi manfiy bo‘lishi mumkin emas!"
#         self.narx -= (self.narx * foiz / 100)
#         return "Narx  qaytadan yangilandi."
#
#
# # Obyektlar
# nexia = Avto("Nexia", 2010, 150000, 6000)
# malibu = Avto("Malibu", 2020, 45000, 18000)
# tracker = Avto("Tracker", 2022, 20000, 25000)
#
# print(nexia.chegirma(-45))
# print(malibu.yurish(500))
# print(tracker.yurish(150))
#
# print(nexia.info())
# print(malibu.info())
# print(tracker.info())
#
# print("Yangilangan ma'lumotlar")
# print(nexia.info())
# print(malibu.info())
# print(tracker.info())







