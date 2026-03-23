kop = [99, 92, 78, 63]

# Step 1: start reference with the first element
Largest = kop[3]

# Step 2: loop over the rest of the list
for num in kop:
    # Step 3: update reference if current element is bigger
    if num > Largest:
        Largest = num

# Step 4: print the largest number after loop
print(Largest)
