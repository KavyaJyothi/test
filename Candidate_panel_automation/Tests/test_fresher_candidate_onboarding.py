import pytest
import unittest
from Pages.fresher_candidate_onboard import FresherCandidateOnboardingFlow
import time
from  Utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures('classLevelSetUp')
class TestFresherCandidateOnboarding(unittest.TestCase):
    @pytest.fixture(autouse='True')
    def classSetUp(self,classLevelSetUp):
        self.fco = FresherCandidateOnboardingFlow(self.driver)

    @data(*read_csv_data("onboard_data.csv"))
    @unpack
    def test_candid_onboard(self, mobile_no, otp, email, password):
         self.fco.initial_onboarding_flow( mobile_no, otp, email, password)
         self.fco.fresher_ondoarding_flow()