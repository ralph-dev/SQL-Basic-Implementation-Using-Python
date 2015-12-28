from database import *
import unittest
import squeal


class TestAssignmentTwoFunctions(unittest.TestCase):

    def test_both_equal_sized_dictionaries(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': ['value_e', 'value_f'], 'key_4': ['value_g', 'value_h']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_b', 'value_b'],
                         'key_2': ['value_c', 'value_c', 'value_d', 'value_d'],
                         'key_3': ['value_e', 'value_f', 'value_e', 'value_f'],
                         'key_4': ['value_g', 'value_h', 'value_g', 'value_h']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #1 - (Two Equal Sized Dictionaries)")

    def test_both_one_column_and_value_same_value(self):
        d1 = {'key_1': ['value_a']}
        d2 = {'key_2': ['value_a']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a'], 'key_2': ['value_a']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #2 - (Empty Rows)")

    def test_both_one_column_and_value_same_value(self):
        d1 = {'key_1': ['value_a'], 'key_2': ['value_a'], 'key_3': ['value_a'],
              'key_4': ['value_a'], 'key_5': ['value_a']}
        d2 = {'key_2_1': ['value_a'], 'key_2_2': ['value_a'],
              'key_2_3': ['value_a'], 'key_2_4': ['value_a'],
              'key_2_5': ['value_a']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a'],
                         'key_2': ['value_a'],
                         'key_3': ['value_a'],
                         'key_4': ['value_a'],
                         'key_5': ['value_a'],
                         'key_2_1': ['value_a'],
                         'key_2_2': ['value_a'],
                         'key_2_3': ['value_a'],
                         'key_2_4': ['value_a'],
                         'key_2_5': ['value_a']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #2 - (5 keys 1 value each)")

    def test_both_dictionaries_same_values(self):
        d1 = {'key_1': ['value_a', 'value_a'], 'key_2': ['value_a', 'value_a']}
        d2 = {'key_3': ['value_a', 'value_a'], 'key_4': ['value_a', 'value_a']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_a', 'value_a'],
                         'key_2': ['value_a', 'value_a', 'value_a', 'value_a'],
                         'key_3': ['value_a', 'value_a', 'value_a', 'value_a'],
                         'key_4': ['value_a', 'value_a', 'value_a', 'value_a']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #3 - (Two Equal Sized Dictionaries With Exact Same Values)")

    def test_both_empty_rows(self):
        d1 = {'key_1': [], 'key_2': []}
        d2 = {'key_3': [], 'key_4': []}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': [], 'key_2': [], 'key_3': [], 'key_4': []}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #4 - (Empty Rows)")

    def test_one_normal_diontary_one_empty_dictionary(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': [], 'key_4': []}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': [], 'key_2': [], 'key_3': [], 'key_4': []}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #5 - (normal dict and empty dict)")

    def test_both_one_more_keys(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': ['value_e', 'value_f'],
              'key_4': ['value_g', 'value_h'],
              'key_5': ['value_i', 'value_j']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_b', 'value_b'],
                         'key_2': ['value_c', 'value_c', 'value_d', 'value_d'],
                         'key_3': ['value_e', 'value_f', 'value_e', 'value_f'],
                         'key_4': ['value_g', 'value_h', 'value_g', 'value_h'],
                         'key_5': ['value_i', 'value_j', 'value_i', 'value_j']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #6 - (2 values in 1 , 1 value in other dict)")

    def test_both_one_column_and_value(self):
        d1 = {'key_1': ['value_a']}
        d2 = {'key_2': ['value_b']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a'], 'key_2': ['value_b']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #7 - (one column and another vlaue)")

    def test_both_one_more_value(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': ['value_e', 'value_f', 'value_g'],
              'key_4': ['value_h', 'value_i', 'value_j']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_a',
                                   'value_b', 'value_b', 'value_b'],
                         'key_2': ['value_c', 'value_c', 'value_c',
                                   'value_d', 'value_d', 'value_d'],
                         'key_3': ['value_e', 'value_f', 'value_g',
                                   'value_e', 'value_f', 'value_g'],
                         'key_4': ['value_h', 'value_i', 'value_j',
                                   'value_h', 'value_i', 'value_j']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #8 - (one more value for both)")

    def test_cartesian_product_twice_both_equal_sized_dicts(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': ['value_e', 'value_f'], 'key_4': ['value_g', 'value_h']}
        d3 = {'key_5': ['value_i', 'value_j'], 'key_6': ['value_k', 'value_l']}
        t1 = Table()
        t2 = Table()
        t3 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        t3.set_dict(d3)
        first_CP_table = squeal.cartesian_product(t1, t2)
        result_table = squeal.cartesian_product(first_CP_table, t3)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_a', 'value_a',
                                   'value_b', 'value_b', 'value_b', 'value_b'],
                         'key_2': ['value_c', 'value_c', 'value_c', 'value_c',
                                   'value_d', 'value_d', 'value_d', 'value_d'],
                         'key_3': ['value_e', 'value_e', 'value_f', 'value_f',
                                   'value_e', 'value_e', 'value_f', 'value_f'],
                         'key_4': ['value_g', 'value_g', 'value_h', 'value_h',
                                   'value_g', 'value_g', 'value_h', 'value_h'],
                         'key_5': ['value_i', 'value_j', 'value_i', 'value_j',
                                   'value_i', 'value_j', 'value_i', 'value_j'],
                         'key_6': ['value_k', 'value_l', 'value_k', 'value_l',
                                   'value_k', 'value_l', 'value_k', 'value_l']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #9 - (dicts equal size)")

    def test_both_one_more_key_and_one_more_value(self):
        d1 = {'key_1': ['value_a', 'value_b'], 'key_2': ['value_c', 'value_d']}
        d2 = {'key_3': ['value_e', 'value_f', 'value_g'],
              'key_4': ['value_h', 'value_i', 'value_j'],
              'key_5': ['value_l', 'value_m', 'value_n']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'key_1': ['value_a', 'value_a', 'value_a',
                                   'value_b', 'value_b', 'value_b'],
                         'key_2': ['value_c', 'value_c', 'value_c',
                                   'value_d', 'value_d', 'value_d'],
                         'key_3': ['value_e', 'value_f', 'value_g',
                                   'value_e', 'value_f', 'value_g'],
                         'key_4': ['value_h', 'value_i', 'value_j',
                                   'value_h', 'value_i', 'value_j'],
                         'key_5': ['value_l', 'value_m', 'value_n',
                                   'value_l', 'value_m', 'value_n']}
        self.assertEqual(result_dict, expected_dict, "Failed Cartesian Product\
        Test #10 - (2 values for first dict , 3 values for second dict)")

if __name__ == '__main__':
    unittest.main(exit=False)
