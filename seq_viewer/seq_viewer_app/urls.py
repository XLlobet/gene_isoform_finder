#   App Name:   Gene Isoform Finder
#   Author:     Xavier Llobet Navàs
#   Content:    Gene Isoform Finder urls
#
# - This file contains all the Django framework urñs for the 
#   Gene Isoform Finder.
# =====================================================================

# IMPORTS
# =====================================================================

from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static
from .                          import views

# DASH BIO APPLICATION: Genes Isoform Finder
# =====================================================================

app_name    = 'GeneIF'
urlpatterns = [

    path(   "accounts/", include("django.contrib.auth.urls")),
    path(   "",
            views.index,
            name="index"),
    path(   "GeneIF",
            views.index,
            name="index")
]