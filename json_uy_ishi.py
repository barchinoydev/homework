# import json
#
# data = {
#     "Model": "Malibu",
#     "Rang": "Qora",
#     "Yil": 2020,
#     "Narh": 40000
# }
# json_data = json.dumps(data, indent=4)
# print(json_data)

# import json
#
# # data obyektini yaratish
# data = {
#     "Model": "Malibu",
#     "Rang": "Qora",
#     "Yil": 2020,
#     "Narh": 40000
# }
#
# # JSON matnidan talaba yaratish
# talaba_json = """
# {"ism":"Hasan","familiya":"Husanov","tyil":2000}
# """
#
# talaba = json.loads(talaba_json)
#
# print("Ism:", talaba["ism"])
# print("Familiya:", talaba["familiya"])
#
# # mashina.json ga yozish
# with open("mashina.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# # talaba.json ga yozish
# with open("talaba.json", "w") as f:
#     json.dump(talaba, f, indent=4)
#
# # talabalar ro'yxatini yaratish
# talabalar_data = [
#     {"ism": "Ali", "familiya": "Valiyev", "kurs": 1, "fakultet": "IT"},
#     {"ism": "Olim", "familiya": "Karimov", "kurs": 2, "fakultet": "Iqtisod"},
#     {"ism": "Malika", "familiya": "Xolmatova", "kurs": 3, "fakultet": "Filologiya"}
# ]
#
# # talabalar.json ga yozish
# with open("talabalar.json", "w") as f:
#     json.dump(talabalar_data, f, indent=4)
#
# # talabalar.json dan o'qish
# with open("talabalar.json") as f:
#     talabalar = json.load(f)
#
# # chiqarish
# for t in talabalar:
#     print(f"{t['ism']} {t['familiya']}, {t['kurs']}-kurs, {t['fakultet']} fakulteti talabasi")

