from math import floor

centuries = int(input())
print(f"{centuries} centuries = {centuries * 100} years = {floor(centuries * 36524.22)} \
days = {floor(floor(centuries * 36524.22) * 24)} hours = {floor(floor(centuries * 36524.22) * 24) * 60} minutes")
