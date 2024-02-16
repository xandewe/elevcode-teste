from rest_framework.views import APIView, Request, Response, status
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, req: Request):

        try:
            page = req.query_params["page"]
        except:
            page = 1

        url = f"https://api.themoviedb.org/3/movie/popular?language=pt-br&page={page}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjN2Y5NzgxOTkxYTUzZmVkZWY5MjBiZjIyNjU2ZGI0MiIsInN1YiI6IjY1Y2Y1YjQ5MzVkYjQ1MDE0YTE4NmRkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y0l1V_3sYEiseePLHrxVf2iObfttcRPVPwr6jX_oBH0",
        }

        response = requests.get(url, headers=headers)

        return Response(response.json(), status.HTTP_200_OK)
