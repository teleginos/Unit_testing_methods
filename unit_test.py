import unittest
from main import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усэйн', 10)
        self.runner_andrei = Runner('Андрей', 9)
        self.runner_nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for key, value in cls.all_results.items():
            print(f"{key}: {{", end="")
            print(", ".join([f"{place}: {runner.name}" for place, runner in value.items()]), end="")
            print("}")

    def test_usain_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results['Усэйн и Ник'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrei_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results['Андрей и Ник'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results['Усэйн, Андрей и Ник'] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_close_speed(self):
        runner1 = Runner('Runner1', 10)
        runner2 = Runner('Runner2', 9.9)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.__class__.all_results['Close Speed'] = results
        self.assertTrue(results[1] == 'Runner1')
        self.assertTrue(results[2] == 'Runner2')

    def test_equal_speed(self):
        runner1 = Runner('Runner1', 10)
        runner2 = Runner('Runner2', 10)
        tournament = Tournament(1000, runner1, runner2)
        results = tournament.start()
        self.__class__.all_results['Equal Speed'] = results
        self.assertTrue(results[1] == 'Runner1' or results[1] == 'Runner2')
        self.assertTrue(results[2] == 'Runner1' or results[2] == 'Runner2')


if __name__ == '__main__':
    unittest.main()
