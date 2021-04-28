import re

text = input()
threshold_pattern = r"\d"
emoji_pattern = r"::[A-Z][a-z][a-z]+::|\*\*[A-Z][a-z][a-z]+\*\*"
threshold = 1
threshold_nums = re.findall(threshold_pattern, text)
for num in threshold_nums:
    threshold *= int(num)
emoji_container = re.findall(emoji_pattern, text)
print(f"Cool threshold: {threshold}")
print(f"{len(emoji_container)} emojis found in the text. The cool ones are:")
for emoji in emoji_container:
    total = 0
    if "*" in emoji:
        total -= 4 * ord("*")
    elif ":" in emoji:
        total -= 4 * ord(":")
    for letter in emoji:
        total += ord(letter)
    if total > threshold:
        print(f"{emoji}")
