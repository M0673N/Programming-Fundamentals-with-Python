n = int(input())
best = 0
for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > best:
        best_snow = snow
        best_time = time
        best_quality = quality
        best = value
print(f"{best_snow} : {best_time} = {int(best)} ({best_quality})")
