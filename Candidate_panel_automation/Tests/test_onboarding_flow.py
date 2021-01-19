import pytest
import unittest
from Pages.candidate_onboarding_flow import  CandidateOnboardingFlow
import time

@pytest.mark.usefixtures('classLevelSetUp')
class Test_Candidate_Onboarding(unittest.TestCase):
    @pytest.fixture(autouse='True')
    def classSetUp(self,classLevelSetUp):
        self.cof=CandidateOnboardingFlow(self.driver)

    def test_candid_onboard(self, mobile='9538596331', otp='495004'):

        self.cof.enterMobileNo(mobile)
        time.sleep(2)
        self.cof.enterOTP(otp)
        self.cof.selectEmail()