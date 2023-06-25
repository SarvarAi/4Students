from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .models import University, FAQ
from .forms import FAQForm, AuthenticationForm


# Create your views here.

class HomePageView(FormView):
    template_name = 'main_en/index.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Home'
    }

    def dispatch(self, request, *args, **kwargs):
        # Check if 'form_data_1' exists in the session
        if 'form_data_1' in self.request.session:
            # If it exists, delete 'form_data_1' from the session
            del self.request.session['form_data_1']

        # Check if 'form_data_2' exists in the session
        if 'form_data_2' in self.request.session:
            # If it exists, delete 'form_data_2' from the session
            del self.request.session['form_data_2']

        # Continue with the regular dispatch process
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']  # Email entered in the username field
        password = form.cleaned_data['password']
        user = authenticate(request=self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

        form.add_error(None, 'Invalid email or password.')
        return self.form_invalid(form)

    def form_invalid(self, form):
        print('Invalid')
        for field in form.errors:
            print(f'Field is {field}, Error is {form.errors[field].as_text()}')
        return super().form_invalid(form)


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



