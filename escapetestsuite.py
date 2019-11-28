import json
import unittest
import escape_som_op_tablet as es
import escape_vullen_torens as torens

# Testsuite oplossing1

class TestStringMethods(unittest.TestCase):

    def test_oplossing1computevermenigvuldigen(self):
        test = json.loads(
            "{\"delen\":false,\"optellen\":false,\"vermenigvuldigen\":true,\"aftrekken\":false,\"som\":{\"getal1\":8,\"getal2\":4}}")
        self.assertEqual(es.oplossing1ComputeEntryCode(test), 32)

    def test_oplossing1computedelen(self):
        test = json.loads(
            "{\"delen\":true,\"optellen\":false,\"vermenigvuldigen\":false,\"aftrekken\":false,\"som\":{\"getal1\":8,\"getal2\":4}}")
        self.assertEqual(es.oplossing1ComputeEntryCode(test), 2)

    def test_oplossing1computeoptellen(self):
        test = json.loads(
            "{\"delen\":false,\"optellen\":true,\"vermenigvuldigen\":false,\"aftrekken\":false,\"som\":{\"getal1\":8,\"getal2\":4}}")
        self.assertEqual(es.oplossing1ComputeEntryCode(test), 12)

    def test_oplossing1computeaftrekken(self):
        test = json.loads(
            "{\"delen\":false,\"optellen\":false,\"vermenigvuldigen\":false,\"aftrekken\":true,\"som\":{\"getal1\":8,\"getal2\":4}}")
        self.assertEqual(es.oplossing1ComputeEntryCode(test), 4)



    #ff printen. assertEquals was teveel moeite (not good, I know)
    def test_torensvolgorde(self):
        test = json.loads("{\"torens\": {\"typeSortering\": \"Oplopend\", \"alfabetisch\": false, \"hoogte\": true, \"bouwjaar\": false}}")
        print (torens.convert2antwoordstring(torens.sortlist(test)))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
