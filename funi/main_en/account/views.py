from typing import Dict

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import password_validation
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from .forms import Signup1Form, Signup2Form, Signup3Form

from ..models import Account


class SignUp1View(FormView):
    """
    Registration form consists from 3 small forms in 3 different web pages.
    So this is first page, and it's first form.
    """
    template_name = 'main_en/signup1.html'
    extra_context = {
        'title': 'Sign Up'
    }
    form_class = Signup1Form  # form for the first signup page

    def get_initial(self) -> Dict[str, str]:
        """
        In this method, we are checking if the user first time visiting this page
        since if he goes back from second form to the first form
        all his data that he saved in first form needs to be showed
        :return: initial is dictionary that contains form1 data
        """
        initial = super().get_initial()
        form_data_1 = self.request.session.get('form_data_1')

        if form_data_1:  # checking if form_data_1 is empty
            initial['first_name'] = form_data_1.get('first_name')
            initial['last_name'] = form_data_1.get('last_name')
            initial['middle_name'] = form_data_1.get('middle_name')
        return initial

    def get_success_url(self) -> str:
        """
        If the data in the form is validated next
        we can go to the next (second) form,
        so this method brings us next url
        :return: reverse('signup_2') it is url to the second form
        """
        return reverse('signup_2')

    def form_valid(self, form: Signup1Form) -> HttpResponseRedirect:
        """
        form_valid method checks if the form is valid
        for our database, if it is not we can't proceed
        next step
        :param form: it is an object of Signup1Form which contains
        all necessary information of form
        :return: Redirect us to the next step, actually we
        are inheriting it
        """

        # saving the data into the session in order to use it
        # after user fills all three forms
        self.request.session['form_data_1'] = form.cleaned_data
        return super().form_valid(form)

    def form_invalid(self, form: Signup1Form) -> HttpResponseRedirect:
        """
        If the user form is not valid, user stays in the same page
        with same form
        :param form: it is an object of Signup1Form which contains
        all necessary information of form
        :return: Redirect us to the next step, actually we
        are inheriting it
        """
        return super().form_invalid(form)


class SignUp2View(FormView):
    template_name = 'main_en/signup2.html'
    form_class = Signup2Form
    extra_context = {
        'title': 'Sign Up'
    }

    def get_initial(self):
        initial = super().get_initial()
        form_data_2 = self.request.session.get('form_data_2')

        if form_data_2:
            initial['username'] = form_data_2.get('username')
            initial['telephone_number'] = form_data_2.get('telephone_number')
            initial['date_of_birth'] = form_data_2.get('date_of_birth')
            initial['email'] = form_data_2.get('email')

        return initial

    def get_success_url(self):
        return reverse('signup_3')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        cleaned_data['date_of_birth'] = cleaned_data['date_of_birth'].isoformat()
        self.request.session['form_data_2'] = cleaned_data
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Invalid')
        for field in form.errors:
            print(f'Field is {field}, Error is {form.errors[field].as_text()}')
            messages.error(self.request, form.errors[field].as_text())
        return super().form_invalid(form)


class SignUp3View(FormView):
    template_name = 'main_en/signup3.html'
    form_class = Signup3Form
    extra_context = {
        'title': 'Sign Up'
    }

    def login_user(self, form):
        data = self.get_session_data()
        username = data['username']
        password = form.cleaned_data['password1']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # Log in the user
        login(self.request, user)

        del self.request.session['form_data_1']
        del self.request.session['form_data_2']

    def get_session_data(self):
        data1 = self.request.session['form_data_1']
        data2 = self.request.session['form_data_2']

        personal_information = {
            'first_name': data1['first_name'],
            'last_name': data1['last_name'],
            'middle_name': data1['middle_name'],
            'username': data2['username'],
            'telephone_number': data2['telephone_number'],
            'date_of_birth': data2['date_of_birth'],
            'email': data2['email']
        }
        return personal_information

    @staticmethod
    def is_password_match(form):
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        if password1 == password2:
            return True
        else:
            return False

    def create_auth_user(self, form):
        data = self.get_session_data()
        password1 = form.cleaned_data['password1']

        if not User.objects.filter(username=data['username']).exists():
            user = User.objects.create_user(
                username=data['username'],
                password=password1,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            user.save()
            return True
        else:
            return False

    def get_user(self):
        data = self.get_session_data()
        user = User.objects.get(username=data['username'])
        return user

    def create_account(self):
        data = self.get_session_data()
        print('creating account')
        print(data['date_of_birth'])
        account = Account.objects.create(
            user=self.get_user(),
            username=data['username'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            telephone_number=data['telephone_number'],
            date_of_birth=data['date_of_birth'],
            email=data['email']
        )

        account.save()

    def get_success_url(self):
        return reverse('account_is_created')

    def form_valid(self, form):
        if self.is_password_match(form):
            try:
                password_validation.validate_password(form.cleaned_data['password1'])
                if self.create_auth_user(form):
                    self.create_account()  # Creating user's account
                    self.login_user(form)  # Log in the user
                    return super().form_valid(form)
                else:
                    return self.form_invalid(form)

            except password_validation.ValidationError as e:
                print('Not valid password')
                return self.form_invalid(form)

        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        print('Invalid')
        for field in form.errors:
            print(f'Field is {field}, Error is {form.errors[field].as_text()}')
            messages.error(self.request, form.errors[field].as_text())
        return super().form_invalid(form)


class AccountIsCreatedView(TemplateView):
    template_name = 'main_en/thanks_for_signup.html'
    extra_context = {
        'title': 'Thank You'
    }


class LogoutView(RedirectView):
    url = reverse_lazy('home')  # URL to redirect after logout

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)  # Logout the user
        return super().get_redirect_url(*args, **kwargs)


class AccountView(TemplateView):
    template_name = 'main_en/account.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        account = Account.objects.get(user=self.request.user)
        context['account'] = account
        context['title'] = 'Your Account'
        return context
