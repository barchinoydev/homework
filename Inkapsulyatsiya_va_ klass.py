# class Shaxs:
#     __odamlar_soni = 0
#
#     def __init__(self, ism, yosh):
#         self.__ism = ism
#         self.__yosh = yosh
#         Shaxs.__odamlar_soni += 1
#
#     def get_ism(self):
#         return self.__ism
#
#     def get_yosh(self):
#         return self.__yosh
#
#     def set_ism(self, yangi_ism):
#         self.__ism = yangi_ism
#
#     def set_yosh(self, yangi_yosh):
#         self.__yosh = yangi_yosh
#
#     def get_info(self):
#         return f"Ism: {self.__ism}, Yosh: {self.__yosh}"
#
#     @classmethod
#     def get_odamlar_soni(cls):
#         return cls.__odamlar_soni
#
#
#
# class Talaba(Shaxs):
#     __talabalar_soni = 0
#
#     def __init__(self, ism, yosh):
#         super().__init__(ism, yosh)
#         Talaba.__talabalar_soni += 1
#
#     @classmethod
#     def get_talabalar_soni(cls):
#         return cls.__talabalar_soni
#
# talaba1=Talaba("Ali", 20)
# talaba2=Talaba("Laylo", 19)
# talaba3=Talaba("Jamshid", 21)
# shaxs1=Shaxs("Olim", 40)
# shaxs2=Shaxs("Ulug'bek", 55)
#
# print(talaba1.get_info())
# print(shaxs1.get_info())
#
# print("Odamlar soni:", Shaxs.get_odamlar_soni())
# print("Talabalar soni:", Talaba.get_talabalar_soni())