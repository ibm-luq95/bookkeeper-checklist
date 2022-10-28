from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import permissions
from prettyprinter import cpprint
import json

from jobs.serializers import CreateJobSerializer


class CreateJobToBookkeeper(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            tasks = data.get("tasks")  # save tasks as string
            del data["tasks"]  # delete tasks from dict
            tasks = json.loads(tasks)  # convert tasks string to dict
            data.setdefault("tasks", tasks)  # save the tasks as list
            serializer = CreateJobSerializer(data=data)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.error_messages)

            serializer.save()
            return Response(
                {"msg": "Job created successfully!"}, status=status.HTTP_201_CREATED
            )
        except APIException as ex:
            print(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while add job to bookkeeper!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
