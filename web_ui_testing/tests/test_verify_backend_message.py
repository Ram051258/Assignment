from tests import BaseClass
from locator.frontend_page_locator import *
from selenium.webdriver.common.keys import Keys

class TestBackEndIntegration(BaseClass):
    def test_verify_backend_message(self):
        backend_message = "Hello from the Backend!"

        ''' Backend testing started. '''
        #Instantiating the logger
        self.log().info("Backend testing started")

        # Opening hosted application using fronted service url 
        self.driver.get("http://192.168.59.100:30406/")

        # Verifying if the h1 element is displayed
        assert self.get_element(VERIFY_BACKEND).is_displayed()

        # Fetching the message coming from the backend as output to frontend page.
        output_text=self.get_element(VERIFY_BACKEND).text

        # Verifying if the backend message fetched is correctly displayed
        assert backend_message == output_text
        self.log().info(output_text)
        
        # logging the test success
        self.log().info("Successfully verified backend message")


        
        

    


