dimensions = (20,3)

def box(dimensions=(20,3), boxChars=["═", "║", "╔", "╗", "╚", "╝"], )
print("╔", end="")
for i in range(dimensions[0]):
    print("═", end="")
print("╗\n", end="")
for j in range(dimensions[1]):
    print("║", end="")
    for i in range(dimensions[0]):
        print(" ", end="")
    print("║\n", end="")