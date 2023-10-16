# import os
# import random

# import pandas as pd
# from constance import config
# from django.conf import settings
# from rest_framework import serializers, status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from app.api.utils import inline_serializer

# from .models import GameSession
# from .selectors import game_session_get_result
# from .services import (
#     game_session_create,
#     game_session_delete,
#     game_session_finish,
#     game_session_update_feedback,
# )
# from .tasks import process_answers


# class GameSessionStartApi(APIView):
#     class InputSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = GameSession
#             fields = (
#                 "gender",
#                 "child_age",
#                 "adult_age_span",
#                 "level_of_education",
#                 "first_time_playing",
#             )

#     def post(self, request):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         rules = pd.read_csv(
#             os.path.join(settings.MEDIA_ROOT, config.RULES),
#             names=["pattern", "category", "cat.simple.rule", "rule"],
#             index_col=None,
#         )
#         rules_association = {
#             "never": "easy",
#             "once": "complex1",
#             "more_than_once": "complex2",
#         }
#         ruletype = rules_association.get(serializer.validated_data.get("first_time_playing"))
#         nb_rules = rules["rule"].str.extract(r"{}(\d+)".format(ruletype), expand=False).dropna().astype(int).max()
#         rulename = f"{ruletype}{random.randint(1, nb_rules)}"
#         patterns = [
#             [pattern, category]
#             for (pattern, category) in zip(
#                 rules[rules["rule"] == rulename]["pattern"].tolist(),
#                 rules[rules["rule"] == rulename]["category"].tolist(),
#             )
#         ]

#         session = game_session_create(**serializer.validated_data, rule=rulename)

#         return Response(
#             {
#                 "session": session.id,
#                 "patterns": patterns,
#             },
#             status=status.HTTP_200_OK,
#         )


# class GameSessionFinishApi(APIView):
#     class InputSerializer(serializers.Serializer):
#         id = serializers.IntegerField(required=True)
#         data = inline_serializer(
#             many=True,
#             required=True,
#             fields={
#                 "pattern": serializers.CharField(min_length=4, max_length=4, required=True),
#                 "category": serializers.CharField(),
#                 "phase": serializers.CharField(required=True),
#                 "answer": serializers.CharField(required=True),
#                 "is_correct": serializers.BooleanField(required=False),
#                 "time_to_answer": serializers.FloatField(),
#             },
#         )

#     def post(self, request):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         session = game_session_finish(**serializer.validated_data)

#         process_answers.delay(session.id)

#         return Response(
#             {"next": session.get_absolute_url()},
#             status=status.HTTP_200_OK,
#         )


# class GameSessionDeleteApi(APIView):
#     class InputSerializer(serializers.ModelSerializer):
#         id = serializers.IntegerField(required=True)

#         class Meta:
#             model = GameSession
#             fields = ("id",)

#     def post(self, request):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         game_session_delete(**serializer.validated_data)

#         return Response({"message": "Success"}, status=status.HTTP_200_OK)


# class GameSessionFeedbackApi(APIView):
#     class InputSerializer(serializers.ModelSerializer):
#         id = serializers.IntegerField(required=True)

#         class Meta:
#             model = GameSession
#             fields = (
#                 "id",
#                 "feedback",
#             )

#     def post(self, request):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         game_session_update_feedback(**serializer.validated_data)

#         return Response(status=status.HTTP_200_OK)


# class GameSessionResultApi(APIView):
#     def get(self, request, *args, **kwargs):
#         result = game_session_get_result(id=kwargs.get("id"))

#         return Response({"result": result}, status=status.HTTP_200_OK)
