import unittest
import tests_12_3

# part one
fileTS =  unittest.TestSuite()
fileTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
fileTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(fileTS)


