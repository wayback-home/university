from Menu import *
from Poetry import *
from BookOfPoetry import *

myPoetryBook = BookOfPoetry()
title = "나의 애송시"
contents = ["진달래 꽃", "그리움", "먼 곳에서부터"]

myMenu = Menu(title, contents)
myMenu.print()
myMenu.getMenuNumber()

while not myMenu.isExit():
    myPoetry = myPoetryBook.PoetryBook[myMenu.MenuNumber - 1]
    myPoetry.print()
    myMenu.print()
    myMenu.getMenuNumber()

print("\t\t안녕히 가세요.")
