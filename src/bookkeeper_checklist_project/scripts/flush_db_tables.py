# -*- coding: utf-8 -*-#
from django.contrib.sessions.models import Session
from django.db.models import Q

from core.utils import debugging_print
from django import apps
from colorama import init
from colorama import Fore, Back, Style
from client.models import Client
from special_assignment.models import SpecialAssignment, Discussion
from jobs.models import JobProxy, JobCategory
from task.models import TaskProxy
from documents.models import Documents
from notes.models import Note
from company_services.models import CompanyService
from users.models import CustomUser


def run(*args):
    init(autoreset=True)
    excluded_apps = args[0].split(",")
    debugging_print(excluded_apps)
    excluded_users = [
        "manager@beachwoodfinancial.com",
        "admin@admin.com",
        "admin@admin.dev",
    ]

    print(Fore.YELLOW + f"Start flush (Discussion) table:")
    debugging_print(f"Total records: {Discussion.original_objects.all().count()}")
    Discussion.original_objects.all().delete()
    debugging_print(f"Finished flush (Discussion) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (SpecialAssignment) table:")
    debugging_print(f"Total records: {SpecialAssignment.original_objects.all().count()}")
    SpecialAssignment.original_objects.all().delete()
    debugging_print(f"Finished flush (SpecialAssignment) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (Task) table:")
    debugging_print(f"Total records: {TaskProxy.original_objects.all().count()}")
    TaskProxy.original_objects.all().delete()
    debugging_print(f"Finished flush (Task) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush clients bookkeepers only:")
    for client in Client.original_objects.all():
        debugging_print(f"Client name: {client.name}")
        bookkeepers = client.bookkeepers.all()
        if bookkeepers:
            client.bookkeepers.clear()
        else:
            print(Fore.RED + f"No bookkeepers for client {client.name}")
    debugging_print("###################################################")

    print(Fore.YELLOW + f"Start flush (Job) table:")
    debugging_print(f"Total records: {JobProxy.original_objects.all().count()}")
    JobProxy.original_objects.all().delete()
    debugging_print(f"Finished flush (Job) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (Documents) table:")
    debugging_print(f"Total records: {Documents.original_objects.all().count()}")
    Documents.original_objects.all().delete()
    debugging_print(f"Finished flush (Documents) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (Note) table:")
    debugging_print(f"Total records: {Note.original_objects.all().count()}")
    Note.original_objects.all().delete()
    debugging_print(f"Finished flush (Note) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (JobCategory) table:")
    debugging_print(f"Total records: {JobCategory.original_objects.all().count()}")
    JobCategory.original_objects.all().delete()
    debugging_print(f"Finished flush (JobCategory) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (CompanyService) table:")
    debugging_print(f"Total records: {CompanyService.original_objects.all().count()}")
    CompanyService.original_objects.all().delete()
    debugging_print(f"Finished flush (CompanyService) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (Users) table:")
    users_records = CustomUser.original_objects.filter(~Q(email__in=excluded_users))
    debugging_print(f"Total records: {users_records.count()}")
    users_records.delete()
    debugging_print(f"Finished flush (Users) table")
    print(Fore.RESET + "###################################################")

    print(Fore.YELLOW + f"Start flush (Session) table:")
    debugging_print(f"Total records: {Session.objects.all().count()}")
    Session.objects.all().delete()
    debugging_print(f"Finished flush (Session) table")
    print(Fore.RESET + "###################################################")
