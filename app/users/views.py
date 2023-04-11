from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import FormView

from django.conf import settings

# Create your views here.
class UsersRegisterView(FormView):
    template_name = "users/register.html"
    form = UserCreationForm
    error_messages = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form, 'error_messages': self.error_messages})

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """

        form = self.form(request.POST)

        # reCAPTCHA validation
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if not result['success']: error_messages["invalid_captcha"] = "Invalid reCAPTCHA. Please try again"

        if not request.POST.get('accept_terms'): error_messages["terms_service"] = "You must accept the terms of service"

        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(Q(email=email))
            if not user.exists():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                token = str(user.pk) + 'p' + get_user_token(user)
                subject = 'Account activation'
                email_template_name='users/register_email.html'
                current_site = get_current_site(request)
                parameters = {
                    'email': user.email,
                    'domain': current_site.domain,
                    'site_name': 'Inadgo',
                    'token': token,
                    'protocol': 'http',
                }
                email_content = render_to_string(email_template_name, parameters)
                email_content = strip_tags(email_content)
                if result['success'] and request.POST.get('accept_terms'):
                    try:
                        send_mail(subject, email_content, '', [email], fail_silently=False)
                        messages.success(request, f"An email has been sent to {email} to confirm the account creation")
                        return redirect('core:landing')
                    except SMTPRecipientsRefused:
                        messages.error(request, "Invalid header")
                        user.delete()
                    return redirect('core:landing')
            else:
                error_messages['email_exists'] = "A user with the same email address already exists in our database"

class UsersPasswordResetView(PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    success_url = "password_reset_confirm"

class UsersPasswordResetConfirmView(PasswordResetView):
    template_name = "users/password_reset_confirm.html"

class UsersPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


#TO DO: USERS WITH UNACTIVATED ACCOUNT (i.e. UNVERIFIED EMAIL) CAN RECEIVE A FYP EMAIL BECAUSE THEY ARE PRESENT IN THE DATABASE.
# INDAGO SHOULD PREVENT THIS KIND OF BEHAVIOUR, PROVIDE A WAY TO RESEND THE ACCOUNT ACTIVATION EMAIL AND NOT KEEP THE ACCOUNT IN THE DATABASE
# SOLUTION : CREATE A DEDICATED VIEW FOR ACTIVATION ?


from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

def password_reset(request):
    error_messages = {}
    if request.method == 'POST':
        forgot_password_form = PasswordResetForm(request.POST)

        # reCAPTCHA validation
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if not result['success']: error_messages["invalid_captcha"] = "Invalid reCAPTCHA. Please try again"
        
        if forgot_password_form.is_valid():
            data = forgot_password_form.cleaned_data.get('email')
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Request'
                    email_template_name='authentication/password_reset_email.html'
                    current_site = get_current_site(request)
                    parameters = {
                        'email': user.email,
                        'domain': current_site.domain, #to change in production
                        'site_name': 'Inadgo',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http', #to change in production
                    }
                    email_content = render_to_string(email_template_name, parameters)
                    email_content = strip_tags(email_content)
                    if result['success']:
                        try: 
                            send_mail(subject, email_content, '', [user.email], fail_silently=False)
                            messages.success(request, "An email has been sent to " + user.email + ". Please check your emails and follow the instructions. If it not appears in your mailbox, please ensure to check the spam folder")
                            return redirect('core:landing')
                        except SMTPRecipientsRefused:
                            return HttpResponse('Invalid Header')
            else:
                error_messages["invalid_email"] = "No account associated to this email address has been found. Please enter a valid email address."
        else:
            error_messages["invalid_email"] = "Please enter a valid email address"
    return render(request, 'authentication/password_reset.html', context=error_messages)
