"""
Pytest for Query Module
"""

from query import get_commands

import logic_w_w
import logic_i_w
import logic_i_i


class TestQuery(object):
    """ Test object validation for the query's functions"""

    def test_command_stack_w_w_1(self):
        """Tests if the Command Stack is created correctly
        Case: word word command stack"""
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}

        expected_command_stack = {
            'brother': True,
            'child': True,
            'uncle': True,
            'cousin': False,
            'cousin_level': False}

        command_stack, _, _ = get_commands(inputs, logic_w_w)
        assert expected_command_stack == command_stack

    def test_command_stack_w_w_2(self):
        """Tests if the Command Stack is created correctly
        Case: word word functions"""
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}

        expected_functions = {
            'brother': '',
            'child': '',
            'cousin': '',
            'cousin_level': '',
            'createQuery': '',
            'executeQuery': '',
            'fillComplexRules': '',
            'uncle': ''}

        _, functions, _ = get_commands(inputs, logic_w_w)
        assert len(expected_functions) == len(functions)

    def test_command_stack_w_w_3(self):
        """Tests if the Command Stack is created correctly
        Case: word word outputs"""
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}

        expected_outputs = {
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}

        _, _, outputs = get_commands(inputs, logic_w_w)
        assert expected_outputs == outputs

    def test_command_stack_i_w_1(self):
        """Tests if the Command Stack is created correctly
        Case: word word command stack"""
        inputs = {
            'related_bool': True,
            'originated_bool': False,
            'list_bool': False,
            'idiom': 'afr',
            'word_idiom': 'eng',
            'word': 'taco',
            'related': '',
            'originated': '',
            'listing': '',
            'error': ''}

        expected_command_stack = {
            'related': True,
            'originated': False,
            'listing': False}

        command_stack, _, _ = get_commands(inputs, logic_i_w)
        assert expected_command_stack == command_stack

    def test_command_stack_i_w_2(self):
        """Tests if the Command Stack is created correctly
        Case: word word functions"""
        inputs = {
            'related_bool': True,
            'originated_bool': False,
            'list_bool': False,
            'idiom': 'afr',
            'word_idiom': 'eng',
            'word': 'taco',
            'related': '',
            'originated': '',
            'listing': '',
            'error': ''}

        expected_functions = {
            'createQuery': '',
            'executeQuery': '',
            'fillComplexRules': '',
            'listing': '',
            'originated': '',
            'related': ''}

        _, functions, _ = get_commands(inputs, logic_i_w)
        assert len(expected_functions) == len(functions)

    def test_command_stack_i_w_3(self):
        """Tests if the Command Stack is created correctly
        Case: word word outputs"""
        inputs = {
            'related_bool': True,
            'originated_bool': False,
            'list_bool': False,
            'idiom': 'afr',
            'word_idiom': 'eng',
            'word': 'taco',
            'related': '',
            'originated': '',
            'listing': '',
            'error': ''}

        expected_outputs = {
            'idiom': 'afr',
            'word_idiom': 'eng',
            'word': 'taco',
            'related': '',
            'originated': '',
            'listing': '',
            'error': ''}

        _, _, outputs = get_commands(inputs, logic_i_w)
        assert expected_outputs == outputs

    def test_command_stack_i_i_1(self):
        """Tests if the Command Stack is created correctly
        Case: word word command stack"""
        inputs = {
            'common_amount_bool': True,
            'common_bool': False,
            'contributed_most_bool': False,
            'idiom_list_bool': False,
            'idiom_1': 'afr',
            'idiom_2': 'eng',
            'common_amount': '',
            'common': '',
            'contributed_most': '',
            'idiom_list': '',
            'error': ''}

        expected_command_stack = {
            'common_amount': True,
            'common': False,
            'contributed_most': False,
            'idiom_list': False}

        command_stack, _, _ = get_commands(inputs, logic_i_i)
        assert expected_command_stack == command_stack

    def test_command_stack_i_i_2(self):
        """Tests if the Command Stack is created correctly
        Case: word word functions"""
        inputs = {
            'common_amount_bool': True,
            'common_bool': False,
            'contributed_most_bool': False,
            'idiom_list_bool': False,
            'idiom_1': 'afr',
            'idiom_2': 'eng',
            'common_amount': '',
            'common': '',
            'contributed_most': '',
            'idiom_list': '',
            'error': ''}

        _, functions, _ = get_commands(inputs, logic_i_i)
        assert 8 == len(functions)

    def test_command_stack_i_i_3(self):
        """Tests if the Command Stack is created correctly
        Case: word word outputs"""
        inputs = {
            'common_amount_bool': True,
            'common_bool': False,
            'contributed_most_bool': False,
            'idiom_list_bool': False,
            'idiom_1': 'afr',
            'idiom_2': 'eng',
            'common_amount': '',
            'common': '',
            'contributed_most': '',
            'idiom_list': '',
            'error': ''}

        expected_outputs = {
            'idiom_1': 'afr',
            'idiom_2': 'eng',
            'common_amount': '',
            'common': '',
            'contributed_most': '',
            'idiom_list': '',
            'error': ''}

        _, _, outputs = get_commands(inputs, logic_i_i)
        assert expected_outputs == outputs
