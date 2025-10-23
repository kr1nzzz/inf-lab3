import re

def slovechki(text):

    words = re.findall(r'\b\w+\b', text.lower())    
    glbuk = 'аеёиоуыэюя'
    result = []
    for word in words:
        naidbuk = re.findall(f'[{glbuk}]', word)
        if len(set(naidbuk)) == 1 and len(naidbuk) >= 1:
            result.append(word)
    
    result.sort(key=lambda x: (len(x), x))
    
    return result

tests = [
    "Окно трава молоко яблоко утка",        
    "Мир море лес город кот",            
    "Бабочка апельсин кактус кукла",      
    "Солнце дождь снег облако",             
    "Река ручей озеро болото",              
]

for i, test in enumerate(tests, 1):
    result = slovechki(test)
    print(f"Тест {i}: {test}")
    print(f"Найденные слова: {result}\n")
