from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="DailyBee API",
        default_version='beta 1',

    ),
    public=True,
    permission_classes=(AllowAny,),
)
