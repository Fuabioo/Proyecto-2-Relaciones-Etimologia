import os
import time
from pprint import pprint


#Parses the .tsv file into several .cl files
def split_files(filename="etymwn.tsv"):
    relations = {}
    start = time.time()
    currDir = os.getcwd() + "\\database\\"
    if ".tsv" in filename:
        with open(filename, 'r', encoding="utf-8") as tsvfile:
            for line in tsvfile:
                columns = line.lower().split("\t")
                language_tag = columns[0].split(':')[0]
                word_1 = '"'+ columns[0].split(':')[1].replace('"', "'").replace(' ','') + '"'
                relation = columns[1].split(":")[1]
                word_2_lang = columns[2].split(':')[0]
                word_2 = '"' + columns[2].split(':')[1].replace("\n", "").replace('"', "'").replace(' ','') + '"'

                if language_tag == "del":
                    language_tag = "delaware"
                if word_2_lang == "del":
                    word_2_lang = "delaware"

                if relation not in relations:
                    relations[relation] = 0
                relations[relation] = relations[relation] + 1

                new_filename = currDir
                new_filename += language_tag + '_'
                new_filename += relation + '_'
                new_filename += word_2_lang + '.cl'

                #print(new_filename, line)

                with open(new_filename, 'a+', encoding="utf-8") as minitsv:
                    # stringTell = ""
                    stringTell = ("+ " + relation + "(" + word_1 + "," + language_tag + "," + word_2+ "," + word_2_lang +")\n" )

                    minitsv.writelines(stringTell)

    pprint(relations)
    print(time.time() - start, "seconds")



                #print(new_filename, line)

if __name__ == '__main__':
    print("Starting")
    split_files()
    print("Finished!")
    input()
