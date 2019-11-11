import re

# Formatting value for SQL
# If it's a string add quotes around it
def formatVal(vals):
    regex = re.compile("[A-Za-z/]")
    valString = ""
    for val in vals:
        valString += val
        if val is not vals[-1]:
            valString += " "

    if regex.search(valString) is not None:
        valNew = '\'' + valString + '\''
        valString = valNew
    return valString


def main():
    f = open("dataScraper.txt")
    vals = []
    string = "INSERT INTO VALUES ("
    pastLine = None
    for line in f:
        if line is "\n":
            pastLine = None
            insertString = string
            for v in vals:
                insertString += str(v) + ", "
            insertStringFormatted = insertString[:-2] + ")"
            # insertString[-1] = ")"
            print(insertStringFormatted)
            vals = []
            continue
        if pastLine is None:
            pastLine = line
            continue
        valsInLine = line.split()
        
        val = formatVal(valsInLine[1:])
        pastLine = line
        if pastLine == "\n":
            pastLine = None
        vals.append(val)
    #print(vals)
if __name__ == "__main__":
    main()