from lib.lib import PageObject
from configure import DROP_DOWN
import unittest
import re


class Testcases(unittest.TestCase):

    def setUp(self):
        self.pages = PageObject()
        self.pass_count = 0

    def test_header(self):
        """
        Verify the header content
        :return:
        """
        try:
            header = "Cyber attack completely fake statistics"
            self.assertEqual(self.pages.waitforelement("//*[@id='app']/h1", "xpath").text, header,
                             "Header not Matching")
        except AssertionError as e:
            self.fail('AssertionError raised')
        except Exception as e:
            self.fail('unexpected {} exception raised'.format(e))

    def test_filter_sort(self):
        """
        Verifying Filter data and sort data label present or not
        Verifying Filter data and sort data textbox and dropdown present or not
        :return:
        """
        try:
            self.assertEqual(self.pages.waitforelement("//*[@id='app']/div[1]/label", "xpath").text, "Filter data", "LABEL not Matching")
            self.pages.waitforelement("filter-input", id)

            self.assertEqual(self.pages.waitforelement('//*[@id="app"]/div[2]/label', "xpath").text, "Sort data", "LABEL not Matching")
            self.pages.waitforelement("sort-select", id)
        except AssertionError as e:
            self.fail('AssertionError raised')
        except Exception as e:
            self.fail('unexpected {} exception raised'.format(e))

    def test_header(self):
        """

        :return:
        """
        column_arr = []

        headers = self.pages.getElements("header__item", "class")
        header_count = len(headers)

        selected = self.pages.get_dropdown("sort-select", "id")

        table = self.pages.getElement("table", "class")
        table_content = table.find_element_by_class_name("table-content")
        rows = table_content.find_elements_by_class_name("table-row")
        # if DROP_DOWN[selected]
        count = 0

        column = DROP_DOWN[selected]
        for j in range(1, len(rows)+1):
            print("value of j = {} and column = {}".format(j, column))
            col = rows[count].find_element_by_xpath("//*[@id='app']/div[3]/div[2]/div[{}]/div[{}]".format(j, column))
            if re.match(r'^[0-9]*[k, K]$', col.text):
                print("col k= {}".format(int(col.text[0:-1])*1000))
                column_arr.append(int(col.text[0:-1])*1000)
                count += 1

            elif re.match(r'^[0-9]*\.?[0-9]*[k, K]$', col.text):
                print("col float k = {}".format(float(col.text)*1000))
                column_arr.append(float(col.text[0:-1])*1000)
                count += 1

            elif re.match(r'^[0-9]*[m, M]$', col.text):
                print("col m= {}".format(int(col.text[0:-1])*1000000))
                column_arr.append(int(col.text[0:-1])*1000000)
                count += 1

            elif re.match(r'^[0-9]*\.?[0-9]*[m, M]$', col.text):
                print("col float m = {}".format(float(col.text[0:-1])*1000000))
                column_arr.append(float(col.text[0:-1])*1000000)
                count += 1

            elif re.match(r'^[0-9]*[b, B]$', col.text):
                print("col b= {}".format(int(col.text[0:-1])*1000000))
                column_arr.append(int(col.text[0:-1]) * 1000000000)
                count += 1

            elif re.match(r'^[0-9]*\.?[0-9]*[b, B]$', col.text):
                print("col float b = {}".format(float(col.text[0:-1])*1000000))
                column_arr.append(float(col.text[0:-1]) * 1000000000)
                count += 1

            else:
                column_arr.append(int(col.text))
                count += 1

        print(column_arr)
        count = 0
        l = sorted(column_arr)
        for i in range(len(l)):
            if type(l[i]) == type(column_arr[i]):
                if column_arr[i] == l[i]:
                    count += 1
            else:
                if 'k' == column_arr[i][-1].lower() or 'K' == column_arr[i][-1].lower():
                    if type(column_arr[i][0:-1]) == int:
                        if column_arr[i]*1000 == l[i]:
                            count += 1
                    elif type(column_arr[i][0:-1]) == float:
                        if column_arr[i]*1000 == l[i]:
                            count += 1
                elif 'm' == column_arr[i][-1].lower() or 'M' == column_arr[i][-1].lower():
                    if type(column_arr[i][0:-1]) == int:
                        if column_arr[i]*1000000 == l[i]:
                            count += 1
                    elif type(column_arr[i][0:-1]) == float:
                        if column_arr[i]*1000000 == l[i]:
                            count += 1
                elif 'b' == column_arr[i][-1].lower() or 'B' == column_arr[i][-1].lower():
                    if type(column_arr[i][0:-1]) == int:
                        if column_arr[i]*1000000000 == l[i]:
                            count += 1
                    elif type(column_arr[i][0:-1]) == float:
                        if column_arr[i]*1000000000 == l[i]:
                            count += 1
        if len(l) == count:
            print("Combination of sorting and filtering works correctly.")
        else:
            print("Combination of sorting and filtering not works correctly, count = {} l = {}".format(count, l))


if __name__ == '__main__':
    unittest.main()

