# -*- coding: utf-8 -*-#
from core.models import SoftDeleteManager, BaseQuerySetMixin


class RepliesQuerySet(BaseQuerySetMixin):
    def get_only_discussion(self):
        return self.filter(replies__isnull=True)


class SpecialAssignmentQuerySet(BaseQuerySetMixin):
    def get_not_seen_special_assignment(self):
        return self.filter(is_seen=False)


class RepliesManager(SoftDeleteManager):
    def get_queryset(self) -> RepliesQuerySet:
        queryset = RepliesQuerySet(self.model, using=self._db).filter(is_deleted=False)
        return queryset


class SpecialAssignmentsManager(SoftDeleteManager):
    def get_queryset(self) -> SpecialAssignmentQuerySet:
        queryset = SpecialAssignmentQuerySet(self.model, using=self._db).filter(
            is_deleted=False
        )
        return queryset
