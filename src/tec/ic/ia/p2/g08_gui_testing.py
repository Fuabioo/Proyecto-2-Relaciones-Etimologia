"""
GUI Test Module
"""

from .g08_controller import Controller


def main():
    """Creates and runs the gui"""
    controller = Controller()  # debug=True)
    controller.run()


if __name__ == '__main__':
    main()
