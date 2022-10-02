# In a nested loop i is iterated for certain constraints on row
# and j is iterated for certain conditions i=on column
# and accordingly '*' character or space is added
x = int(input('Enter Number :'))  
# Enter dimensions of square box for which we want to draw pattern
for i in range(x):  # iterations for rows
    for j in range(x):  # iterations for column
        if ((i == 0 and j < x-1) or j == 0 or (i == x-1 and j < x-1) or (j == x-1 and 0 < i < x-1)):
        # conditions for priting *
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()  # new line entered for creating pattern
