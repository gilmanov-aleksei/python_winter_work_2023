#! /usr/bin/python
#
# import unittest
#
#
# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#     def test_concatenation(self):
#         self.assertEqual('fuzz' + 'dizz', 'fuzzdizz')
#
#     def test_multiplay(self):
#         self.assertEqual('fuzz' * 3, 'fuzzfuzzfuzz')
#
#
# if __name__ == '__main__':
#     unittest.main


import unittest


def cube_area(side):
    return 6 * side ** 2

class TestCubeArea(unittest.TestCase):
    def test_cube_area(self):
        self.assertEqual(cube_area(3), 54)
        self.assertEqual((0), 0)

    # def test_value(self):
    #     self.assertRaises(ValueError, cube_area, -1)

    def test_type(self):
        self.assertRaises(TypeError, cube_area, 'String')
        # self.assertRaises(TypeError, cube_area, True)
        self.assertRaises(TypeError, cube_area, [0])
        self.assertRaises(TypeError, cube_area, (1, 2))
        self.assertRaises(TypeError, cube_area, {})


if __name__ == '__main__':
    unittest.main
