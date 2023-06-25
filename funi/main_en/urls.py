from django.urls import path

from .views import (
    HomePageView,
    SearchPageView,
    AboutUsPageView,
    PricingPageView,
    FAQPageView,
    AskQuestionPageView,
    UniversityPageView,
    ThanksForEmailPageView,

)

from .account.views import (
    SignUp1View,
    SignUp2View,
    SignUp3View,
    AccountIsCreatedView,
    LogoutView,
    AccountView
)

account = [
    path('signup-1/', SignUp1View.as_view(), name='signup_1'),
    path('signup-2/', SignUp2View.as_view(), name='signup_2'),
    path('signup-3/', SignUp3View.as_view(), name='signup_3'),
    path('account-is-created/', AccountIsCreatedView.as_view(), name='account_is_created'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account')
]

urlpatterns = [
                  path('', HomePageView.as_view(), name='home'),
                  path('search/', SearchPageView.as_view(), name='search_page'),
                  path('about-us/', AboutUsPageView.as_view(), name='about_us'),
                  path('pricing/', PricingPageView.as_view(), name='pricing'),
                  path('faq/', FAQPageView.as_view(), name='faq'),
                  path('ask-question/', AskQuestionPageView.as_view(), name='ask_question'),
                  path('thanks-for-question/', ThanksForEmailPageView.as_view(), name='thanks_for_question'),
                  path('university/<slug:slug>/', UniversityPageView.as_view(), name='university'),
                  path('account/', AccountView.as_view(), name='account'),
              ] + account
