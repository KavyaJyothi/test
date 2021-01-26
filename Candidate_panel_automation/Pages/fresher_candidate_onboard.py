from  Base.selenium_driver import  SeleniumDriver
import time
class FresherCandidateOnboardingFlow(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_mob_no_field ="//input[@formcontrolname='mobile_no']"
    xpath_otp_field="//input[@formcontrolname='otp']"
    xpath_email_selection="//input[@id='identifierId']"
    xpath_nxt_btn="//*[@id='identifierNext']/div/button/div[2]"
    xpath_email_password_field="//input[@type='password']"
    xpath_password_nxt_btn="//div[@id='passwordNext']/div/button/div[2]"
    xpath_gender="//nb-radio-group/nb-radio[2]/label/span[2]"
    xpath_next_1="//button[@tabindex='0' and contains(text(), 'Next')]"
    xpath_select_exp_state="//ngx-work-status-profile/div/div[2]/div[1]/div[2]/span"
    xpath_qualification="(//nb-select/button)[1]"
    xpath_select_qualification="//div[@id='cdk-overlay-2']/div/ul/nb-option[3]"
    xpath_location_field="//ngx-location/div/div/div/input"
    xpath_select_location="//nb-card/nb-list/nb-list-item[1]/div[1]/b"
    xpath_job_category_field="(//ng-select/div/div/div[2]/input)[1]"
    xpath_select_category="//ng-dropdown-panel/div/div/div[4]/span"
    xpath_specification_field="//ng-select/div/div/div[2]/input"
    xpath_select_specification="//ng-dropdown-panel/div/div/div[1]/span"
    xpath_expected_salary_field="(//nb-select/button)[2]"
    xpath_select_sal="//div[@id='cdk-overlay-3']/div/ul/nb-option[3]"
    xpath_nxt2="//div/div[3]/button[2]"
