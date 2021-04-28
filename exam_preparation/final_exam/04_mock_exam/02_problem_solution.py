import re

n = int(input())
codes = []
for i in range(n):
    code = input()
    codes.append(code)

valid_pattern = r"@#+[A-Z][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]+[A-Z]@#+"
nums_pattern = r"\d+"

codes_as_text = ", ".join(codes)

good_codes = re.findall(valid_pattern, codes_as_text)

for code in codes:
    if code in good_codes:
        group = re.findall(nums_pattern, code)
        if group:
            group_code = ""
            for i in group:
                group_code += i
            print(f"Product group: {group_code}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
