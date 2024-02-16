from rest_framework.views import APIView, Request, Response, status
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import os
from dotenv import load_dotenv

load_dotenv()


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, req: Request):
        token = os.getenv("API_TOKEN")

        try:
            page = req.query_params["page"]
        except:
            page = 1

        url = f"https://api.themoviedb.org/3/movie/popular?language=pt-br&page={page}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}",
        }

        response = requests.get(url, headers=headers)

        return Response(response.json(), status.HTTP_200_OK)
