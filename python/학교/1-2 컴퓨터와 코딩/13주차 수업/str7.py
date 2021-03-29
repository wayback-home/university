instr, outstr = "", ""

while True:
    sel = int(input("1. 대문자 2. 소문자 3. 섞어서 4. 종료 : "))

    if sel == 1:
        instr = input("대문자 입력 : ")
    if sel == 2:
        instr = input("소문자 입력 : ")
    if sel == 3:
        instr = input("대소문자 입력 : ")
    else:
        break

    n = len(instr)

    for i in range(0, n):
        ch = instr[i]
        if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
            change = ch.lower()
        elif ord("a") and ord(ch) <= ord("z"):
            change = ch.upper()
        else:
            change = ch
        outstr += change
    print("%s  =>  %s" % (instr, outstr))
    outstr = ""