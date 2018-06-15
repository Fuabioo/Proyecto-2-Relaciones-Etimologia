"""
Automated tests for graphic
"""
from tec.ic.ia.pc2.g08 import get_args, get_result


def main():
    """
    Main execution
    """
    valores = [5, 10, 15, 20]
    tableros = [
        "_generated_inputs_/25x25(50).txt",
        "_generated_inputs_/25x25(100).txt",
        "_generated_inputs_/50x50(50).txt",
        "_generated_inputs_/50x50(100).txt",
        "_generated_inputs_/75x75(50).txt",
        "_generated_inputs_/75x75(100).txt",
        "_generated_inputs_/100x100(50).txt",
        "_generated_inputs_/100x100(100).txt"]
    out_file = "Output/gathered_data"
    with open(out_file, 'a') as output:
        for tablero in tableros:
            for vision in valores:
                for zanahorias in valores:
                    args = get_args()
                    args.a_estrella = True
                    args.vision = vision
                    args.zanahorias = zanahorias
                    args.tablero_inicial = tablero
                    result = get_result(algorithm="AStar", args=args)
                    output.write('\n---------- ' + tablero + ' -----------')
                    output.write("\n    vision " + str(vision))
                    output.write("\nzanahorias " + str(zanahorias))
                    output.write("\n   tablero " + tablero)
                    res = result.run()
                    output.write("\n     steps " + str(res[0]))
                    output.write("\n  duration " + str(res[1]))
                    output.write("\n    result " + str(res[2]))
                    output.write('\n')


if __name__ == '__main__':
    main()
