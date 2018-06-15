"""
pyDatalog Idiom-Word Logic
"""

from pyDatalog import pyDatalog

def formatResult(result):
    output = ""
    for key in result:
        output += "| "+str(key)+":"+str(result[str(key)])+"\n"
    return output



def to_int(response):
    return str(response)[2:-3]

def fillComplexRules(parent_child, child_parent, all_relations, relations):

    rules = ""
    for relation in all_relations:
        if relations[relation]:
            rules += 'palabras(X,I) <= ~palabras(X,I) & '+relation+'(X,I,A,B)\n'
            rules += 'palabras(X,I) <= ~palabras(X,I) & '+relation+'(A,B,X,I)\n'
            rules += 'igualesEntreIdiomas(I1,I2,X) <= palabras(X,I1) & palabras(X,I2)\n'
            rules += 'porcentaje(X, Y, Z) <= (Z == X / Y*100)\n'

    for relation in parent_child:
        if relations[relation]:
            rules += 'aporte(I1,I2,Y) <= '+relation+'(_,I1,Y,I2) & ~(I2 == I1)\n'
    for relation in child_parent:
        if relations[relation]:
            if relation == "etymology":
                rules += 'aporte(I1,I2,Y) <= etymological_origin_of(Y,I2, _,I1) & ~(I2 == I1)\n'
            elif relation == "is_derived_from":
                rules += 'aporte(I1,I2,Y) <= has_derived_form(Y,I2, _,I1) & ~(I2 == I1)\n'
            else:
                rules += 'aporte(I1,I2,Y) <= '+relation+'(Y,I2, _,I1) & ~(I2 == I1)\n'
    pyDatalog.load(rules)
    return




def createQuery(idiom1, idiom2, queryType, relations, console):


    parent_child = ["derived", "etymologically", "etymological_origin_of", "has_derived_form"]
    child_parent = ["etymologically_related", "etymology", "is_derived_from", "variant"]
    all_relations = parent_child+child_parent
    fillComplexRules(parent_child, child_parent, all_relations, relations)
    
    relationsNumber = 0
    query = ""
    if queryType == "common_amount":
        relationsNumber += 1
        baseQuery = '(Y==len(igualesEntreIdiomas('+idiom1+','+idiom2+',_)))'
        if relationsNumber > 1:
            query += ' or '+baseQuery
        else:
            query += baseQuery

    elif queryType == "common":
        relationsNumber += 1
        baseQuery = 'igualesEntreIdiomas('+idiom1+','+idiom2+',_)'
        if relationsNumber > 1:
            query += ' or '+baseQuery
        else:
            query += baseQuery

    elif queryType == "contributed_most":
        relationsNumber += 1
        result = str(pyDatalog.ask('(aporte(X,'+idiom1+',Y) ) '))
        console.print("|--------------------Query---------------------\n|", 'aporte(X, '+idiom1+',Y)')
        
        if result != "None":
            Y = int(to_int(pyDatalog.ask('Y==len(palabras(_,'+idiom1+'))')))
            result =  eval("["+ result [1:-1].replace("(","[").replace(")","]")+"]")
            result = [row[0] for row in result]
            result = {i:result.count(i)*100/Y for i in result}
            key = max(result.keys(), key=(lambda k: result[k]))
            result = "Idiom: "+key+"', Percentage: "+str(result[key])
        console.print("|--------------------Result--------------------\n|", result)

    elif queryType == "idiom_list":
        relationsNumber += 1
        result = str(pyDatalog.ask('(aporte(X, '+idiom1+',Y))'))
        console.print("|--------------------Query---------------------\n|", 'aporte(X, '+idiom1+',Y)')
        if result != "None":
            Y = int(to_int(pyDatalog.ask('Y==len(palabras(_,'+idiom1+'))')))
            result =  eval("["+ result [1:-1].replace("(","[").replace(")","]")+"]")
            result = [row[0] for row in result]
            result = {i:result.count(i)*100/Y for i in result}


            console.print("|--------------------Result--------------------\n", formatResult(result))

        else:
            console.print("|--------------------Result--------------------\n|", "None")

    return query


def executeQuery(query, console, queryType):
    if queryType == "contributed_most" or queryType == "idiom_list":
        return "Result in console."
    result= pyDatalog.ask(query)
    console.print("|--------------------Query---------------------\n|",query)
    console.print("|--------------------Result--------------------\n|",result)
    
    if result == None:
        return False
    return True

def common_amount(a,b, idiom1, idiom2, console, data, relations):
    """Counts all common words between two idioms"""
    pyDatalog.Logic(data)
    
    query = createQuery(idiom1, idiom2, "common_amount", relations, console)
    return executeQuery(query, console, "common_amount")


def common(a,b, idiom1, idiom2, console, data, relations):
    """Lists all common words between two idioms"""
    pyDatalog.Logic(data)
   
    query = createQuery(idiom1, idiom2, "common", relations, console)
    return executeQuery(query, console, "common")


def contributed_most(a,b, idiom1, d, console, data, relations):
    """Idioms that contributed more to the other"""
    pyDatalog.Logic(data)
    query = createQuery(idiom1, "", "contributed_most", relations, console)
    return executeQuery(query, console, "contributed_most")


def idiom_list(a,b, idiom1, d, console, data, relations):
    """List all idioms that were contributed (show percentage)"""
    pyDatalog.Logic(data)
    query = createQuery(idiom1, "", "idiom_list", relations, console)
    return executeQuery(query, console, "idiom_list")