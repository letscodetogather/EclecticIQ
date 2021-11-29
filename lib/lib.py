from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from configure import URL, Chrome_DRIVER, SELECRTED_DROP_DOWN, SORT_SELECT, ID, XPATH, LINK_TEXT, CLASS
from selenium.webdriver.support.select import Select



class PageObject:

    def __init__(self):
        self.locator = None
        self.driver = webdriver.Chrome(Chrome_DRIVER)
        self.driver.get(url=URL)
        print(self.driver)

    def get_title(self):
        return self.driver.title

    def getByType(self, locatorType):
        if locatorType == ID:
            return By.ID
        elif locatorType == XPATH:
            return By.XPATH
        elif locatorType == LINK_TEXT:
            return By.LINK_TEXT
        elif locatorType == CLASS:
            return By.CLASS_NAME

    def waitforelement(self, locator, locator_type="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locator_type)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
        except ElementNotVisibleException as e:
            print(e)
        except Exception as e:
            print(e)
        return element

    def getElement(self, locator, locatortype=""):
        element = None
        try:
            locator_type = locatortype.lower()
            byType = self.getByType(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: ", locator, " and locatorType: ", locatortype)
        except ElementNotVisibleException as e:
            self.log.info("Element not found with locator: ", locator, " and  locatorType: ", locatortype)
        except Exception as e:
            print(e)

        return element

    def getElements(self, locator, locatortype=""):
        elements = None
        try:
            locator_type = locatortype.lower()
            byType = self.getByType(locator_type)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element Found with locator: ", locator, " and locatorType: ", locatortype)
        except ElementNotVisibleException as e:
            self.log.info("Element not found with locator: ", locator, " and  locatorType: ", locatortype)
        except Exception as e:
            print(e)

        return elements

    def get_dropdown(self, locator, locatortype=""):
        # get selected item
        s = Select(self.getElement(SORT_SELECT, ID))
        s.select_by_visible_text(SELECRTED_DROP_DOWN)
        selected_option = s.first_selected_option
        return selected_option.text




