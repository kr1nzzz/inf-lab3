# Author = Kozlov Timofey Alekseevich
# Group = P3111
# Date = 23.10.2025

import re

tests = [
    "весенний вечер/лист шуршит в тишине/луна на воде",
    "тихий вечер/ветер в кронах поет/ночь наступает",
    "весенний вечер/луна на воде",
    "ветер в поле/пахнет дождем/идет буря/ночь наступает",
    "  осенний вечер /  листья падают с клена  /  тишина вокруг  "
]

for i, haiku in enumerate(tests, start=1):
    print(f"Тест {i}: {haiku}")
    
    sp = [p.strip() for p in haiku.split('/')]
    
    if len(sp) != 3:
        print("Не хайку. Должно быть 3 строки.\n")
    else:
        glbuk = r"[аеёиоуыэюяАЕЁИОУЫЭЮЯ]"
        kolbuk = [len(re.findall(glbuk, line)) for line in sp]
        
        if kolbuk == [5, 7, 5]:
            print("Хайку!\n")
        else:
            print("Не хайку.\n")

