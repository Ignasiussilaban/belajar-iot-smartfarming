suhu_pagi = float(input("suhu pagi (c): "))
suhu_siang = float(input("suhu siang (c): "))
suhu_sore = float(input("suhu sore (c): "))
rata_rata = (suhu_pagi + suhu_siang + suhu_sore) / 3
print("Rata-rata Suhu =", rata_rata, "c")