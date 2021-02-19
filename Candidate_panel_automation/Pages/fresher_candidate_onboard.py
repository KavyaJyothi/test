from  Base.selenium_driver import  SeleniumDriver
from Pages.candidate_onboarding_flow import CandidateOnboardingFlow
import time
class FresherCandidateOnboardingFlow(CandidateOnboardingFlow):
    def __init__(self, driver):
     self.driver = driver

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
    xpath_qualification_field1="//div[1]/div[2]/div[1]/nb-select/button"
    xpath_select_qualification1="//div[@id='cdk-overlay-1']/div/ul/nb-option[3]"
    xpath_category_field="(//ngx-wx-dropdown/div/ng-select/div/div/div[2]/input)[1]"
    xpath_job_specialization_field1="//ngx-wx-dropdown/div/ng-select/div/div/div[2]/input"
    xpath_select_job_specialization1="//ng-dropdown-panel/div/div/div[1]"
    xpath_expected_salary_field="(//nb-select/button)[2]"
    xpath_select_sal="//div[@id='cdk-overlay-2']/div/ul/nb-option[2]"


    def select_experience(self):
        self.elementClick(self.xpath_select_exp_state, locatorType='xpath')
        self.elementClick(self.xpath_nxt2, locatorType='xpath')
    def select_qualification(self):
        self.elementClick(self.xpath_qualification_field1, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self.xpath_select_qualification1, locatorType='xpath')
    def select_category(self):
        self.elementClick(self.xpath_category_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_category, locatorType='xpath')
    def select_specialization(self):
        self.elementClick(self.xpath_job_specialization_field1, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_job_specialization1, locatorType='xpath')
    def select_expected_sal(self):
        self.elementClick(self.xpath_expected_salary_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_sal, locatorType='xpath')


    def initial_onboarding_flow(self, mobile_no, otp, email, password):
        self.onboarding_flow( mobile_no, otp, email, password)

    def fresher_ondoarding_flow(self):
        self.select_experience()
        self.select_qualification()
        time.sleep(5)
        self.select_location()
        time.sleep(3)
        self.select_category()
        time.sleep(2)
        self.select_specialization()
        time.sleep(2)
        self.select_expected_sal()
        time.sleep(1)
        self.elementClick(self.xpath_nxt2, locatorType='xpath')
        time.sleep(2)
        self.select_skills()
        time.sleep(2)






