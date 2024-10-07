from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from .serializer import  ServerSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='category',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="Filters the Category of servers to retrieve",
        ),
        OpenApiParameter(
            name='qty',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Filters the number of servers to be retrieved.",
        ),
        OpenApiParameter(
            name='by_user',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Filters services by the current authenticated user (True/False).",
        ),
        OpenApiParameter(
            name='with_num_members',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description="Retrieves the number of users in the server",
        ),
    ]
)

