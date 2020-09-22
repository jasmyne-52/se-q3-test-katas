import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(1, 1), 2)
        self.assertEqual(katas.add(1, -1), 0)
        self.assertEqual(katas.add(0, -1), -1)

    def test_multiply(self):
        self.assertEqual(katas.multiply(1, 1), 1)
        self.assertEqual(katas.multiply(1, -1), -1)
        self.assertEqual(katas.multiply(0, -1), 0)

    def test_power(self):
        self.assertEqual(katas.power(1, 1), 1)
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(0, 1), 0)


    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
