infile = None
instr = ""

infile = open(
    "data1.txt",
    "r",
    encoding="UTF-8",
)


while True:
    instr = infile.readline()
    if instr == " ":
        break
    print(instr)

infile.close()