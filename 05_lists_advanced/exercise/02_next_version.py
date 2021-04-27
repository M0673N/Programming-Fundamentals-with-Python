version = input().split(".")
version = [int(el) for el in version]
version[2] += 1
if version[2] == 10:
    version[2] = 0
    version[1] += 1
if version[1] == 10:
    version[1] = 0
    version[0] += 1
version = [str(el) for el in version]
print(".".join(version))
