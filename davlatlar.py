# davlatlar = {
#         "ozbekiston":{
#             "poytaxti": "Toshkent",
#             "hududi": 448978 ,
#             "aholisi": 300000000,
#             "pul birligi": "som"
#             },
#
#         "Rossiya":{
#             "poytaxti": "moskva",
#             "hududi":1244556 ,
#             "aholisi":37000000,
#             "pul birligi": "dollar"
#             },

#         "Malaziya": {
#             "poytaxti": "Kuala-lampur",
#             "hududi": 329750,
#             "aholisi": 25000000,
#             "pul birligi": "rinngit",
#                 },
#
#         "AQSH":{
#             "poytaxti": "Vashington",
#             "hududi":9631418,
#             "aholisi":3270000,
#             "pul birligi" : "dollar",
#                 },
# }
#
# for davlat_nomi,ma_lumotlar in  davlatlar.items():
#         print(f"\n{davlat_nomi}ning poytaxti: {ma_lumotlar['poytaxti']}")
#         print(f"Hududi: {ma_lumotlar['hududi']}")
#         print(f"Aholisi: {ma_lumotlar['aholisi']}")
#         print(f"Pul birligi: {ma_lumotlar['pul birligi']}")
# #
# user_input = input("Davlat nomini kiriting: ")
# if user_input in davlatlar:
#     info = davlatlar[user_input]
#     print("---- haqida malumot")
#     for key,value in info.items():
#         print(f"{key.capitalize()}:{value}")
# else:
#     print("kechirasz bizda bu davlat haqiada malumot yoq")