from django.urls import path

from .views import HomePageView, SearchPageView, AboutUsPageView, \
    PricingPageView, FAQPageView, SignUpPageView, AskQuestionPageView, \
    UniversityPageView, ThanksForEmailPageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchPageView.as_view(), name='search_page'),
    path('about-us/', AboutUsPageView.as_view(), name='about_us'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('sign-up/', SignUpPageView.as_view(), name='signup'),
    path('ask-question/', AskQuestionPageView.as_view(), name='ask_question'),
    path('thanks-for-question/', ThanksForEmailPageView.as_view(), name='thanks_for_question'),
    path('university/<slug:slug>/', UniversityPageView.as_view(), name='university'),
)
