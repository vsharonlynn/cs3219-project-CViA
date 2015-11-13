from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from cvia.settings import MEDIA_ROOT
import cvia.views as views

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'resumes', views.ResumeViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'uploads', views.FileUploadViewSet)
router.register(r'my-jobs', views.MyJobViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('allauth.urls')),
    url(r'^api/profile', RedirectView.as_view(url='/rest-auth/user/')),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
] + static('files/', document_root=MEDIA_ROOT)
