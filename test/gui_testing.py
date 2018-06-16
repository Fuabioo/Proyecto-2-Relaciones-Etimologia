"""
GUI Test Module
"""

from tec.ic.ia.p2.g08_controller import Controller


def main():
    """Creates and runs the gui"""
    controller = Controller()  # debug=True)
    controller.run()


if __name__ == '__main__':
    main()
