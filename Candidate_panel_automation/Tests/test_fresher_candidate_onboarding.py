import pytest
import unittest
from Pages.fresher_candidate_onboard import FresherCandidateOnboardingFlow
import time

@pytest.mark.usefixtures('classLevelSetUp')
class TestFresherCandidateOnboarding(unittest.TestCase):
    @pytest.fixture(autouse='True')
    def classSetUp(self,classLevelSetUp):
        self.fco = FresherCandidateOnboardingFlow(self.driver)

    def test_candid_onboard(self, mobile='9538596331', otp='495004', email='kavya.b@workex.xyz', password='', from_date="Jan 15,2019"):
         self.fco.onboarding_flow(mobile, otp, email, password)
         self.fco.previous_work_exp_skills(from_date)