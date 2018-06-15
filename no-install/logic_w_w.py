"""
pyDatalog Word-Word Logic
"""
from pyDatalog import pyDatalog

"""

1. Rel:derived
    Padre -> hijo

2. Rel:etymologically
    Padre -> hijo

4. Rel:etymological_origin_of
    Padre -> hijo

6. Rel:has_derived_form
    Padre -> hijo

3. Rel:etymologically_related
    Hijo -> padre

5. Rel:etymology
    Hijo -> padre

7. Rel:is_derived_from
    Hijo -> padre

8. Rel:variant:ortography
    Hijo -> padre
"""

def out_(p1,p2,p3,p4):

    print(p1,p2,p3,p4)
    return

def fillComplexRules(parent_child, child_parent, relations):

    rules = ""
    #Hermanos relation+'(X, IX, '+W1+', '+I1+') & '+relation+'(X, IX, '+W2+', '+I2+')'
    for relation in parent_child:
        if relations[relation]:
            rules += 'hermanos(W1,I1,W2,I2) <= '+relation+'(X, IX, W1, I1) & '+relation+'(X, IX, W2, I2) & (~(W1 == W2) or ~(I1 == I2))\n'
            rules += 'hermanos(W1,I1,W2,I2) <= hermanos(W2, I2, W1, I1)\n'

    for relation in child_parent:
        if relations[relation]:
            if relation == "etymology":
                rules += 'hermanos(W1,I1,W2,I2) <= etymological_origin_of(W1, I1, X, IX) & etymological_origin_of(W2, I2, X, IX) & (~(W1 == W2) or ~(I1 == I2))\n'
            elif relation == "is_derived_from":
                rules += 'hermanos(W1,I1,W2,I2) <= is_derived_from(W1, I1, X, IX) & is_derived_from(W2, I2, X, IX) & (~(W1 == W2) or ~(I1 == I2))\n'
            else:
                rules += 'hermanos(W1,I1,W2,I2) <= '+relation+'(W1, I1, X, IX) & '+relation+'(W2, I2, X, IX) & (~(W1 == W2) or ~(I1 == I2))\n'
            rules += 'hermanos(W1,I1,W2,I2) <= hermanos(W2, I2, W1, I1)\n'






    
    return

    #Child
    for relation in parent_child:
        if relations[relation]:
            rules += 'hijo(W1,I1,W2,I2) <= '+relation+'(W2,I2, W1, I1)\n'

    for relation in child_parent:
        if relations[relation]:
            if relation == "etymology":
                rules += 'hijo(W1,I1,W2,I2) <= etymological_origin_of(W1, I1, W2, I2)\n'
            elif relation == "is_derived_from":
                rules += 'hijo(W1,I1,W2,I2) <= has_derived_form(W1, I1, W2, I2)\n'
            else:
                rules += 'hijo(W1,I1,W2,I2) <= '+relation+'(W1, I1, W2, I2)\n'

    #Uncle relation+'(G, IG, '+W1+','+I1+') & '+relation+'(G, IG, P, IP) & '+relation+'(P, IP, '+W2+','+I2+')'
    for relation in parent_child:
        if relations[relation]:
            rules += 'tio(W1,I1,W2,I2) <= '+relation+'(G, IG, W1,I1) & '+relation+'(G, IG, P, IP) & '+relation+'(P, IP, W2, I2) & (~(W1 == P) or ~(I1 == IP))\n'

    for relation in child_parent:
        if relations[relation]:
            if relation == "etymology":
                rules += 'tio(W1,I1,W2,I2) <= etymological_origin_of(W1,I1,G, IG) & etymological_origin_of(P, IP, G, IG) & etymological_origin_of(W2, I2, P, IP) & (~(W1 == P) or ~(I1 == IP))\n'
            elif relation == "is_derived_from":
                rules += 'tio(W1,I1,W2,I2) <= is_derived_from(W1,I1,G, IG) & is_derived_from(P, IP, G, IG) & is_derived_from(W2, I2, P, IP) & (~(W1 == P) or ~(I1 == IP))\n'
            else:
                rules += 'tio(W1,I1,W2,I2) <= '+relation+'(W1,I1,G, IG) & '+relation+'(P, IP, G, IG) & '+relation+'(W2, I2, P, IP) & (~(W1 == P) or ~(I1 == IP))\n'


    #Cousin
    
    for relation in parent_child:
        if relations[relation]:

            rules += 'primos(A,Ai,B,Bi,G) <= primos2(B,Bi,A,Ai,G) \n'
            rules += 'primos(A,Ai,B,Bi,G) <= primos2(A,Ai,B,Bi,G)\n'
            rules += 'primos2(A,Ai,B,Bi,G) <= '+relation+'(Papa,Papai, A,Ai) & '+relation+'(Abuelo,Abueloi, Papa,Papai) & '+relation+'(Abuelo,Abueloi, Tio,Tioi) & '+relation+'(Tio,Tioi,B,Bi) & ~(A == B)  & (G==1)'
            rules += ' & (VARI==console.print(Papa,Papai, A,Ai))\n'
            rules += 'primos2(A,Ai,B,Bi,G) <= ('+relation+'(Papa,Papai, A,Ai) & primos2(B,Bi,Papa,Papai,F)) & (G==F+1)\n'


    for relation in child_parent:
        if relations[relation]:
            rules += 'primos(A,Ai,B,Bi,G) <= primos2(B,Bi,A,Ai,G)\n'
            rules += 'primos(A,Ai,B,Bi,G) <= primos2(A,Ai,B,Bi,G)\n'
            if relation == "etymology":
                
                rules += 'primos2(A,Ai,B,Bi,G) <= (etymological_origin_of(A,Ai,Papa,Papai) & etymological_origin_of(Papa,Papai,Abuelo,Abueloi) & etymological_origin_of(Tio,Tioi,Abuelo,Abueloi) & etymological_origin_of(B,Bi,Tio,Tioi)) & (~(A == B) or ~(Ai == Bi)) & (G==1)\n'
                rules += 'primos2(A,Ai,B,Bi,G) <= (etymological_origin_of(A,Ai,Papa,Papai) & primos2(Papa,Papai,B,Bi,F)) & (G==F+1)\n'
            elif relation == "is_derived_from":
                
                rules += 'primos2(A,Ai,B,Bi,G) <= (has_derived_form(A,Ai,Papa,Papai) & has_derived_form(Papa,Papai,Abuelo,Abueloi) & has_derived_form(Tio,Tioi,Abuelo,Abueloi) & has_derived_form(B,Bi,Tio,Tioi)) & (~(A == B) or ~(Ai == Bi)) & (G==1)\n'
                rules += 'primos2(A,Ai,B,Bi,G) <= (has_derived_form(A,Ai,Papa,Papai) & primos2(Papa,Papai,B,Bi,F)) & (G==F+1)\n'
            else:
                
                rules += 'primos2(A,Ai,B,Bi,G) <= ('+relation+'(A,Ai,Papa,Papai) & '+relation+'(Papa,Papai,Abuelo,Abueloi) & '+relation+'(Tio,Tioi,Abuelo,Abueloi) & '+relation+'(B,Bi,Tio,Tioi)) & (~(A == B) or ~(Ai == Bi)) & (G==1)\n'
                rules += 'primos2(A,Ai,B,Bi,G) <= ('+relation+'(A,Ai,Papa,Papai) & primos2(Papa,Papai,B,Bi,F)) & (G==F+1)\n'

    pyDatalog.load(rules)



def createQuery(word1, I1, word2, I2, queryType, relations):
    """Formulates the query based on the query type and the relations checked"""    
    

    W1 = '" '+word1+'"'
    W2 = '" '+word2+'"'
    #W1 = word1
    #W2 = word2

    parent_child = ["derived", "etymologically", "etymological_origin_of", "has_derived_form"]
    child_parent = ["etymologically_related", "etymology", "is_derived_from", "variant"]
    all_relations = parent_child+child_parent
    fillComplexRules(parent_child, child_parent, relations)
    relationsNumber = 0
    query = ""
    #Query for both parent_child-child_parent types of relation to determine if both words are brothers 
    if queryType == "brother":
        relationsNumber += 1
        baseQuery = 'hermanos('+W1+', '+I1+', '+W2+', '+I2+')'
        if relationsNumber > 1:
            query += ' or '+baseQuery
        else:
            query += baseQuery

    #Query for both parent_child-child_parent types of relation to determine if W1 is W2's parent 
    elif queryType == "child":
            relationsNumber += 1
            baseQuery = 'hijo('+W1+','+I1+','+W2+','+I2+')'
            if relationsNumber > 1:
                query += ' or '+baseQuery
            else:
                query += baseQuery
        

    
    elif queryType == "uncle":

            relationsNumber += 1
            baseQuery = 'tio('+W1+','+I1+','+W2+','+I2+')'
            if relationsNumber > 1:
                query += ' or '+baseQuery
            else:
                query += baseQuery



    elif queryType == "cousin":
        for relation in all_relations:
            if relations[relation]:
                relationsNumber += 1
                baseQuery = 'primos('+W1+',' +I1+',' +W2+',' +I2+', 1)'
                if relationsNumber > 1:
                    query += ' or '+baseQuery
                else:
                    query += baseQuery

    elif queryType == "cousin_level":
        for relation in all_relations:
            if relations[relation]:
                relationsNumber += 1
                baseQuery = 'primos('+W1+',' +I1+',' +W2+',' +I2+', G)'
                
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

def brother(word1, idiom1, word2, idiom2, console, data, relations):
    """Checks if two given words are brothers in the current data's context"""
    pyDatalog.create_terms('console')
    pyDatalog.Logic(data)
    if word1=="" or word2=="":
        return "Fill all the spaces, please."

    query = createQuery(word1, idiom1, word2, idiom2, "brother", relations)
    print("Query: ",query)
    return executeQuery(query, console)

def child(word1, idiom1, word2, idiom2, console, data, relations):
    """Checks if the first word (Son) is the second word's (Father) child"""
    pyDatalog.create_terms('console')
    pyDatalog.Logic(data)
    if word1=="" or word2=="":
        return "Fill all the spaces, please."

    query = createQuery(word1, idiom1, word2, idiom2, "child", relations)
    print("Query: ",query)
    return executeQuery(query, console)


def uncle(word1, idiom1, word2, idiom2, console, data, relations):
    """Checks if the first word (Son) is the second word's (Father) child"""
    pyDatalog.create_terms('console')
    pyDatalog.Logic(data)
    if word1=="" or word2=="":
        return "Fill all the spaces, please."

    query = createQuery(word1, idiom1, word2, idiom2, "uncle", relations)
    print("Query: ",query)
    return executeQuery(query, console)


def cousin(word1, idiom1, word2, idiom2, console, data, relations):
    """Checks if two given words are cousins in the current data's context"""
    
    pyDatalog.create_terms('console')
    pyDatalog.Logic(data)
    pyDatalog.create_terms('console')
    if word1=="" or word2=="":
        return "Fill all the spaces, please."

    query = createQuery(word1, idiom1, word2, idiom2, "cousin", relations)
    print("Query: ",query)
    return executeQuery(query, console)


def cousin_level(word1, idiom1, word2, idiom2, console, data, relations):
    """Checks if two given words are cousins and returns their cousin level"""
    pyDatalog.create_terms('console')
    pyDatalog.Logic(data)
    pyDatalog.create_terms('console')
    if word1=="" or word2=="":
        return "Fill all the spaces, please."

    query = createQuery(word1, idiom1, word2, idiom2, "cousin_level", relations)
    print("Query: ",query)
    return executeQuery(query, console)
