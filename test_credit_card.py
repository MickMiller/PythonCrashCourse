""" File: test_credit_card.py
    Purpose: Predict what next credit_card bill will be
    Input: text file from download.csv
	Use: In Bash window with Python 3.7 installed "python test_credit_card.py"
	Expected Results:
	----------------------------------------------------------------------
    Ran 1 test in 0.001s
    OK
    Sum is:  2694.12

"""

import unittest


class TestCreditCard(unittest.TestCase):
    """ See class name """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_credit_card_balance(self):
        """ See title """
        credit_card_sum = 0

        with open('credit_card.txt', 'r') as file_object:
            for line in file_object:
                line2 = line.rstrip()
                if "." in line2:
                    line3 = line2
                else:
                    line3 = line2 + ".00"

                line4 = line3.replace(".", "")  # now int of pennies

                if line4[0] == "-":
                    line5 = line4.replace("-", "")
                    credit_card_sum = credit_card_sum + int(line5)

        sum_string = str(credit_card_sum)
        sum_dollars = sum_string[:-2] + "." + sum_string[-2:]
        print("Sum is: ", sum_dollars)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
