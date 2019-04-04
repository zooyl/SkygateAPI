from rest_framework import permissions


class ExamPermission(permissions.BasePermission):
    """ User has to be owner of an object to perform actions """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class TaskPermission(permissions.BasePermission):
    """ User has to be owner of an object to perform actions """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.exam.user == request.user
