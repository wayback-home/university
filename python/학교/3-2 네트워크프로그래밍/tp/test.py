import sys
import os

filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)


filename = sys.stdin.readline()

gccCommand = f"gcc ./{filename}"
runCommand = "./a.out"

os.system(gccCommand)
os.system(runCommand)
