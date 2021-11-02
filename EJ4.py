import unicodedata

print ("Introduce una letra: ")
letra= input()
letra= letra.lower()
trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
letra = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', letra).translate(trans_tab))

if((letra=='a')|(letra=='e')|(letra=='i')|(letra=='o')|(letra=='u')):
    print ("vocal")
else:
    print ("no vocal")   

