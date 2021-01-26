from  Base.selenium_driver import  SeleniumDriver
import time
class CandidateOnboardingFlow(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    xpath_mob_no_field="//input[@formcontrolname='mobile_no']"
    xpath_otp_field="//input[@formcontrolname='otp']"
    xpath_email_selection="//input[@id='identifierId']"
    xpath_nxt_btn="//*[@id='identifierNext']/div/button/div[2]"
    xpath_email_password_field="//input[@type='password']"
    xpath_password_nxt_btn="//div[@id='passwordNext']/div/button/div[2]"
    xpath_gender="//nb-radio-group/nb-radio[2]/label/span[2]"
    xpath_next_1="//button[@tabindex='0' and contains(text(), 'Next')]"
    xpath_Experienced="//div/div[2]/div[2]/div[2]/span[contains(text(), 'Experienced')]"
    xpath_next2="//button[@tabindex='0' and contains(text(), 'Next')]"
    xpath_work_exp="//div/div[2]/div[1]/nb-select/button"
    xpath_select_exp='//div[@id="cdk-overlay-1"]/div/ul/nb-option[1]'
    xpath_qualification_field="//div/div[2]/div[2]/nb-select/button"
    xpath_qualification="//div[@id='cdk-overlay-2']/div/ul/nb-option[3]"
    xpath_location_field="//ngx-location/div/div/div/input"
    xpath_select_location="//ngx-location/div[2]/nb-card/nb-list/nb-list-item[1]"
    xpath_job_category="//div/div[2]/ngx-wx-dropdown/div"
    xpath_select_category="//ng-dropdown-panel/div/div/div[2]/span"
    xpath_job_specialization_field="//ngx-experience-profile/div/div[3]//ngx-wx-dropdown/div/ng-select"
    xpath_job_specialization="//ng-dropdown-panel/div/div/div[1]"
    xpath_role_field="//ngx-experience-profile/div/div[4]/ngx-wx-dropdown/div/ng-select"
    xpath_role_selection="//ng-dropdown-panel/div/div/div[1]/span"
    xpath_company_field="(//ngx-wx-dropdown/div/ng-select/div/div/div[2]/input)[1]"
    xpath_company="//ng-dropdown-panel/div/div/div[1]/span"
    xpath_cwh_checkbox="//nb-checkbox/label/span[2]"
    xpath_from_date="//ngx-experience-profile/div/div[8]/div/input"
    xpath_min_sal_field="//ngx-experience-profile/div/div[9]/div"
    xpath_select_sal="//ng-dropdown-panel/div/div/div[3]"
    xpath_notice_period="//ngx-new-add-edit-chip/div/div[1]"
    xpath_skill1="//ngx-new-add-edit-chip/div/div[1]"
    xpath_skill2="//ngx-new-add-edit-chip/div/div[2]"
    xpath_skill3 = "//ngx-new-add-edit-chip/div/div[3]"
    xpath_skill4 = "//ngx-new-add-edit-chip/div/div[4]"
    xpath_skill5 = "//ngx-new-add-edit-chip/div/div[5]"

    def enterMobileNo(self, mobile):
        self.sendKeys(mobile,self.xpath_mob_no_field, locatorType='xpath')
        self.pressEnter(self.xpath_mob_no_field, locatorType='xpath')
    def enterOTP(self, otp):
        self.sendKeys(otp,self.xpath_otp_field, locatorType='xpath' )
        self.pressEnter(self.xpath_otp_field, locatorType='xpath')
    def enterEmail(self, email, password):
        before_window = self.driver.current_window_handle
        self.log.info(before_window)

        handles = self.driver.window_handles

        for handle in handles:
            self.log.info("inside for loop")
            if handle not in  before_window:
                self.log.info(handle)
                after_window = handle
                time.sleep(2)
                self.driver.switch_to.window(after_window)

                self.log.info("switched window")
                self.sendKeys(email,self.xpath_email_selection, locatorType='xpath')
                time.sleep(2)
                self.elementClick(self.xpath_nxt_btn, locatorType='xpath')
                time.sleep(2)
                self.sendKeys(password, self.xpath_email_password_field, locatorType='xpath')
                self.elementClick(self.xpath_password_nxt_btn, locatorType='xpath')
                time.sleep(2)
        self.driver.switch_to.window(before_window)
        time.sleep(2)
    def select_gender(self):
        self.elementClick(self.xpath_gender, locatorType='xpath')
        time.sleep(2)

    def click_next1(self):
        # time.sleep(2)

        self.elementClick(self.xpath_next_1, locatorType='xpath')
        # self.elementClick(self.xpath_nxt_btn, locatorType='xpath')
    def select_experience(self):
        self.elementClick(self.xpath_Experienced, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_work_exp, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_exp, locatorType='xpath')
    def select_qualification(self):
        self.elementClick(self.xpath_qualification_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_qualification, locatorType='xpath')

    def select_location(self):
        self.sendKeys("j", self.xpath_location_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_location, locatorType='xpath')

    def click_next2(self):
        self.elementClick(self.xpath_next2, locatorType='xpath')

    def select_work_exp_details(self, from_date):
        self.elementClick(self.xpath_job_category, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_select_category, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_job_specialization_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_job_specialization, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_role_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_role_selection, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_company_field, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_company, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_cwh_checkbox, locatorType='xpath')
        time.sleep(6)
        self.sendKeys(from_date, self.xpath_from_date, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_min_sal_field, locatorType='xpath')
        self.elementClick(self.xpath_select_sal, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.xpath_notice_period, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.xpath_next2, locatorType='xpath')
        time.sleep(3)
    def select_skills(self):
        self.elementClick(self.xpath_skill1, locatorType='xpath')
        self.elementClick(self.xpath_skill2, locatorType='xpath')
        self.elementClick(self.xpath_skill3, locatorType='xpath')
        self.elementClick(self.xpath_skill4, locatorType='xpath')
        self.elementClick(self.xpath_skill5, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.xpath_next2, locatorType='xpath')
        time.sleep(4)



    def onboarding_flow(self, mobile, otp, email, password):
        self.enterMobileNo(mobile)
        time.sleep(6)
        self.enterOTP(otp)
        time.sleep(8)
        self.enterEmail(email, password)
        time.sleep(3)
        self.select_gender()
        time.sleep(5)
        self.click_next1()
        time.sleep(3)
        self.select_experience()
        time.sleep(3)
        self.select_qualification()
        time.sleep(3)
        self.select_location()
        time.sleep(3)
        self.click_next2()
        time.sleep(3)

    def previous_work_exp_skills(self, from_date):
        self.select_work_exp_details(from_date)
        self.select_skills()




