"""
Proyecto Corto 1 - Simulador de Votos
"""
import csv
import math
import random
import argparse
from io import StringIO
import numpy

from . import actas
from . import indicadores

ACTAS_FINAL = "ACTASFINAL.csv"
INDICATORS_FILE = "INDICADORES.csv"

TESTING = False
RIGGED_RANDOM = 0

# Definición de rangos para asignación aleatoria de cantones
CANTONES = [["SAN JOSE", 1, 409],
            ["ESCAZU", 410, 490],
            ["DESAMPARADOS", 491, 779],
            ["PURISCAL", 780, 851],
            ["TARRAZU", 852, 879],
            ["ASERRI", 880, 962],
            ["MORA", 963, 1009],
            ["GOICOECHEA", 1010, 1165],
            ["SANTA ANA", 1166, 1229],
            ["ALAJUELITA", 1230, 1317],
            ["VAZQUEZ DE CORONADO", 1318, 1409],
            ["ACOSTA", 1410, 1452],
            ["TIBAS", 1453, 1548],
            ["MORAVIA", 1549, 1625],
            ["MONTES DE OCA", 1626, 1699],
            ["TURRUBARES", 1700, 1715],
            ["DOTA", 1716, 1729],
            ["CURRIDABAT", 1730, 1815],
            ["PEREZ ZELEDON", 1816, 2066],
            ["LEON CORTEZ CASTRO", 2067, 2092],
            ["ALAJUELA", 2093, 2463],
            ["SAN RAMON", 2464, 2593],
            ["GRECIA", 2594, 2713],
            ["SAN MATEO", 2714, 2725],
            ["ATENAS", 2726, 2765],
            ["NARANJO", 2766, 2828],
            ["PALMARES", 2829, 2881],
            ["POAS", 2882, 2922],
            ["OROTINA", 2923, 2953],
            ["SAN CARLOS", 2954, 3181],
            ["ZARCERO", 3182, 3203],
            ["VALVERDE VEGA", 3204, 3232],
            ["UPALA", 3233, 3301],
            ["LOS CHILES", 3302, 3332],
            ["GUATUSO", 3333, 3358],
            ["CARTAGO", 3359, 3575],
            ["PARAISO", 3576, 3661],
            ["LA UNION", 3662, 3788],
            ["JIMENEZ", 3789, 3815],
            ["TURRIALBA", 3816, 3949],
            ["ALVARADO", 3950, 3971],
            ["OREAMUNO", 3972, 4035],
            ["EL GUARCO", 4036, 4098],
            ["HEREDIA", 4099, 4265],
            ["BARVA", 4266, 4325],
            ["SANTO DOMINGO", 4326, 4386],
            ["SANTA BARBARA", 4387, 4434],
            ["SAN RAFAEL", 4435, 4498],
            ["SAN ISIDRO", 4499, 4531],
            ["BELEN", 4532, 4564],
            ["FLORES", 4565, 4593],
            ["SAN PABLO", 4594, 4632],
            ["SARAPIQUI", 4633, 4711],
            ["LIBERIA", 4712, 4798],
            ["NICOYA", 4799, 4904],
            ["SANTA CRUZ", 4905, 4996],
            ["BAGACES", 4997, 5028],
            ["CARRILLO", 5029, 5076],
            ["CANHAS", 5077, 5118],
            ["ABANGARES", 5119, 5157],
            ["TILARAN", 5158, 5195],
            ["NANDAYURE", 5196, 5225],
            ["LA CRUZ", 5226, 5257],
            ["HOJANCHA", 5258, 5276],
            ["PUNTARENAS", 5277, 5470],
            ["ESPARZA", 5471, 5518],
            ["BUENOS AIRES", 5519, 5597],
            ["MONTES DE ORO", 5598, 5623],
            ["OSA", 5624, 5682],
            ["QUEPOS", 5683, 5727],
            ["GOLFITO", 5728, 5795],
            ["COTO BRUS", 5796, 5866],
            ["PARRITA", 5867, 5900],
            ["CORREDORES", 5901, 5970],
            ["GARABITO", 5971, 5992],
            ["LIMON", 5993, 6130],
            ["POCOCI", 6131, 6310],
            ["SIQUIRRES", 6311, 6396],
            ["TALAMANCA", 6397, 6442],
            ["MATINA", 6443, 6486],
            ["GUACIMO", 6487, 6542]]

# Definición votos posibles (Incluyendo votos válidos, nulos y blancos)
PARTIDOS = ["ACCESIBILIDAD SIN EXCLUSION",
            "ACCION CIUDADANA",
            "ALIANZA DEMOCRATA CRISTIANA",
            "DE LOS TRABAJADORES",
            "FRENTE AMPLIO",
            "INTEGRACION NACIONAL",
            "LIBERACION NACIONAL",
            "MOVIMIENTO LIBERTARIO",
            "NUEVA GENERACION",
            "RENOVACION COSTARRICENSE",
            "REPUBLICANO SOCIAL CRISTIANO",
            "RESTAURACION NACIONAL",
            "UNIDAD SOCIAL CRISTIANA",
            "VOTOS NULOS",
            "VOTOS BLANCOS"]


PARTIDOS2 = ["ACCION CIUDADANA",
            "RESTAURACION NACIONAL",
            "VOTOS NULOS",
            "VOTOS BLANCOS"]

# Definición de provincias
PROVINCIAS = ["SAN JOSE",
              "ALAJUELA",
              "CARTAGO",
              "HEREDIA",
              "GUANACASTE",
              "PUNTARENAS",
              "LIMON"]

VOTES = [1404242,
         848146,
         490903,
         433677,
         326953,
         410929,
         386862]


def parse_args():
    """
    Argument parser
    """
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument(
        '--indicadores',
        nargs="+",
        default=['default'],
        help='Archivo csv. Ej: indicadores.csv')
    parser.add_argument(
        '--actas',
        nargs="+",
        default=['default'],
        help='Archivo csv. Ej: actas.csv')
    return parser.parse_args()


def load_data():
    """
    Loads the default data and if specified loads from data file
    """
    args = parse_args()
    if args.indicadores[0] != 'default' and args.actas[0] != 'default':
        indicadores.INDICADORES = open(args.indicadores[0], 'r')
        actas.ACTAS_FINAL = open(args.actas[0], 'r')
    elif args.indicadores[0] == 'default' and args.actas[0] != 'default':
        actas.ACTAS_FINAL = open(args.actas[0], 'r')
    elif args.actas[0] == 'default' and args.indicadores[0] != 'default':
        indicadores.INDICADORES = open(args.indicadores[0], 'r')


def csv2mat():
    """
    Converts the csv to a matrix
    """
    matrix = [[]]
    for i in range(1, 8):
        with open("ActaSesion" + str(i) + ".csv", 'r') as f:
            reader = csv.reader(f)
            act = list(reader)
        if i == 1:
            matrix = act
        else:
            act = numpy.delete(act, (0), axis=1)
            matrix = numpy.hstack((matrix, act))

    matrix = numpy.delete(matrix, slice(0, 2), axis=0)
    i = 1
    while i < len(matrix[0]):
        for j in range(len(CANTONES)):
            if int(CANTONES[j][1]) <= int(matrix[0][i]) <= int(CANTONES[j][2]):
                matrix[0][i] = CANTONES[j][0]
                break
        if matrix[0][i].isdigit():
            matrix = numpy.delete(matrix, (i), axis=1)
            i -= 1
        i += 1

    fixed_matrix = matrix[:, [0]]
    for i in range(1, len(matrix[0])):
        find = False
        for j in range(len(fixed_matrix[0])):
            if fixed_matrix[0][j] == matrix[0][i]:
                find = True
                for k in range(1, len(matrix)):
                    fixed_matrix[k][j] = str(
                        int(fixed_matrix[k][j]) + int(matrix[k][i]))
        if find == False:
            fixed_matrix = numpy.hstack((fixed_matrix, matrix[:, [i]]))

    numpy.savetxt("ACTASFINAL.csv", fixed_matrix, delimiter=",", fmt="%s")
    print("Procesamiento terminado")


def round_retain_total(original_list):
    """
    Retains the total after rounded
    """
    original_total = round(sum(original_list), 0)
    rounded_list = numpy.array(original_list).round(0)
    #new_total = rounded_list.sum()
    error = original_total - sum(rounded_list)
    n = int(round(error))
    result = rounded_list
    for _, i in sorted(((original_list[i] - rounded_list[i], i)
                        for i in range(len(original_list))), reverse=n > 0)[:abs(n)]:
        result[i] += math.copysign(1, n)
    result = list(map(int, result))
    return result


def get_att(percent=50):
    """
    Gets the attribute and uses the rigged random if testing
    """
    if TESTING:
        percent = RIGGED_RANDOM
    random.seed()
    return int(random.randrange(100) < float(percent))


def get_vote(arr):
    """
    Gets the vote of an array
    """
    #val = int(arr[17])
    choose = random.randrange(int(arr[17]))
    arr = numpy.concatenate((arr[1:14], arr[15:17]))

    for i in range(len(arr)):
        choose -= int(arr[i])
        if choose <= 0:
            return PARTIDOS[i]


def get_vote2(arr):
    """
    Gets the vote of an array
    """
    #val = int(arr[17])
    choose = random.randrange(int(arr[6]))
    arr = numpy.concatenate((arr[1:3], arr[4:6]))

    for i in range(len(arr)):
        choose -= int(arr[i])
        if choose <= 0:
            return PARTIDOS2[i]


def generar_muestra_provincia(n, nombre_provincia, sample_type):
    """
    Generates the sample by province
    """
    #print("Muestra: " + nombre_provincia)
    reader = csv.reader(StringIO(actas.ACTAS_FINAL))
    acts = list(reader)

    reader = csv.reader(StringIO(actas.ACTAS_FINAL2))
    acts2 = list(reader)

    reader = csv.reader(StringIO(indicadores.INDICADORES))
    indicators = list(reader)

    index = PROVINCIAS.index(nombre_provincia) * 32
    total = 0
    totals = []
    for i in range(1, len(indicators[index + 1])):

        total += float(indicators[index + 1][i])
        totals += [float(indicators[index + 1][i])]

    for i in range(len(totals)):
        totals[i] = totals[i] / total * n

    totals = round_retain_total(totals)
    population = []
    for i in range(1, len(indicators[index])):
        for j in range(1, len(acts[0])):
            if indicators[index][i] == acts[0][j]:
                for k in range(totals[i - 1]):
                    arr = numpy.array(acts)
                    arr2 = numpy.array(acts2)
                    hombres_ratio = float(indicators[index + 5][i])
                    hombres = (hombres_ratio * 100) / (hombres_ratio + 100)
                    votes = []
                    if sample_type != 2:
                        votes += get_vote(arr[:, j]),						# Voto 1
                    if sample_type == 1 or sample_type == 2:

                    	votes += get_vote2(arr2[:, j]),						# Voto 2
                    population += [[  # Demo-Geográficas
                        # Canton
                        (indicators[index][i]),
                        # Población total
                        float(indicators[index + 1][i]),
                        # Superficie
                        float(indicators[index + 2][i]),
                        # Densidad Poblacional (Estatico)
                        float(indicators[index + 3][i].replace(" ", "")),
                        # Personas que viven en zona urbana
                        get_att(indicators[index + 4][i]),
                        # Hombre/Mujeres
                        get_att(hombres),
                        # Relacion de dependencia
                        get_att(indicators[index + 6][i]),
                        # Viviendas individuales (Estatico)
                        float(indicators[index + 7][i]),
                        # Promedio de ocupantes (Estatico)
                        float(indicators[index + 8][i]),
                        # Porcentaje de viviendas en buen estado
                        get_att(indicators[index + 9][i]),
                        # Porcentaje de viviendas hacinadas
                        get_att(indicators[index + 10][i]),
                        # Educativas
                        # Porcentaje de alfabetismo
                        get_att(indicators[index + 11][i]),
                        float(indicators[index + 12][i]),
                        float(indicators[index + 13][i]),
                        # Escolaridad promedio
                        float(indicators[index + 14][i]),
                        # 25 a 49 años
                        float(indicators[index + 15][i]),
                        # 50+ años
                        float(indicators[index + 16][i]),
                        # Porcentaje de asistencia a la educaci¢n
                        # regular
                        float(indicators[index + 17][i]),
                        # Menor de 5 anhos
                        float(indicators[index + 18][i]),
                        # 5 a 17 anhos
                        float(indicators[index + 19][i]),
                        # 18 a 24 anhos
                        float(indicators[index + 20][i]),
                        # 25 y m s anhos
                        float(indicators[index + 21][i]),
                        # Económicas
                        # Fuera de la fuerza de trabajo
                        get_att(indicators[index + 22][i]),
                        # Tasa neta de participacion
                        get_att(indicators[index + 23][i]),
                        # Hombres
                        float(indicators[index + 24][i]),
                        # Mujeres
                        float(indicators[index + 25][i]),
                        # Porcentaje de poblacion ocupada no
                        # asegurada
                        get_att(indicators[index + 26][i]),
                        # Sociales
                        # Porcentaje de poblacion nacida en el
                        # extranjero
                        get_att(indicators[index + 27][i]),
                        # Porcentaje de poblacion con discapacidad
                        get_att(indicators[index + 28][i]),
                        # Porcentaje de poblacion no asegurada
                        get_att(indicators[index + 29][i]),
                        # Porcentaje de hogares con jefatura
                        # femenina
                        get_att(indicators[index + 30][i]),
                        # Porcentaje de hogares con jefatura
                        # compartida
                        get_att(indicators[index + 31][i]),
                        nombre_provincia,                               # Provincia

                        ] + votes]                             

    return population

"""
Sample type = 0 first round
Sample type = 1 second round using first round
Sample type = 2 second round without first round
"""
def generar_muestra_pais(n,sample_type = 0):
    """
    Generates the sample of all provinces
    """
    total = 0
    totals = []
    for i in range(len(VOTES)):
        total += float(VOTES[i])
        totals += [float(VOTES[i])]

    for i in range(len(totals)):
        totals[i] = totals[i] / total * n
    totals = round_retain_total(totals)
    population = []
    for i in range(len(totals)):
        population += generar_muestra_provincia(totals[i], PROVINCIAS[i],sample_type)

    return population


def show_percentages(population):
    """
    Shows the percentages for a given population
    """
    print("Porcentajes:\n")
    percents = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(population)):
        for j in range(len(PARTIDOS)):
            if population[i][len(population[0]) - 1] == PARTIDOS[j]:
                percents[j] += 1

    for j in range(len(PARTIDOS)):
        print(PARTIDOS[j] + ":  " + str((percents[j] / len(population) * 100)))

    return population


def show_percentages_indicator(population, indicator):
    """
    Shows the percentages indicators
    """
    position = get_position(indicator)
    total = 0.0
    for i in range(len(population)):
        total += population[i][position]

    print(indicator + ": " + str((total / len(population))))
    return total / len(population)


def show_percentages_indicator_partido(population, indicator, partido):
    """
    Shows categorized percentages for a given population
    """
    position = get_position(indicator)
    total_indicador = 0.0
    total_partido = 0
    for i in range(len(population)):
        if population[i][1] == partido:
            total_partido += 1
            total_indicador += population[i][position]

    print(partido + " - " + indicator + ": " +
          str((total_indicador / total_partido)) + "%")
    return total_indicador / total_partido


def get_position(indicator):
    """
    Obtains position for indicator
    """
    return {"URBANIDAD": 3,
            "HOMBRES": 5,
            "ALFABETIZACION": 11,
            "ESCOLARIDAD": 14,
            "ASISTENCIA": 17,
            "PARTICIPACION": 23
            }[indicator]


# load_data()
def main():
    """
    Main execution
    """
    # load_data()
    #csv2mat()
    # show_percentages(generar_muestra_provincia(100,"CARTAGO"))
    # show_percentages(generar_muestra_pais(200000))

    # MUESTRA
    muestra1 = generar_muestra_pais(10,2)

    # PORCENTAJES
    # show_percentages(muestra1)

    show_percentages_indicator(muestra1, "URBANIDAD")
    show_percentages_indicator(muestra1, "HOMBRES")
    show_percentages_indicator(muestra1, "ALFABETIZACION")
    show_percentages_indicator(muestra1, "ESCOLARIDAD")
    show_percentages_indicator(muestra1, "ASISTENCIA")
    show_percentages_indicator(muestra1, "PARTICIPACION")

    #show_percentages_indicator_partido(muestra1, "PARTICIPACION", "RESTAURACION NACIONAL")


if __name__ == '__main__':
    main()
