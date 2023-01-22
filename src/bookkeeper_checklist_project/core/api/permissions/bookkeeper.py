# -*- coding: utf-8 -*-#
from rest_framework import permissions
from pprint import pprint


class BookkeeperApiPermission(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.user_type == "bookkeeper":
            return True


class CheckOwnerPermission(permissions.BasePermission):
    message = "Editing post is restricted to owner only!"

    def has_object_permission(self, request, view, obj):
        # if request.user.is_superuser:
        #     return True
        # pprint(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            print("#############################")
            return True
        #
        # if obj.author == request.user:
        #     return True
        #
        # if request.user.is_staff and request.method not in self.edit_methods:
        #     return True
        #
        # if request.user.user_type == "assistant":
        #     return True

        return True
