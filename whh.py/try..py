dash = "Bakul sangwan"

# find returns the lowest index of the substring or -1 if not found
idx = dash.find("sangwan")
print("Index of 'sangwan':", idx)

# find with start (and optional end)
idx2 = dash.find("a", 2)  # find 'a' starting from index 2
print("First 'a' after index 2:", idx2)

# rfind finds the last occurrence
last_a = dash.rfind("a")
print("Last 'a' index:", last_a)

# example: find space to split first and last name
space = dash.find(" ")
first = dash[:space] if space != -1 else dash
last = dash[space+1:] if space != -1 else ""
print("First name:", first)
print("Last name:", last)

# case-insensitive search
ci = dash.lower().find("bakul")
print("Case-insensitive index of 'bakul':", ci)