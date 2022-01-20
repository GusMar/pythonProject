import unittest
from pathlib import Path
import os

from appium import webdriver


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        # self.dc['app'] = '/bitrise/src/pythonProject/resources/eribank.apk'
        self.dc['app'] = os.environ['BITRISE_SOURCE_DIR'] + '/resources/eribank.apk'
        # self.dc['app'] = os.path.join( str(Path(__file__).parent),'resources', 'eribank.apk')
        # self.dc['app'] = os.path.join(str(Path(__file__).parent), 'resources', 'eribank.apk')
        # "C:\\Users\\gmarin\\PycharmProjects\\FirstPythonAppiumTest\\resources\\eribank.apk"
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capability specify platform detail to Appium
        self.dc['platformName'] = 'Android'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'pixel6'
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_automation(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_element_by_xpath("//*[@text='OK']").click();
        # Find location of Elements and perform action.
        self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        # self.driver.find_element_by_xpath("//*[@text='Login']").click()
        butons = len(self.driver.find_elements_by_xpath("//*[@text='Login']"))
        print("===========  the login button is present " + str(butons) + " times ===========")
        assert len(self.driver.find_elements_by_xpath("//*[@text='Login']")) > 0

    def test_other(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_element_by_xpath("//*[@text='OK']").click();
        # Find location of Elements and perform action.
        self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        # self.driver.find_element_by_xpath("//*[@text='Login']").click()
        butons = len(self.driver.find_elements_by_xpath("//*[@text='Login']"))
        print("===========  second test the other login button is present " + str(butons) + " times ===========")
        assert len(self.driver.find_elements_by_xpath("//*[@text='Login']")) > 0

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
