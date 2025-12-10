# import datetime as dt


# bugun = dt.date.today()
#
# print("Bugungi kundan boshlab 2 hafta farq bilan 10 ta sana:")
#
# for i in range(10):
#     sana = bugun + dt.timedelta(weeks=2*i)
#     print(sana)

   # 2
# bugun = dt.date.today()
#
# ramazon = dt.date(2026, 2, 18)
# qurbon = dt.date(2026, 6, 6)
#
# farq_ramazon = ramazon - bugun
# farq_qurbon = qurbon - bugun
#
# print(f"Ramazonga {farq_ramazon.days} kun qoldi")
# print(f"Qurbon hayitiga {farq_qurbon.days} kun qoldi")

  # 3

#
# bugun = dt.date(2025, 12, 10)
# tugilgan = dt.date(2025, 5, 5)
#
# yil = bugun.year - tugilgan.year
# oy = bugun.month - tugilgan.month
# kun = bugun.day - tugilgan.day
#
# if kun < 0:
#     oy -= 1
#     oldingi_oy_kunlari = (bugun.replace(day=1) - dt.timedelta(days=1)).day
#     kun += oldingi_oy_kunlari
#
# if oy < 0:
#     yil -= 1
#     oy += 12
#
# print(f"Tug'ilgan kunimdan {yil} yil, {oy} oy,va  {kun} kun o'tdi")
#

#
# bugun = dt.date(2025, 12, 10)
# tugilgan = dt.date(2026, 5, 5)
#
# yil = tugilgan.year - bugun.year
# oy = tugilgan.month - bugun.month
# kun = tugilgan.day - bugun.day
#
# if kun < 0:
#     oy -= 1
#     oldingi_oy_kunlari = (tugilgan.replace(day=1) - dt.timedelta(days=1)).day
#     kun += oldingi_oy_kunlari
#
# if oy < 0:
#     yil -= 1
#     oy += 12
#
# print(f"Tug'ilgan kunimga {yil} yil, {oy} oy, {kun} kun qoldi")

  # 4


# import re
# 
# raqam1 = "+998901234567"
# raqam2 = "+998991112233"
# raqam3 = "123456789"
#
# # Telefon raqam uchun andoza
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# #
#
# # Tekshirish
# print(re.match(andoza, raqam1))  # mos kelsa match object qaytaradi
# print(re.match(andoza, raqam2))  # mos kelsa match object qaytaradi
# print(re.match(andoza, raqam3))  # mos kelmasa None qaytaradi


#     # 5
# import re
#
# # Matn ichida bir nechta URL
# matn = """Maqolalar  2025-yilning 20-martiga qadar barchinoyjumyozova@gmail.com  https://www.youtube.com ,  https://youtube.com elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
#
#
# # URL uchun andoza
# andoza = r"https?://[^\s]+"
# url = re.findall(andoza, matn)
#
# print("Matndagi url(lar):", url)
