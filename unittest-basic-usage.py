# -*- coding: utf-8 -*-
import unittest

class FilaEmpty(Exception):

    def __init__(self, message):
        self.message = message


class Fila(object):

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        self._data = list(args)

    def enter(self, value):
        self._data.append(value)

    def exit(self):
        try:
            self._data.pop()
        except IndexError:
            raise FilaEmpty("Impossible remove value in fila empty")

    def __eq__(self, other):
        if isinstance(other, list):
            return self._data == other
        return False

    def __repr__(self):
        return repr(self._data)



class TestFila(unittest.TestCase):

    def test_initialize_fila_with_list_of_args(self):
        fila = Fila(1, 2, 3)
        self.assertEqual(fila, [1, 2, 3])

    def test_initialize_fila_with_list(self):
        fila = Fila([1, 2, 3])
        self.assertEqual(fila, [1, 2, 3])

    def test_representation_of_fila(self):
        fila = Fila([1, 2, 3])
        self.assertEqual(repr(fila), "[1, 2, 3]")

    def test_append_value_in_fila(self):
        fila = Fila()
        fila.enter(1)
        self.assertEqual(fila, [1])

    def test_remove_value_in_end_fila(self):
        fila = Fila(1, 2, 3)
        fila.exit()
        self.assertEqual(fila, [1, 2])

    def test_error_with_try_remove_item_in_empty_fila(self):
        fila = Fila()
        with self.assertRaises(FilaEmpty):
            fila.exit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

