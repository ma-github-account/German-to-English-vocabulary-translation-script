
import sys
import requests
import json

translation_direction = "deen"

headers = {
    'X-Secret': 'b7ad6a785a74561720d36595ce71b34fbdc3fad94e43f5c4e0c9dbd8187afab1',
}

excluded_words = ["Der", "Die", "Das", "der", "die", "das", "Dem", "dem", "Den", "den", "Des", "des", ".", ",", "-", "ein", "eine", "einer", "-eines", "Ein", "Eine", "Einer", "-Eines"]

def prepareGetRequest(get_request_specification):

    separator = '&' if '?' in get_request_specification else '?'
    request = f"https://api.pons.com/v1/dictionary{separator}{get_request_specification}"
    return request

def translateAWord(translation_direction, delivered_word):

	get_request_specification = f"l={translation_direction}&q={delivered_word}"
	get_response = requests.get(prepareGetRequest(get_request_specification), headers=headers)
	ResponseDataInJsonFormat = json.loads(get_response.text)
	translated_word = (ResponseDataInJsonFormat[0]['hits'][0]['roms'][0]['arabs'][0]['translations'][0]['target'])
	return translated_word

def translateAWordForDeclaredTranslationDirection(original_word):

	return translateAWord(translation_direction, original_word)

def cleanTheTranslatedString(translated_string):

	return translated_string.split(sep="<")[0].split(sep="&")[0].split(sep="[")[0].rstrip(' ')

def translateAText(original_text):

	word_list = original_text.split(sep=" ")
	word_dictionary = {}
	for word in word_list:
		try:
			word_dictionary[word] = cleanTheTranslatedString(translateAWordForDeclaredTranslationDirection(word))
		except:
			word_dictionary[word] = "Word not found"
	return word_dictionary

def printTheDictionary(word_dictionary):

	print()
	for word in word_dictionary:
		if len(word_dictionary[word]) > 0 and word not in excluded_words:
			print(word +  " : " + word_dictionary[word])
	print()

def translateTextProvidedAsScriptParameterAndPrintTheTranslations():

	if len(sys.argv)>1:
		printTheDictionary(translateAText(sys.argv[1]))
	else:
		print("Text has not been specified")










