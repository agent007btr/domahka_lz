import json  # встроенный модуль для json

# 1. Создаем профиль
p = {
    "Имя": "Алексей",
    "Группа": "КБ-101",
    "Навыки": ["Python", "Excel"],
    "Уведомления": True
}

# 2. Сохраняем в файл
f = open("participant.json", "w", encoding="utf-8")
# записываем в читаемом виде с русскими буквами
json.dump(p, f, ensure_ascii=False, indent=2)
f.close()

# 3. Читаем обратно
f = open("participant.json", "r", encoding="utf-8")
p = json.load(f)
f.close()

# 4. Меняем данные
# добавляем навык CSV
p["Навыки"].append("CSV")
# отключаем уведомления
p["Уведомления"] = False

# 5. Сохраняем обновленный профиль
f = open("participant.json", "w", encoding="utf-8")
json.dump(p, f, ensure_ascii=False, indent=2)
f.close()

# читаем его снова
f = open("participant.json", "r", encoding="utf-8")
p = json.load(f)
f.close()

# выводим все сведения
print("Имя:", p["Имя"])
print("Группа:", p["Группа"])
print("Навыки:", p["Навыки"])
print("Уведомления:", p["Уведомления"])