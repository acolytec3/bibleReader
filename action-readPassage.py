#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import scriptures
import json

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

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

def readPassage_callback(hermes, intentMessage):
	book = intentMessage.slots.book[0].slot_value.value.value
	chapter = intentMessage.slots.chapter[0].slot_value.value.value
	verse = intentMessage.slots.verse[0].slot_value.value.value
	reference = book + ' ' + str(int(chapter))
	if type(verse)==float:
		reference+=":" + str(int(verse))
	print(reference)
	message = readPassage(reference)
	hermes.publish_end_session(intentMessage.session_id, message)

if __name__=="__main__":
	with Hermes("localhost:1883") as h:
		h.subscribe_intent("konjou:readPassage",readPassage_callback).start()
