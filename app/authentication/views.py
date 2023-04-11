from django.contrib.auth.views import LoginView, LogoutView

class UserSessionLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
""" 

    def login(request):
        invalid_login = False
        if request.POST:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth_login(request, user)

                if request.GET.get("next"):
                    return redirect(request.GET.get("next"))
                return redirect("/jobs/add/")
                
            else:
                invalid_login = True
        return render(request, 'core/login.html', {'form': LoginForm(), 'invalid_login': invalid_login})
    return """


