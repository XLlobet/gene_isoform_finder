from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static
from .                          import views

app_name    = 'SeqViewer'
urlpatterns = [

    path(   "accounts/", include("django.contrib.auth.urls")),
    path(   "",
            views.index,
            name="index"),
    path(   "SeqViewer",
            views.index,
            name="index")
]