import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = Runner('Kate')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner('Vadim')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run_1 = Runner('Elena')
        run_2 = Runner('Leo')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)

if __name__ == '__main__':
    unittest.main()