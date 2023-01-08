# -*- coding: utf-8 -*-#
from typing import Optional, Union

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from core.utils import debugging_print, get_trans_txt
from special_assignment.models import Discussion, SpecialAssignment
from users.models import CustomUser


class DiscussionForm(BaseModelFormMixin):
    def __init__(
        self,
        special_assignment: Optional[SpecialAssignment] = None,
        discussion_user: Optional[CustomUser] = None,
        reply_object: Optional[Discussion] = None,
        *args,
        **kwargs,
    ):
        super(DiscussionForm, self).__init__(*args, **kwargs)

        self.fields["body"].widget.attrs.update({"rows": 5, "cols": 10})

        self.fields["title"].widget.attrs.update(
            {"placeholder": get_trans_txt("Optional title for the reply")}
        )

        # check if special assignment is passed
        if special_assignment:
            self.fields["special_assignment"].initial = special_assignment
            self.fields["special_assignment"].widget.attrs.update(
                {"class": "readonly-select", "readonly": "readonly"}
            )
            self.fields["replies"].queryset = Discussion.objects.select_related().filter(
                special_assignment=special_assignment
            )

        # check if the discussion_user passed
        if discussion_user:
            user_type = discussion_user.user_type
            match user_type:
                case "manager":
                    self.fields["manager"].initial = discussion_user.manager
                case "bookkeeper":
                    self.fields["bookkeeper"].initial = discussion_user.bookkeeper
                case "assistant":
                    self.fields["assistant"].initial = discussion_user.assistant

            for field_name in ["bookkeeper", "assistant", "manager"]:
                if field_name != user_type:
                    self.fields.pop(field_name)
            self.fields[user_type].widget.attrs.update({"class": "readonly-select"})

        # check if reply_object passed
        # if reply_object:
        #     self.fields["replies"].initial = reply_object
        # else:
        #     self.fields.pop("replies")

    class Meta(BaseModelFormMixin.Meta):
        model = Discussion
        exclude = EXCLUDED_FIELDS + ["is_seen"]
