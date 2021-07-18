dimensions = (20,3)

def box(parameter=None, dimensions=(20,3), content=None, boxChars=("═", "║", "╔", "╗", "╚", "╝"), ):
    if (type(parameter) == tuple or type(parameter) == list) and len(parameter) == 2 and type(parameter[0]) == int:
        dimensions = parameter
    elif (type(parameter) == tuple or type(parameter) == list or type(parameter) == str):
        content = parameter
    if type(content) == str:
        content = content.split("\n")
    elif content != None:
        dimensions=(
            max(map(len, content)),
            len(content)
        )

    box = ""
    box += boxChars[2]
    for j in range(dimensions[0]):
        box += boxChars[0]
    box += boxChars[3] + "\n"
    for i in range(dimensions[1]):
        box += boxChars[1]
        for j in range(dimensions[0]):
            try:
                box += content[i][j]
            except:
                box += " "
        box += boxChars[1] + "\n"
    box += boxChars[4]
    for j in range(dimensions[0]):
        box += boxChars[0]
    box += boxChars[5]
    return box