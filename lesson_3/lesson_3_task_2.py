from smartphone import Smartphone

catalog = []

mobil1 = Smartphone('apple','iphone14','+7 985 644 76 76')
mobil2 = Smartphone('samsung','s10','+7 911 657 08 08')
mobil3 = Smartphone('realme','10pro','+7 933 678 09 23')
mobil4 = Smartphone('xiaomi','redmi','+7 945 678 01 01')
mobil5 = Smartphone('honor','8x','+7 980 045 34 21')

catalog.append(mobil1)
catalog.append(mobil2)
catalog.append(mobil3)
catalog.append(mobil4)
catalog.append(mobil5)

for mobil in catalog:
    print("марка -", mobil.brand, "модель -", mobil.model,"телефон -", mobil.number)