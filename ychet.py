import csv  
f = open("tablica.csv", "w", encoding="utf-8", newline="")
w = csv.writer(f)
w.writerow(["Товар", "Цена за штуку", "Количество"])
w.writerow(["Тетрадь", "2.50", "4"])
w.writerow(["Ручка", "1.20", "3"])
w.writerow(["Папка", "4.00", "2"])
w.writerow(["Маркер", "3.30", "1"])
f.close()
f = open("tablica.csv", "r", encoding="utf-8", newline="")
r = csv.reader(f)
next(r)
s = 0
for a in r:
    n = a[0]
    p = float(a[1])
    k = int(a[2])
    c = p * k
    print(n, "цена:", p, "количество:", k, "стоимость:", c)
    s = s + c
f.close()
print("Общая сумма:", s)