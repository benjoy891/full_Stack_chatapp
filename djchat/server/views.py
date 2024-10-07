from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Server
from .serializer import ServerSerializer, ChannelSerializer
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.db.models import Count
from .schema import server_list_docs


# Create your views here.

class ServerListViewSet(viewsets.ViewSet):
    """
    ServerListViewSet provides an endpoint for retrieving and filtering a list of Server objects.

    This viewset supports several query parameters that allow users to retrieve servers based on 
    categories, specific server IDs, and associated user membership. Additionally, it offers an 
    option to limit the number of results and display the number of members in each server.

    Main Functions:
    1. `list`: Handles the GET request for listing servers with optional filtering and ordering.

    Query Parameters:
    - `category` (string, optional): Filters the servers by the category name. The `category` should match 
    the `name` field of the `Category` model associated with the server.
    
    - `qty` (int, optional): Limits the number of server results to the value of `qty`. If not provided, all
    servers matching the filters will be returned.

    - `by_user` (boolean, optional): If set to "true", filters the servers where the currently authenticated user 
    is a member. This filter requires the user to be authenticated; otherwise, an `AuthenticationFailed` exception
    is raised.

    - `by_serverid` (int, optional): Filters the servers by a specific server ID. The server ID should be a valid 
    integer. If the server with the provided ID is not found, a `ValidationError` is raised. If an invalid value is 
    passed, a `ValidationError` with a message "Server value error" will be raised.

    - `with_num_members` (boolean, optional): If set to "true", annotates each server in the result set with the 
    number of members. The result will include a `num_members` field that contains the count of users associated 
    with each server.

    Behavior:
    - The method starts by retrieving all servers (`Server.objects.all()`).
    - If a `category` is provided, the queryset is filtered to return only servers belonging to the specified category.
    - If `by_user` is set to true, the queryset is filtered to return only servers where the authenticated user is a member.
    - If `with_num_members` is true, the queryset is annotated with a `num_members` field containing the count of members for each server.
    - The number of results can be limited by specifying the `qty` parameter.
    - The `by_serverid` parameter filters the queryset by server ID. If the ID is invalid or not found, an appropriate 
    validation error is returned.

    Security:
    - When filtering by `by_user` or `by_serverid`, the method checks if the user is authenticated. If not, an 
    `AuthenticationFailed` exception is raised.
    
    Exception Handling:
    - `AuthenticationFailed`: Raised if the request is trying to filter by user membership or server ID but the 
    user is not authenticated.
    - `ValidationError`: Raised if a provided server ID does not exist or if an invalid value is passed for the server ID.

    Return:
    - The method serializes the resulting queryset using the `ServerSerializer` and includes a context parameter to 
    pass whether the `num_members` field is included. The data is returned as a JSON response.
    """

    queryset = Server.objects.all()

    @server_list_docs
    def list(self, request):
        queryset = Server.objects.all()
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # if by_user or by_serverid and not request.user.is_authenticated:
        #     raise AuthenticationFailed()

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()


        if with_num_members:
            self.queryset = self.queryset.annotate(num_members = Count('member'))

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            try:
                self.queryset = self.queryset.filter(id=by_serverid)        
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail=f"Server value error")
            

        serializer = ServerSerializer(self.queryset, many=True, context={"num_memberes": with_num_members})
        return Response(serializer.data)
    
    





