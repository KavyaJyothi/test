import pytest
import unittest
from Pages.candidate_onboarding_flow import  CandidateOnboardingFlow
import time
from  Utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures('classLevelSetUp')
class Test_Candidate_Onboarding(unittest.TestCase):
    @pytest.fixture(autouse='True')
    def classSetUp(self,classLevelSetUp):
        self.cof=CandidateOnboardingFlow(self.driver)
    @data(*read_csv_data("onboard_data.csv"))
    @unpack
    def test_candid_onboard(self, mobile, otp, email, password):
         self.cof.onboarding_flow(mobile, otp, email, password)
         self.cof.experience_detais()
         self.cof.previous_work_exp_skills("Jan 15,2019")

