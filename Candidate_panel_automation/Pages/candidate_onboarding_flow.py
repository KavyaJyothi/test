from  Base.selenium_driver import  SeleniumDriver

class CandidateOnboardingFlow(SeleniumDriver):
    def __init__(self, driver):
        self.driver=driver

    xpath_mob_no_field="//input[@formcontrolname='mobile_no']"
    xpath_otp_field="//input[@formcontrolname='otp']"
    xpath_email_selection="//div/div/div[@data-email='kavya.b@workex.xyz']"


    def enterMobileNo(self, mobile):
        self.sendKeys(mobile,self.xpath_mob_no_field, locatorType='xpath')
    def enterOTP(self, otp):
        self.sendKeys(otp,self.xpath_otp_field, locatorType='xpath' )
    def selectEmail(self):
        self.elementClick(self.xpath_email_selection, locatorType='xpath')