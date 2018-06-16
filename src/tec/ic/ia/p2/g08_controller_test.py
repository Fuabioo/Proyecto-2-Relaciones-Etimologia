"""
Pytest for Controller Module
"""
# aaq: Pawanobskewi   rel:etymological_origin_of  eng: Penobscot

from tec.ic.ia.p2.g08_controller import Controller


class TestController(object):
    """ Test object validation for the controller object"""

    def test_thread_building_1(self):
        """
        Tests if the controller builds thread names correctly
        (Acording to the respective file name)
        Base Case: one relation, two idioms
        """
        test_controller = Controller()
        inputs = {
            "idiom_1": "afr",
            "idiom_2": "eng"
        }
        relations = {
            "etymological_origin_of": True,
            "variant": False
        }
        expected_result = ["afr_etymological_origin_of_eng.cl"]
        obtained_result = test_controller.build_threads(inputs, relations)
        assert expected_result == obtained_result

    def test_thread_building_2(self):
        """
        Tests if the controller builds thread names correctly
        (Acording to the respective file name)
        Base Case Variation: one relation, one idiom
        """
        test_controller = Controller()
        inputs = {
            "idiom": "afr"
        }
        relations = {
            "etymological_origin_of": True,
            "variant": False
        }
        expected_result = [
            "afr_etymological_origin_of_afr.cl",
            'afr_etymological_origin_of_deu.cl',
            "afr_etymological_origin_of_eng.cl",
            'afr_etymological_origin_of_fin.cl',
            'afr_etymological_origin_of_fra.cl',
            'afr_etymological_origin_of_ita.cl',
            'afr_etymological_origin_of_nld.cl',
            "afr_etymological_origin_of_por.cl",
            'afr_etymological_origin_of_rus.cl',
            'afr_etymological_origin_of_spa.cl']
        obtained_result = test_controller.build_threads(inputs, relations)
        assert expected_result == obtained_result

    def test_thread_building_3(self):
        """
        Tests if the controller builds thread names correctly
        (Acording to the respective file name)
        Base Case Variation: one relation, zero idioms
        """
        test_controller = Controller()
        inputs = {}
        relations = {
            "etymological_origin_of": True,
            "variant": False
        }
        expected_result = 17
        obtained_result = test_controller.build_threads(inputs, relations)
        assert expected_result == len(obtained_result)

    def test_thread_building_4(self):
        """
        Tests if the controller builds thread names correctly
        (Acording to the respective file name)
        Base Case Variation: multiple relations, two idioms
        """
        test_controller = Controller()
        inputs = {
            "idiom_1": "afr",
            "idiom_2": "eng"
        }
        relations = {
            "etymology": True,
            "etymological_origin_of": True,
            "variant": True,
            "derived": False
        }
        expected_result = ["afr_etymological_origin_of_eng.cl"]
        obtained_result = test_controller.build_threads(inputs, relations)
        assert expected_result == obtained_result

    def test_thread_building_5(self):
        """
        Tests if the controller builds thread names correctly
        (Acording to the respective file name)
        Base Case Variation: multiple relations, one idioms
        """
        test_controller = Controller()
        inputs = {
            "idiom_1": "afr"
        }
        relations = {
            "etymology": True,
            "etymological_origin_of": True,
            "variant": True,
            "derived": False
        }
        expected_result = [
            'afr_etymology_afr.cl',
            'afr_etymology_ara.cl',
            'afr_etymology_deu.cl',
            'afr_etymology_fra.cl',
            'afr_etymology_ind.cl',
            'afr_etymology_msa.cl',
            'afr_etymology_nld.cl',
            'afr_etymology_por.cl',
            'afr_etymological_origin_of_afr.cl',
            'afr_etymological_origin_of_deu.cl',
            'afr_etymological_origin_of_eng.cl',
            'afr_etymological_origin_of_fin.cl',
            'afr_etymological_origin_of_fra.cl',
            'afr_etymological_origin_of_ita.cl',
            'afr_etymological_origin_of_nld.cl',
            'afr_etymological_origin_of_por.cl',
            'afr_etymological_origin_of_rus.cl',
            'afr_etymological_origin_of_spa.cl']
        obtained_result = test_controller.build_threads(inputs, relations)
        assert expected_result == obtained_result

    def test_inputs_1(self):
        """Tests if the input check is done correctly
        Case: Inputs have querys selected"""
        test_controller = Controller()
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
        result = test_controller.check_inputs(inputs)

        assert result

    def test_inputs_2(self):
        """Tests if the input check is done correctly
        Case: No idiom_1"""
        test_controller = Controller()
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': '',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}
        result = test_controller.check_inputs(inputs)

        assert not result

    def test_inputs_3(self):
        """Tests if the input check is done correctly
        Case: No word_1"""
        test_controller = Controller()
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': '',
            'idiom_2': 'afr',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}
        result = test_controller.check_inputs(inputs)

        assert not result

    def test_inputs_4(self):
        """Tests if the input check is done correctly
        Case: No idiom_2"""
        test_controller = Controller()
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': '',
            'word_2': 'vaar',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}
        result = test_controller.check_inputs(inputs)

        assert not result

    def test_inputs_5(self):
        """Tests if the input check is done correctly
        Case: No word_2"""
        test_controller = Controller()
        inputs = {
            'brother_bool': True,
            'child_bool': True,
            'uncle_bool': True,
            'cousin_bool': False,
            'cousin_level_bool': False,
            'idiom_1': 'afr',
            'word_1': 'afvaar',
            'idiom_2': 'afr',
            'word_2': '',
            'brother': '',
            'child': '',
            'uncle': '',
            'cousin': '',
            'cousin_level': '',
            'error': ''}
        result = test_controller.check_inputs(inputs)

        assert not result

    def test_relations_1(self):
        """Tests if the realtion check is done correctly
        Case: Inputs have relations selected"""
        test_controller = Controller()
        inputs = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result, _ = test_controller.check_relations(inputs)

        assert result

    def test_relations_2(self):
        """Tests if the realtion check is done correctly
        Case: Inputs have NO relations selected"""
        test_controller = Controller()
        inputs = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result, _ = test_controller.check_relations(inputs)

        assert not result

    def test_relations_3(self):
        """Tests if the realtion check is done correctly
        Case: One work relation"""
        test_controller = Controller()
        inputs = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        expected_result = ['etymological_origin_of']
        _, work_relations = test_controller.check_relations(inputs)

        assert expected_result == work_relations

    def test_relations_4(self):
        """Tests if the realtion check is done correctly
        Case: No work relation"""
        test_controller = Controller()
        inputs = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        expected_result = []
        _, work_relations = test_controller.check_relations(inputs)

        assert expected_result == work_relations

    def test_relations_5(self):
        """Tests if the realtion check is done correctly
        Case: Two work relation, but three relations selected
        **This because two types of relations are the same but inverted,
        so it's pointless to load them both"""
        test_controller = Controller()
        inputs = {
            'derived': False,
            'etymologically': False,
            'etymology': True,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': True,
            'variant': False}
        expected_result = ['has_derived_form', 'etymological_origin_of']
        _, work_relations = test_controller.check_relations(inputs)

        assert expected_result == work_relations
