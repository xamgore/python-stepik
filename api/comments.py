# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Comment:
    _resources_name = 'comments'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Comment(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Comment are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def parent(self) -> str:
        return self._data['parent']


    @parent.setter
    def parent(self, value: str):
        self._data['parent'] = value


    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @readonly
    @property
    def user_role(self) -> str:
        return self._data['user_role']


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('time', "None")


    @readonly
    @property
    def last_time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('last_time', "None")


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


    @required
    @readonly
    @property
    def reply_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['reply_count']


    @readonly
    @property
    def is_deleted(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_deleted']


    @readonly
    @property
    def deleted_by(self) -> str:
        return self._data['deleted_by']


    @readonly
    @property
    def deleted_at(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('deleted_at', "None")


    @readonly
    @property
    def can_edit(self) -> str:
        return self._data['can_edit']


    @readonly
    @property
    def can_moderate(self) -> str:
        return self._data['can_moderate']


    @readonly
    @property
    def can_delete(self) -> str:
        return self._data['can_delete']


    @readonly
    @property
    def actions(self) -> str:
        return self._data['actions']


    @required
    @property
    def target(self) -> str:
        return self._data['target']


    @target.setter
    def target(self, value: str):
        self._data['target'] = value


    @readonly
    @property
    def replies(self) -> str:
        return self._data['replies']


    @readonly
    @property
    def subscriptions(self) -> str:
        return self._data['subscriptions']


    @property
    def is_pinned(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_pinned']


    @is_pinned.setter
    def is_pinned(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_pinned'] = value


    @readonly
    @property
    def pinned_by(self) -> str:
        return self._data['pinned_by']


    @readonly
    @property
    def pinned_at(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('pinned_at', "None")


    @readonly
    @property
    def is_staff_replied(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_staff_replied']


    @property
    def is_reported(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_reported']


    @is_reported.setter
    def is_reported(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_reported'] = value


    @property
    def attachments(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self._data['attachments']


    @attachments.setter
    def attachments(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        self._data['attachments'] = value


    @property
    def thread(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('thread', "None")


    @thread.setter
    def thread(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['thread'] = value


    @property
    def submission(self) -> str:
        return self._data['submission']


    @submission.setter
    def submission(self, value: str):
        self._data['submission'] = value


    @readonly
    @property
    def edited_by(self) -> str:
        return self._data['edited_by']


    @readonly
    @property
    def edited_at(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('edited_at', "None")


    @readonly
    @property
    def epic_count(self) -> int:
        return self._data['epic_count']


    @readonly
    @property
    def abuse_count(self) -> int:
        return self._data['abuse_count']


    @readonly
    @property
    def vote_delta(self) -> int:
        return self._data['vote_delta']


    @readonly
    @property
    def vote(self) -> str:
        return self._data['vote']


    @readonly
    @property
    def translations(self) -> str:
        return self._data['translations']


