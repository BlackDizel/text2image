import os
import sys


def convert(text, index):
	print(text)
	os.system(
		"convert -background white -fill black -font Helvetica -pointsize 36 -size 320x caption:\"" + text + "\" output" + str(index)+".png")


def toText(arg):
	output = " "
	return output.join(arg)


def main(args):
	if len(args) != 3:
		print("запустите программу в виде split.py textfile charsnum, где textfile путь к текстовому файлу, "
		"charsnum количество букв в одном выходном файле")
		return

	words = []
	with open(args[1], "r") as fp:
		for line in fp:
			words += line.split()

	text = []
	i = 0
	for item in words:
		retain = int(args[2]) - len(toText(text))
		if retain < len(item):
			i += 1
			convert(toText(text), i)
			text = []

		text.append(item)
	if len(text) > 0:
		convert(toText(text), i)


if __name__ == "__main__":
	main(sys.argv)
