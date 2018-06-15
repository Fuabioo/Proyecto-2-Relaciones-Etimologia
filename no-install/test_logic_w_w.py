"""
Pytest for Logic Word-Word Module
"""

from model import Model
import logic_w_w


class Dummy:
    """Dummy console, this prevents modifying the code for the logic_w_w"""

    def __init__(self):
        self.dummy = ""  # Dummy variable

    def print(self, *args):
        """dummy function"""
        self.dummy = args


class TestLogicWW(object):
    """ Test object validation for the logic"""

    def test_brothers_1(self):
        """Test Case: afvaar(afr) is brother of vaar(afr)? -> No"""
        thread = "afr_etymological_origin_of_afr.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.brother(
            "afvaar",
            "afr",
            "vaar",
            "afr",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_brothers_2(self):
        """Test Case: anholdelse(dan) is brother of anseelse(dan)? -> Yes"""
        thread = "dan_etymological_origin_of_dan.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.brother(
            "anholdelse",
            "dan",
            "anseelse",
            "dan",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_child_1(self):
        """Test Case: afvaar(afr) is child of vaar(afr)? -> Yes"""
        thread = "afr_etymological_origin_of_afr.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.child(
            "afvaar",
            "afr",
            "vaar",
            "afr",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_child_2(self):
        """Test Case: anholdelse(dan) is child of anseelse(dan)? -> No"""
        thread = "dan_etymological_origin_of_dan.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.child(
            "anholdelse",
            "dan",
            "anseelse",
            "dan",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_1(self):
        """Test Case: afvaar(afr) is uncle of vaar(afr)? -> No"""
        thread = "afr_etymological_origin_of_afr.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.uncle(
            "afvaar",
            "afr",
            "vaar",
            "afr",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_2(self):
        """Test Case: anholdelse(dan) is uncle of anseelse(dan)? -> No"""
        thread = "dan_etymological_origin_of_dan.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.uncle(
            "anholdelse",
            "dan",
            "anseelse",
            "dan",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_3(self):
        """Test Case: "tio" is uncle of "sobrino"? -> Yes"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," sobrino",spa)']
        model_test.append_data(data_pool)
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.uncle(
            "tio",
            "spa",
            "sobrino",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_cousin_1(self):
        """Test Case: afvaar(afr) is cousin of vaar(afr)? -> No"""
        thread = "afr_etymological_origin_of_afr.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin(
            "afvaar",
            "afr",
            "vaar",
            "afr",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_2(self):
        """Test Case: anholdelse(dan) is cousin of anseelse(dan)? -> No"""
        thread = "dan_etymological_origin_of_dan.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin(
            "anholdelse",
            "dan",
            "anseelse",
            "dan",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_3(self):
        """Test Case: hijo is cousin of primo? -> Yes"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," hijo",spa)',
            '+ etymological_origin_of(" tio",spa," primo",spa)']
        model_test.append_data(data_pool)
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin(
            "hijo",
            "spa",
            "primo",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_cousin_level_1(self):
        """Test Case: afvaar(afr) cousin level of vaar(afr)? -> Not cousins"""
        thread = "afr_etymological_origin_of_afr.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin_level(
            "afvaar",
            "afr",
            "vaar",
            "afr",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_level_2(self):
        """Test Case:
        anholdelse(dan) cousin level of anseelse(dan)? -> Not cousins"""
        thread = "dan_etymological_origin_of_dan.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin_level(
            "anholdelse",
            "dan",
            "anseelse",
            "dan",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_level_3(self):
        """Test Case: hijo cousin level of primo? -> 1"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," hijo",spa)',
            '+ etymological_origin_of(" tio",spa," primo",spa)']
        model_test.append_data(data_pool)
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_w_w.cousin_level(
            "hijo",
            "spa",
            "primo",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result
