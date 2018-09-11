import scriptures
import json

bible = []

def readVerse(reference):
	with open('ESV.json') as data:
		bible = json.load(data)
	ref = scriptures.extract(reference) 
	if ref != []:
		print(ref)
		verse = bible[ref[0][0]][str(ref[0][1])][str(ref[0][2])]
		return verse
	else:
		return('This is not a valid reference')

def readPassage(reference):
	with open('ESV.json') as data:
		bible = json.load(data)
	ref = scriptures.extract(reference)
	print(ref)
	passage = ''
	if ref != []:
		verse = ref[0][2]
		for chapter in range(ref[0][1],ref[0][3]+1):
			if chapter < ref[0][3]:
				while 1:
					try:
						passage+=bible[ref[0][0]][str(chapter)][str(verse)]
						passage+=' '
						verse+=1
					except:
						break
			else:
				while verse <= ref[0][4]:
					passage+=bible[ref[0][0]][str(chapter)][str(verse)]
					verse+=1
			chapter+=1
			verse = 1
		return passage
	else:
		return('This is not a valid reference')

