"""
pyDatalog Idiom-Idiom Logic
"""

import logging
from pyDatalog import pyDatalog
from pyDatalog import pyEngine
pyEngine.Logging = True




def fillComplexRules(parent_child, child_parent, all_relations, relations):

    rules = ""

    #Originated
    for relation in parent_child:
        if relations[relation]:
            rules += 'originated(X, Xi, Y, Yi) <= '+relation+'(X, Xi, Y, Yi )\n'

    for relation in child_parent:
        if relations[relation]:
            if relation == "etymology":
                rules += 'originated(X, Xi, Y, Yi) <= etymological_origin_of(Y, Yi, X, Xi)\n'
            elif relation == "is_derived_from":
                rules += 'originated(X, Xi, Y, Yi) <= has_derived_form(Y, Yi, X, Xi)\n'
            else:
                rules += 'originated(X, Xi, Y, Yi) <= '+relation+'(Y, Yi, X, Xi)\n'

    #Listing
    for relation in all_relations:
        if relations[relation]: 
            
            if relation == "etymology":
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & etymological_origin_of(X, Xi, Y, Yi)\n'
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & etymological_origin_of(Y, Yi, X, Xi)\n'
            elif relation == "is_derived_from":
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & has_derived_form(X, Xi, Y, Yi)\n'
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & has_derived_form(Y, Yi, X, Xi)\n'
            else:
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & '+relation+'(X, Xi, Y, Yi)\n'
                rules += 'listing(Xi, Y, Yi) <= ~listing(Xi, Y, Yi) & '+relation+'(Y, Yi, X, Xi)\n'


    pyDatalog.load(rules)

def createQuery(word1, idiom1, word2, idiom2, queryType, relations):
    parent_child = ["derived", "etymologically", "etymological_origin_of", "has_derived_form"]
    child_parent = ["etymologically_related", "etymology", "is_derived_from", "variant"]
    all_relations = parent_child+child_parent
    fillComplexRules(parent_child, child_parent, all_relations, relations)
    query = ""
    word1 = '" '+word1+'"'
    print("Word1",word1)
    word2 = '" '+word2+'"'
    print("Word2",word2)

    relationsNumber = 0
    if queryType == "related":
        for relation in all_relations:
            if relations[relation]:
                relationsNumber += 1
                baseQuery = relation+'(X, '+idiom1+', '+word2+', '+idiom2+') or '+relation+'('+word2+', '+idiom2+', X, '+idiom1+')'
                if relationsNumber > 1:
                    query += ' or '+baseQuery
                else:
                    query += baseQuery

    elif queryType == "originated":
        relationsNumber += 1
        baseQuery = 'originated('+word2+','+idiom2+', _, '+idiom1+')'
        if relationsNumber > 1:
            query += ' or '+baseQuery
        else:
            query += baseQuery

    elif queryType == "listing":
        relationsNumber += 1
        baseQuery = 'listing(Xi, '+word2+', '+idiom2+')'
        if relationsNumber > 1:
            query += ' or '+baseQuery
        else:
            query += baseQuery

    return query

def executeQuery(query, console):
    result= pyDatalog.ask(query)
    console.print("|--------------------Query---------------------\n|",query)
    console.print("|--------------------Result--------------------\n|",result)
    
    if result == None:
        return False
    return True

def related(a, idiom1, word2, idiom2, console, data, relations):
    """If a word is related to an idiom"""
    pyDatalog.Logic(data)
    console.print("Is "+idiom1+" related to "+word2+" ("+idiom2+") ?")
    if idiom1=="" or word2=="" or idiom2=="":
        return "Fill all spaces, please."
    query = createQuery("", idiom1, word2, idiom2, "related", relations)
    return executeQuery(query, console)


def originated(a, idiom1, word2, idiom2, console, data, relations):
    """All words in idiom1 originated from a word"""
    pyDatalog.Logic(data)
    console.print("Words in "+idiom1+" originated from "+word2+"("+idiom2+") ?")
    if word2=="" or idiom2=="" or idiom1=="":
        return "Fill all spaces, please."
    query = createQuery("", idiom1, word2, idiom2, "originated", relations)
    return executeQuery(query, console)


def listing(a, b, word2, idiom2, console, data, relations):
    """All idioms realted to a word"""
    pyDatalog.Logic(data)
    console.print("Idioms related to "+word2+"("+idiom2+") ?")
    if word2=="" or idiom2=="":
        return "Fill all spaces, please."
    query = createQuery("", "", word2, idiom2, "listing", relations)
    return executeQuery(query, console)
