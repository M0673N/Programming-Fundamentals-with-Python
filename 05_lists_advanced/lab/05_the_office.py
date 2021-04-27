happiness_data = input().split()
improvement_factor = int(input())
happiness_data = [int(el) * improvement_factor for el in happiness_data]
average = sum(happiness_data) / len(happiness_data)
new_data = [el for el in happiness_data if el >= average]
if len(new_data) >= len(happiness_data) / 2:
    print(f"Score: {len(new_data)}/{len(happiness_data)}. Employees are happy!")
else:
    print(f"Score: {len(new_data)}/{len(happiness_data)}. Employees are not happy!")
