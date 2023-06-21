from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib import messages

from .models import University, FAQ
from .forms import FAQForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'main_en/index.html'
    extra_context = {
        'title': 'Home'
    }


class SearchPageView(ListView):
    model = University
    template_name = 'main_en/search.html'
    extra_context = {
        'title': 'Search'
    }
    context_object_name = 'universities'


class AboutUsPageView(TemplateView):
    template_name = 'main_en/about_us.html'
    extra_context = {
        'title': 'About us'
    }


class PricingPageView(TemplateView):
    template_name = 'main_en/pricing.html'
    extra_context = {
        'title': 'Pricing'
    }


class FAQPageView(TemplateView):
    template_name = 'main_en/faq.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'FAQ'
        context['questions'] = FAQ.objects.filter(status=True)
        return context


class SignUpPageView(TemplateView):
    template_name = 'main_en/signup.html'
    extra_context = {
        'title': 'Sign Up'
    }


class AskQuestionPageView(FormView):
    template_name = 'main_en/ask_question.html'
    form_class = FAQForm
    extra_context = {
        'title': 'Ask Question'
    }
    success_url = '/thanks-for-question/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        if 'last_name' in form.errors:
            print(True)
            print(form.errors['last_name'].as_text())

        for field in form.errors:
            messages.error(self.request, form.errors[field].as_text())
        return super().form_invalid(form)


class ThanksForEmailPageView(TemplateView):
    template_name = 'main_en/thanks_for_question.html'
    extra_context = {
        'title': 'Thanks for question'
    }


class ContactUsPageView(TemplateView):
    template_name = 'main_en/contact_us.html'
    extra_context = {
        'title': 'Contact us'
    }


class UniversityPageView(TemplateView):
    template_name = 'main_en/university.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        university = University.objects.get(slug=kwargs['slug'])
        context['title'] = university.title
        context['university'] = university
        return context
