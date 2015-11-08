from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import cvia.views as views

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'resumes', views.ResumeViewSet)
router.register(r'submissions', views.SubmissionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
