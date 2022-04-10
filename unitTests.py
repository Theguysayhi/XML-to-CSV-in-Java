import unittest
from CSVextractor import XmlManager as XM

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.xmlfile = 'Testfiles/testfile.xml'
        with open('Testfiles/12345678901.csv') as f:
            self.csvfile1 = f.read()
            f.close()
        with open('Testfiles/98765432109.csv') as f:
            self.csvfile2 = f.read()
            f.close()

    def test_matchesOutput(self):
        self.assertEqual(self.csvfile1, XM().tostring(self.xmlfile, 0))
        self.assertEqual(self.csvfile2, XM().tostring(self.xmlfile, 1))

    # def test_incorrectStartFormat(self):
    #     self.assertEqual(True, False)
    #
    # def test_incorrectEndFormat(self):
    #     self.assertEqual(True, False)
    #
    # def test_whitespacesAndTabs(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
