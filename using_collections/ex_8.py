text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Line 3 slices and extracts a string ranging from index 21 to 35
# while Line 4 does a search for the index from the original string