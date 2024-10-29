import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


"""
Tests class Runner
    """

# class RunnerTest(unittest.TestCase):
#     def test_walk(self):
#         run = Runner('Kate')
#         for i in range(10):
#             run.walk()
#         self.assertEqual(run.distance, 50)
#
#     def test_run(self):
#         run = Runner('Vadim')
#         for i in range(10):
#             run.run()
#         self.assertEqual(run.distance, 100)
#
#     def test_challenge(self):
#         run_1 = Runner('Elena')
#         run_2 = Runner('Leo')
#         for i in range(10):
#             run_1.run()
#             run_2.walk()
#         self.assertNotEqual(run_1.distance, run_2.distance)

"""
Test class Tournament
    """


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f'{test_name}:{result}')

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")


if __name__ == '__main__':
    unittest.main()
