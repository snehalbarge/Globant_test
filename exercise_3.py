import unittest

def validator(*datatypes):
    def validate_func(function):
        assert len(datatypes) == function.__code__.co_argcount

        def updated_function(*args, **kwargs):
            for (a, t) in zip(args, datatypes):
                assert isinstance(a, t), "parameters %r does not match %s" % (a, t)
            return function(*args, **kwargs)
        updated_function.__name__ = function.__name__
        return updated_function
    return validate_func


class TestValidator(unittest.TestCase):
    def test_validator(self):
        var1 = 1
        var2 = 2
        var3 = 3

        @validator(int, int, str)
        def f(a, b, c):
            pass

        self.assertRaises(AssertionError, f, var1, var2, var3)


if __name__ == "__main__":
    unittest.main()
