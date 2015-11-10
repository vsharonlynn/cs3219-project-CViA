from rest_framework import permissions
from cvia.models import Submission


class IsSelf(permissions.BasePermission):
    """
    Custom permission to only allow user to edit his/herself
    """

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsRecruiter(permissions.BasePermission):
    """
    Custom permission to only allow Recruiter to perform the action
    """

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Recruiter'


class IsEmployee(permissions.BasePermission):
    """
    Custom permission to only allow Employee to perform the action
    """

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Employee'


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsResumeOwnerOrRecruiter(permissions.BasePermission):
    """
    Custom permission to only allow owners of a resume or submitted to recruiter to access it.
    """

    def has_object_permission(self, request, view, obj):
        submitted = Submission.objects.filter(job__author__user=request.user,
                                              resume__author=obj.author).first()
        return obj.author == request.user or submitted is not None
