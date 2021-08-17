Script uses PONS online dictionary rest api to provide translation of the German words. User provides German text as attribute. Script delivers the translation of the words.

Pons dictionary: https://en.pons.com/translate Pons Rest Api: https://en.pons.com/p/online-dictionary/developers/api

1.Prerequisites:

Requests (pip install requests)
Pons Account. It allows to obtain X-Secret that enables rest communication. One is already provided in the script translations_management.py so that the script works, but please notice that provided one will expire after some time.
2.How to run scripts - example: python vocabulary_translation_script.py "Wenn die Sonne weg ist, ist es ganz kalt"
