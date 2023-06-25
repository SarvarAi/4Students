from django.test import TestCase
from django.urls import reverse, resolve

from ..views import (
    HomePageView,
    SearchPageView,
    AboutUsPageView,
    PricingPageView,
    FAQPageView,
    AskQuestionPageView,
    ThanksForEmailPageView,
    UniversityPageView,
    AccountView
)
from ..account.views import (
    SignUp1View,
    SignUp2View,
    SignUp3View,
    AccountIsCreatedView,
    LogoutView
)


class UrlsTest(TestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_search_page_url(self):
        url = reverse('search_page')
        self.assertEqual(resolve(url).func.view_class, SearchPageView)

    def test_about_us_url(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func.view_class, AboutUsPageView)

    def test_pricing_url(self):
        url = reverse('pricing')
        self.assertEqual(resolve(url).func.view_class, PricingPageView)

    def test_faq_url(self):
        url = reverse('faq')
        self.assertEqual(resolve(url).func.view_class, FAQPageView)

    def test_ask_question_url(self):
        url = reverse('ask_question')
        self.assertEqual(resolve(url).func.view_class, AskQuestionPageView)

    def test_thanks_for_question_url(self):
        url = reverse('thanks_for_question')
        self.assertEqual(resolve(url).func.view_class, ThanksForEmailPageView)

    def test_university_url(self):
        url = reverse('university', args=['example-slug'])
        self.assertEqual(resolve(url).func.view_class, UniversityPageView)

    def test_account_url(self):
        url = reverse('account')
        self.assertEqual(resolve(url).func.view_class, AccountView)

    def test_signup_1_url(self):
        url = reverse('signup_1')
        self.assertEqual(resolve(url).func.view_class, SignUp1View)

    def test_signup_2_url(self):
        url = reverse('signup_2')
        self.assertEqual(resolve(url).func.view_class, SignUp2View)

    def test_signup_3_url(self):
        url = reverse('signup_3')
        self.assertEqual(resolve(url).func.view_class, SignUp3View)

    def test_account_is_created_url(self):
        url = reverse('account_is_created')
        self.assertEqual(resolve(url).func.view_class, AccountIsCreatedView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
