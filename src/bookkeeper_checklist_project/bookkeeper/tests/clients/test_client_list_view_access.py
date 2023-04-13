# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core import management
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from core.utils.developments import debugging_print
from core.utils.developments.debugging_print import debugging_colored_print
from users.management.commands import create_groups
from users.tests.factories.users_factory import UserFactory


class TestClientListViewAccess(TestCase):
    def setUp(self):
        # First create user groups
        debugging_colored_print(f"Create init users groups: ", "yellow", mark="####")
        management.call_command(create_groups.Command())
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = UserFactory.create(password="test123456")
        debugging_colored_print(f"Create user {self.user}", "green", mark="***")
        # ch = self.user.check_password("test123456")
        # debugging_print(ch)
        # login the bookkeeper
        debugging_colored_print(f"Login - {self.user}", "yellow", mark="***")
        self.client.login(username=self.user.email, password="test123456")

    def tearDown(self):
        debugging_colored_print(f"Delete user {self.user}", "yellow", mark="###")
        self.user.delete()

    def test_access_client_list_view(self):
        client_list_url = reverse("client:list")
        # Assign client can list view permission
        content_type = ContentType.objects.get(model="client", app_label="client")
        permission = Permission.objects.get(content_type=content_type, codename="can_view_list")
        debugging_print(content_type)
        debugging_print(permission)
        self.user.user_permissions.add(permission)
        response = self.client.get(client_list_url)
        # debugging_print(dir(response))
        # debugging_print(type(response.request))
        # debugging_print(response.status_code)
        # debugging_print(response.url)
        # debugging_print(response.request)
        debugging_print(response.status_code)
        # if status code is 403 means the bookkeeper not has client permission to see client view
        self.assertEquals(response.status_code, 200)
        # self.assertNotEquals(response.status_code, 302)
        # self.assertListEqual([response.status_code], [403])
