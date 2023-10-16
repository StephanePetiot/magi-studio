from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.selectors import user_get_login_data


class UserSessionLoginApi(APIView):
    """
    Following https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-in
    """

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def get(self, request):
        return render(request, "authentication/login.html")

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response({"messages": ["Wrong email and/or password"]}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response(
            {
                "session": session_key,
                "data": data,
                "messages": ["Valid credentials. You should be redirected..."],
                "redirect_url": settings.LOGIN_REDIRECT_URL,
            },
            status=status.HTTP_200_OK,
        )


class UserSessionLogoutApi(APIView):
    def get(self, request):
        logout(request)

        return Response({"redirect_url": settings.LOGOUT_REDIRECT_URL}, status=status.HTTP_200_OK)

    def post(self, request):
        logout(request)

        return Response({"redirect_url": settings.LOGOUT_REDIRECT_URL}, status=status.HTTP_200_OK)


# class UserJwtLoginApi(ObtainJSONWebTokenView):
#     def get(self, request):
#         return render(request, "authentication/login.html")

#     def post(self, request, *args, **kwargs):
#         # We are redefining post so we can change the response status on success
#         # Mostly for consistency with the session-based API
#         try:
#             response = super().post(request, *args, **kwargs)
#         except:
#             return Response({"messages": ["Wrong email and/or password"],}, status=status.HTTP_400_BAD_REQUEST)

#         if response.status_code == status.HTTP_201_CREATED:
#             response.status_code = status.HTTP_200_OK

#         response.data['redirect_url'] = settings.LOGIN_REDIRECT_URL
#         response.data['messages'] = ["Valid credentials. You should be redirected..."]

#         return response


# class UserJwtLogoutApi(ApiAuthMixin, APIView):

#     def post(self, request):
#         auth_logout(request.user)

#         response = Response(
#             {"redirect_url": settings.LOGOUT_REDIRECT_URL},
#             status=status.HTTP_200_OK
#         )

#         if settings.JWT_AUTH["JWT_AUTH_COOKIE"] is not None:
#             response.delete_cookie(settings.JWT_AUTH["JWT_AUTH_COOKIE"])

#         return response


# class UserMeApi(ApiAuthMixin, APIView):
#     def get(self, request):
#         data = user_get_login_data(user=request.user)

#         return Response(data)
