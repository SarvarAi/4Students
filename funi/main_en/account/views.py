from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import password_validation
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from .forms import Signup1Form, Signup2Form, Signup3Form

from ..models import Account


class SignUp1View(FormView):
    template_name = 'main_en/signup1.html'
    extra_context = {
        'title': 'Sign Up'
    }
    form_class = Signup1Form

    def get_initial(self):
        initial = super().get_initial()
        form_data_1 = self.request.session.get('form_data_1')

        if form_data_1:
            initial['first_name'] = form_data_1.get('first_name')
            initial['last_name'] = form_data_1.get('last_name')
            initial['middle_name'] = form_data_1.get('middle_name')

        return initial

    def get_success_url(self):
        return reverse('signup_2')

    def form_valid(self, form):
        self.request.session['form_data_1'] = form.cleaned_data
        return super().form_valid(form)

    def form_invalid(self, form):
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

    def create_account(self):
        data = self.get_session_data()
        print('creating account')
        print(data['date_of_birth'])
        account = Account.objects.create(
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
