'''
import random

with open('etymwn_mini.tsv', 'w', encoding="utf-8") as minitsv:
    with open('etymwn.tsv', 'r', encoding="utf-8") as tsvfile:
        for line in tsvfile:
            if(random.random() < 0.05):
                minitsv.writelines(line)
minitsv.close()
tsvfile.close()
'''
import random
cont = 0
with open('cl.cl', 'w', encoding="utf-8") as minitsv:
	
    with open('etymwn.tsv', 'r', encoding="utf-8") as tsvfile:
        for line in tsvfile:
	        #if(random.random() < 0.01):
            stringTell = ""
            columns = line.split("\t")
            language_tag = columns[0].split(':')[0]
            word_1 = '"'+ columns[0].split(':')[1].replace('"', "'").replace(' ','') + '"'
            relation = columns[1].split(':')[1]
            word_2 = '"' + columns[2].split(':')[1].replace("\n", "").replace('"', "'").replace(' ','') + '"'
            word_2_lang = columns[2].split(':')[0]

            #stringTell+= ("+ hasWord("+language_tag.lower()+","+word_1.lower()+")\n")
            #stringTell+= ("+ hasWord("+word_2_lang.lower()+","+word_2.lower()+")\n")
            #stringTell+=  (language_tag, word_1, relation, word_2, word_2_lang)
            stringTell+= ("+ " + relation.lower() + "(" + word_1.lower() + "," + language_tag.lower() + "," + word_2.lower()+ "," + word_2_lang.lower() +")\n" )

            minitsv.writelines(stringTell)
            cont+=1
            if cont == 60000:
            	break
minitsv.close()
tsvfile.close()