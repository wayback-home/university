str1 = "주륵주륵"
str2 = "내린다"

print(str1 + str2)
print(str1, str2)

print(str1 * 3)

str3 = "반짝반짝 작은별"

print(str3[-1])
print(str3[3:])
print(str3[1:4])

str4 = "   교통대학교   "

print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

print(len(str4))

print(str3.count("반짝"))

print(str4.count(" "))

str5 = "Choi Yeong Seo"

print(str5.upper())
print(str5.title())
print(str5.swapcase())

print(str5.startswith("Choi"))
print(str5.startswith("seo"))
print(str5.endswith("Seo"))
print(str5.endswith("Choi"))

print(str5.find("o"))
print(str5.find("o", 2))
print(str5.find("o", 3))
print(str5.find("r"))
