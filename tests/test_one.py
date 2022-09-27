import unittest
from main import *
from parameterized import parameterized
from mock import patch


class TestOne(unittest.TestCase):
    @parameterized.expand(
        [
            ("2207 876234", "Василий Гупкин"),
            ("10006", "Аристарх Павлов")
        ]
    )
    @patch('builtins.input')
    def test_get_doc_owner_name(self, doc, name, inp):
        inp.return_value = doc
        self.assertEqual(get_doc_owner_name(), name)

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        etalon = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        self.assertEqual(etalon, result)

    def test_show_document_info(self):
        self.assertEqual('passport "2207 876234" "Василий Гупкин"', show_document_info(documents[0]))

    @patch('builtins.input')
    def test_delete_doc(self, inp):
        inp.return_value = "10006"
        self.assertEqual(('10006', True), delete_doc())

    @patch('builtins.input')
    def test_add_new_doc(self, inp):
        inp.return_value = 'p'
        inp.return_value = "passport"
        inp.return_value = "passport"
        inp.return_value = "1"
        self.assertEqual(add_new_doc(), '1')
