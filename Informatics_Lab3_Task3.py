# Author = Kozlov Timofey Alekseevich
# Group = P3111
# Date = 23.10.2025

import re

number = r"(?:\d{1,2})"              
rangee = r"(?:\d{1,2}-\d{1,2})"       
step = r"(?:\*/\d{1,2})"             
listt = r"(?:\d{1,2}(?:,\d{1,2})*)"   
star = r"\*"                         

field = rf"(?:{star}|{step}|{rangee}|{listt}|{number})"

cron1 = rf"^{field} {field} {field} {field} {field}$"

cron2 = re.compile(cron1)

def valid_cron(cron_expr: str) -> bool:
    return bool(cron2.match(cron_expr))

tests = [
    "30 14 * * *",       
    "*/5 * * * *",       
    "0 0 1 1 *",         
    "1,15,30 0-23 * * *",
    "60 14 * * *"    
]

for test in tests:
    print(f"{test}: {valid_cron(test)}")

