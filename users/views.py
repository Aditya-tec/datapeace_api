from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User
from .serializers import UserSerializer

class UserListCreateAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        
        # Filter by name
        name_query = request.GET.get('name')
        if name_query:
            users = users.filter(
                Q(first_name__icontains=name_query) | Q(last_name__icontains=name_query)
            )

        # Sorting
        sort_param = request.GET.get('sort')
        if sort_param:
            users = users.order_by(sort_param)

        # Pagination
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 5))
        paginator = Paginator(users, limit)
        paginated_users = paginator.get_page(page)

        serializer = UserSerializer(paginated_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = self.get_object(pk)
        if not user:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        allowed_fields = {'first_name', 'last_name', 'age'}
        partial_data = {k: v for k, v in request.data.items() if k in allowed_fields}
        serializer = UserSerializer(user, data=partial_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        if user:
            user.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
