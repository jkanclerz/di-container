import os
import unittest
from container import Container 

class Foo:
    def __init__(self, bar):
        self.__bar = bar

    def bar(self):
        return self.__bar

class Bar:
    def __init__(self):
        return

def createBar(container):
    return Bar()

def createFoo(container):
    foo = Foo(container.get('bar'))
    return foo

class TestCase(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def tearDown(self):
        return

    def test_register_plain_data(self):
        self.container.register('my_data', 'my_data_value')

        assert 'my_data_value' in self.container.get('my_data')

    def test_register_object(self):
        self.container.register('my_object', Bar())

        self.assertIsInstance(self.container.get('my_object'), Bar)

    def test_register_lazy_object(self):
        self.container.register('my_lazy_object', createBar)

        self.assertIsInstance(self.container.get('my_lazy_object'), Bar)

    def test_register_lazy_object_with_dependencies(self):
        self.container.register('bar', createBar)
        self.container.register('my_lazy_object', createFoo)
        foo = self.container.get('my_lazy_object')

        self.assertIsInstance(foo, Foo)
        self.assertIsInstance(foo.bar(), Bar)

if __name__ == '__main__':
    unittest.main()