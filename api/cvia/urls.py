from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
import cvia.views as views

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'resumes', views.ResumeViewSet)
router.register(r'submissions', views.SubmissionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('allauth.urls')),
    url(r'^api/profile', RedirectView.as_view(url='/rest-auth/user/')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
