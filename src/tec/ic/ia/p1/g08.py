"""
Proyecto #1 - Predicción Votaciones
"""
import csv
import numpy
from argparse import ArgumentParser

from tec.ic.ia.p1 import g08_redes_neuronales
from tec.ic.ia.p1 import g08_kdtrees
from tec.ic.ia.p1 import g08_desicion_tree
from tec.ic.ia.p1 import g08_regresion
from tec.ic.ia.p1 import g08_svm
from tec.ic.ia.pc1 import g08

def get_args():
    """
    Processes the arguments, returning them
    """
    parser = ArgumentParser(description="Proyect #1 - Votes predictor")

    parser.add_argument('--poblacion', default='-1', type=int, required=True)
    parser.add_argument(
        '--porcentaje-pruebas',
        default='-1',
        type=int,
        required=True)

    parser.add_argument('--provincia', default='PAIS', type=str)

    parser.add_argument('--regresion-logistica', action='store_true')
    parser.add_argument('--l1', action='store_true')
    parser.add_argument('--l2', action='store_true')

    parser.add_argument('--red-neuronal', action='store_true')
    parser.add_argument('--numero-capas', default='1', type=int)
    parser.add_argument('--unidades-por-capa', default='60', type=int)
    parser.add_argument('--funcion-activacion', default='relu', type=str)

    parser.add_argument('--arbol', action='store_true')
    parser.add_argument('--umbral-poda', default='0.1', type=float)

    parser.add_argument('--knn', action='store_true')
    parser.add_argument('--k', default='3', type=int)

    parser.add_argument('--svm', action='store_true')
    args = parser.parse_args()
    return args


def regresion_logistica(args, dataset):
    """
    Ejecucion de la regresion logica
    """
    print("Regresion con l1", args.l1, ", l2", args.l2)
    result = g08_regresion.regression(dataset, args.porcentaje_pruebas, args.l1, args.l2)
    get_output(dataset, result, "REGRESION_LOGISTICA")

def red_neuronal(args, dataset):
    """
    Ejecucion de la red neuronal
    """
    if args.numero_capas == -1:
        print("ValueError: numero-capas")
    elif args.unidades_por_capa == -1:
        print("ValueError: unidades-por-capa")
    else:
        print(
            "Red neuronal con",
            args.numero_capas,
            "capas,",
            args.unidades_por_capa,
            "unidades por capa y",
            args.funcion_activacion,
            "como funcion de activacion")
        result = g08_redes_neuronales.execute_model(args.numero_capas,
            args.unidades_por_capa,
            args.funcion_activacion,
            dataset,
            args.porcentaje_pruebas)
        get_output(dataset, result, "RED_NEURONAL")


def arbol(args, dataset):
    """
    Ejecucion del arbol de decision
    """
    print("Arbol con umbral de poda", args.umbral_poda)
    result = g08_desicion_tree.cross_validate(dataset=dataset, percent=args.porcentaje_pruebas, error_margin=args.umbral_poda)
    get_output(dataset, result, "DECISION_TREE")

def knn(args, dataset):
    """
    Ejecucion del knn
    """
    if args.k == -1:
        print("ValueError: k")
    else:
        print("KNN con k = ", args.k)
        result = g08_kdtrees.cross_validate(dataset=numpy.array(dataset), percent=args.porcentaje_pruebas, k=args.k)
        get_output(dataset, result, "KNN")


def svm(args, dataset):
    """
    Ejecucion de la svm
    """
    print("SVM = ", args.svm)
    result = g08_svm.execute_model(
            dataset,
            args.porcentaje_pruebas)
    get_output(dataset, result, "SVM")

def gen_dataset(n, provincia, sample_type=1):
    """
    Generates the working dataset
    """
    result = None
    if provincia != "PAIS":
        result = g08.generar_muestra_provincia(n,provincia,sample_type)
    else:
        result = g08.generar_muestra_pais(n,sample_type)
    return result

def write_csv(data, model_name):
    # for votante in initial_dataset:
    #     print(votante)
    model_name = model_name.lower()
    filename = model_name + "_output.csv"
    column_names = ["Cantón",
        "Población total",
        "Superficie (km2)",
        "Densidad de población",
        "Porcentaje de población urbana",
        "Relación hombres-mujeres",
        "Relación de dependencia demográfica",
        "Viviendas individuales ocupadas",
        "Promedio de ocupantes",
        "Porcentaje de viviendas en buen estado",
        "Porcentaje de viviendas hacinadas",
        "Porcentaje de alfabetismo",
        "10 a 24 años",
        "25 y más años",
        "Escolaridad promedio",
        "25 a 49 años",
        "50 o más años",
        "Porcentaje de asistencia a la educación regular",
        "Menor de 5 años",
        "5 a 17 años",
        "18 a 24 años",
        "25 y más años",
        "Personas fuera de la fuerza de trabajo (15 años y más)",
        "Tasa neta de participación",
        "Hombres",
        "Mujeres",
        "Porcentaje de población ocupada no asegurada",
        "Porcentaje de población nacida en el extranjero",
        "Porcentaje de población con discapacidad",
        "Porcentaje de población no asegurada",
        "Porcentaje de hogares con jefatura femenina",
        "Porcentaje de hogares con jefatura compartida",
        "Provincia",
        "Voto 1ra ronda",
        "Voto 2ra ronda",
        "es_entrenamiento",
        "prediccion_r1",
        "prediccion_r2",
        "prediccion_r2_con_r1"]
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(column_names)
        for line in data:
            writer.writerow(line)


def get_output(initial_dataset, result, model_name):
    """
    Generates a csv with the given result and prints
    on the console the train and test error
    """
    size = len(result["res_1"])
    for i in range(size):
        initial_dataset[i].append(result["train_set"][i])
        initial_dataset[i].append(result["res_1"][i])
        initial_dataset[i].append(result["res_2"][i])
        initial_dataset[i].append(result["res_3"][i])
    write_csv(initial_dataset, model_name)
    print(model_name)
    print("   - Error de entrenamiento: ", 1 - result["err_train"])
    print("   - Error de pruebas: ", 1 - result["err_test"])

def run_prediction():
    """
    Runs a prediction for each model
    """
    # Load Arguments
    args = get_args()
    # Generate dataset
    dataset = gen_dataset(args.poblacion, args.provincia)
    if args.regresion_logistica:
        regresion_logistica(args, dataset)
    elif args.red_neuronal:
        red_neuronal(args, dataset)
    elif args.arbol:
        arbol(args, dataset)
    elif args.knn:
        knn(args, dataset)
    elif args.svm:
        svm(args, dataset)


if __name__ == '__main__':
    run_prediction()
