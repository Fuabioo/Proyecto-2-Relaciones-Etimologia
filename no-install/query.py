"""
Query routing module, the commands are stacked for later execution from the inputs
"""
import inspect

import logic_w_w
import logic_i_w
import logic_i_i


def get_commands(inputs: dict, module):
    """Processes the inputs and the given logic module
    Returns:
        The mapped functions on the module
        The command stacked from the inputs
        The outputs needed in the view"""
    functions = dict(inspect.getmembers(module, inspect.isfunction))
    command_stack = {}
    outputs = {}
    for key, value in inputs.items():
        if "_bool" in key.lower():
            key = key.replace('_bool', '')
            if key == "list":
                key = "listing"
            command_stack[key] = value
        else:
            if key == "list":
                key = "listing"
            outputs[key] = value
    return command_stack, functions, outputs


def execute(strings: tuple, parameters: tuple, module):
    """Executes the specified module over the inputs"""
    inputs = parameters[0]
    console = parameters[1]
    string_1, string_2, string_3, string_4 = strings
    if console:
        command_stack, functions, outputs = get_commands(inputs, module)
        for command, do_it in command_stack.items():
            if do_it:
                result = functions[command](
                    string_1,
                    string_2,
                    string_3,
                    string_4,
                    console,
                    parameters[2],  # data
                    parameters[3])  # relations
                outputs[command] = str(result)
    return outputs


def word_word(inputs: dict, relations: dict, console=None, data=None):
    """Prepares parameters for the logic w w module"""
    strings = (
        inputs["word_1"],
        inputs["idiom_1"],
        inputs["word_2"],
        inputs["idiom_2"])
    parameters = (inputs, console, data, relations)
    # try:
    outputs = execute(
    strings=strings,
    parameters=parameters,
    module=logic_w_w)
    # except BaseException as exception:
    #     outputs = {"error": "Predicate undefined."}
    #     console.print(exception)
    # Returns the dictionary with the outputs
    return outputs


def idiom_word(inputs: dict, relations: dict, console=None, data=None):
    """Prepares parameters for the logic w i module"""

    strings = ('', inputs["idiom"], inputs["word"], inputs["word_idiom"])
    parameters = (inputs, console, data, relations)
    try:
        outputs = execute(
            strings=strings,
            parameters=parameters,
            module=logic_i_w)
    except BaseException as exception:
        outputs = {"error": "Predicate undefined."}
        console.print(exception)

    # Returns the dictionary with the outputs
    return outputs


def idiom_idiom(inputs: dict, relations: dict, console=None, data=None):
    """Prepares parameters for the logic i i module"""
    strings = ('', '', inputs["idiom_1"], inputs["idiom_2"])
    parameters = (inputs, console, data, relations)
    # try:
    outputs = execute(
        strings=strings,
        parameters=parameters,
        module=logic_i_i)
    # except BaseException as exception:
    #     outputs = {"error": "Predicate undefined."}
    #     console.print(exception)
    # Returns the dictionary with the outputs
    return outputs
