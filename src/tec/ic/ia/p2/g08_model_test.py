"""
Pytest for Model Module
"""

from tec.ic.ia.p2.g08_model import get_files, Model


class TestModel(object):
    """ Test object validation for the model object"""

    def test_file_getter_1(self):
        """Tests if it gets correctly all the files given a criteria
        Case: criteria without multiplicity"""
        filename = "afr_etymological_origin_of_afr"
        expected_result = (['afr_etymological_origin_of_afr.cl'], True)
        obtained_result = get_files(filename)
        assert obtained_result == expected_result

    def test_file_getter_2(self):
        """Tests if it gets correctly all the files given a criteria
        Case: criteria with (right) multiplicity"""
        filename = "afr_etymological_origin_of_*"
        expected_result = ([
            'afr_etymological_origin_of_afr.cl',
            'afr_etymological_origin_of_deu.cl',
            'afr_etymological_origin_of_eng.cl',
            'afr_etymological_origin_of_fin.cl',
            'afr_etymological_origin_of_fra.cl',
            'afr_etymological_origin_of_ita.cl',
            'afr_etymological_origin_of_nld.cl',
            'afr_etymological_origin_of_por.cl',
            'afr_etymological_origin_of_rus.cl',
            'afr_etymological_origin_of_spa.cl'], True)
        obtained_result = get_files(filename)
        assert obtained_result == expected_result

    def test_file_getter_3(self):
        """Tests if it gets correctly all the files given a criteria
        Case: criteria with (left) multiplicity"""
        filename = "*_etymological_origin_of_afr"
        expected_result = ([
            'afr_etymological_origin_of_afr.cl',
            'ara_etymological_origin_of_afr.cl',
            'deu_etymological_origin_of_afr.cl',
            'fra_etymological_origin_of_afr.cl',
            'ind_etymological_origin_of_afr.cl',
            'msa_etymological_origin_of_afr.cl',
            'nld_etymological_origin_of_afr.cl',
            'por_etymological_origin_of_afr.cl'], True)
        obtained_result = get_files(filename)
        assert obtained_result == expected_result

    def test_appender(self):
        """Tests if the data appends correctly to a model"""
        test_model_manual = Model()
        logics = {}
        logics["afr_etymological_origin_of_fin"] = """+ etymological_origin_of(" apartheid",afr," apartheid",fin)"""
        logics["afr_etymological_origin_of_rus"] = """+ etymological_origin_of(" apartheid",afr," апартеид",rus)"""

        test_model_manual.append_data(logics["afr_etymological_origin_of_fin"])
        test_model_manual.append_data(logics["afr_etymological_origin_of_rus"])
        result_1 = test_model_manual.data

        test_model_pool = Model()
        data_pool = []
        data_pool.append(logics["afr_etymological_origin_of_fin"])
        data_pool.append(logics["afr_etymological_origin_of_rus"])

        test_model_pool.append_data(data_pool)
        result_2 = test_model_pool.data
        assert result_1 == result_2

    def test_clear(self):
        """Tests if the data appends correctly to a model"""
        test_model = Model()
        logics = {}
        logics["afr_etymological_origin_of_fin"] = """+ etymological_origin_of(" apartheid",afr," apartheid",fin)"""
        logics["afr_etymological_origin_of_rus"] = """+ etymological_origin_of(" apartheid",afr," апартеид",rus)"""

        test_model.append_data(logics["afr_etymological_origin_of_fin"])
        test_model.append_data(logics["afr_etymological_origin_of_rus"])

        test_model.clear()

        assert test_model.data == ""
