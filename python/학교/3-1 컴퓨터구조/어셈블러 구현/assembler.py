import sys


makeObj = sys.argv[2]
toObjFile = open(makeObj, "w")

# * Main
filePath = sys.argv[1]
src = open(filePath, "r")

dataLine = list()

while True:
    getLine = src.readline()
    if not getLine:
        break
    dataLine.append(getLine)

src.close()

for i in range(0, len(dataLine)):
    dataLine[i] = dataLine[i].strip("\n")

parsingData = list()
for i in range(0, len(dataLine)):
    parsingData.append(dataLine[i].split(" "))


indexOPs = list()
indexParam = list()
indexCommand = list()

sequence = int(parsingData[0][1])

address = 0
value = 0


for i in range(1, len(parsingData)):
    if parsingData[i][0] == "lda":
        tempMemory = parsingData[i][1]

        for j in range(0, len(parsingData)):
            if parsingData[j][0] == tempMemory + ",":
                address = j
                value = int(parsingData[j][2])
                if value < 0:
                    complement = 3
                elif value >= 0:
                    complement = 2

        print(
            "%03d" % (sequence), "0001%012d" % (int(bin(address)[2:])), file=toObjFile
        )
        print("%03d" % (sequence), "0001%012d" % (int(bin(address)[2:])))
        print(
            "%03d" % (sequence + i),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
            file=toObjFile,
        )
        print(
            "%03d" % (sequence + i),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
        )
    elif parsingData[i][0] == "add":
        tempMemory = parsingData[i][1]

        for j in range(0, len(parsingData)):
            if parsingData[j][0] == tempMemory + ",":
                address = j
                value = int(parsingData[j][2])
                if value < 0:
                    complement = 3
                elif value >= 0:
                    complement = 2

        print(
            "%03d" % (sequence + i),
            "0011%012d" % (int(bin(address)[2:])),
            file=toObjFile,
        )
        print("%03d" % (sequence + i), "0011%012d" % (int(bin(address)[2:])))
        print(
            "%03d" % (sequence + i + 1),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
            file=toObjFile,
        )
        print(
            "%03d" % (sequence + i + 1),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
        )
    elif parsingData[i][0] == "sta":
        tempMemory = parsingData[i][1]

        for j in range(0, len(parsingData)):
            if parsingData[j][0] == tempMemory + ",":
                address = j
                value = int(parsingData[j][2])
                if value < 0:
                    complement = 3
                elif value >= 0:
                    complement = 2

        print(
            "%03d" % (sequence + i + 1),
            "0111%012d" % (int(bin(address)[2:])),
            file=toObjFile,
        )
        print("%03d" % (sequence + i + 1), "0111%012d" % (int(bin(address)[2:])))
        print(
            "%03d" % (sequence + i + 2),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
            file=toObjFile,
        )
        print(
            "%03d" % (sequence + i + 2),
            "%04d%012d"
            % (int(bin(address)[complement:]), int((bin(value)[complement:]))),
        )
        print(
            "%03d" % (sequence + i + 3),
            "%016d" % (int(parsingData[0][1])),
            file=toObjFile,
        )
        print("%03d" % (sequence + i + 3), "%016d" % (int(parsingData[0][1])))
