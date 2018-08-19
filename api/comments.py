# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteComment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteComment(id={self.id!r})'


    @property
    def parent(self) -> str:
        return self.__data['parent']


    @parent.setter
    def parent(self, value: str):
        self.__data['parent'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @property
    def target(self) -> str:
        return self.__data['target']


    @target.setter
    def target(self, value: str):
        self.__data['target'] = value


    @property
    def is_pinned(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_pinned']


    @is_pinned.setter
    def is_pinned(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_pinned'] = value


    @property
    def is_reported(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_reported']


    @is_reported.setter
    def is_reported(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_reported'] = value


    @property
    def attachments(self) -> List:
        """
        Default value: ``[]``
        """
        return self.__data['attachments']


    @attachments.setter
    def attachments(self, value: List):
        """
        Default value: ``[]``
        """
        self.__data['attachments'] = value


    @property
    def thread(self) -> str:
        """
        Type: choice
        """
        return self.__data['thread']


    @thread.setter
    def thread(self, value: str):
        """
        Type: choice
        """
        self.__data['thread'] = value


    @property
    def submission(self) -> str:
        return self.__data['submission']


    @submission.setter
    def submission(self, value: str):
        self.__data['submission'] = value




class Comment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Comment(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def parent(self) -> str:
        return self.__data['parent']


    @parent.setter
    def parent(self, value: str):
        self.__data['parent'] = value


    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @readonly
    @property
    def user_role(self) -> str:
        return self.__data['user_role']


    @readonly
    @property
    def time(self) -> str:
        """
        Type: datetime
        """
        return self.__data['time']


    @readonly
    @property
    def last_time(self) -> str:
        """
        Type: datetime
        """
        return self.__data['last_time']


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @readonly
    @property
    def reply_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['reply_count']


    @readonly
    @property
    def is_deleted(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_deleted']


    @readonly
    @property
    def deleted_by(self) -> str:
        return self.__data['deleted_by']


    @readonly
    @property
    def deleted_at(self) -> str:
        """
        Type: datetime
        """
        return self.__data['deleted_at']


    @readonly
    @property
    def can_edit(self) -> str:
        return self.__data['can_edit']


    @readonly
    @property
    def can_moderate(self) -> str:
        return self.__data['can_moderate']


    @readonly
    @property
    def can_delete(self) -> str:
        return self.__data['can_delete']


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


    @required
    @property
    def target(self) -> str:
        return self.__data['target']


    @target.setter
    def target(self, value: str):
        self.__data['target'] = value


    @readonly
    @property
    def replies(self) -> str:
        return self.__data['replies']


    @readonly
    @property
    def subscriptions(self) -> str:
        return self.__data['subscriptions']


    @property
    def is_pinned(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_pinned']


    @is_pinned.setter
    def is_pinned(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_pinned'] = value


    @readonly
    @property
    def pinned_by(self) -> str:
        return self.__data['pinned_by']


    @readonly
    @property
    def pinned_at(self) -> str:
        """
        Type: datetime
        """
        return self.__data['pinned_at']


    @readonly
    @property
    def is_staff_replied(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_staff_replied']


    @property
    def is_reported(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_reported']


    @is_reported.setter
    def is_reported(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_reported'] = value


    @property
    def attachments(self) -> List:
        """
        Default value: ``[]``
        """
        return self.__data['attachments']


    @attachments.setter
    def attachments(self, value: List):
        """
        Default value: ``[]``
        """
        self.__data['attachments'] = value


    @property
    def thread(self) -> str:
        """
        Type: choice
        """
        return self.__data['thread']


    @thread.setter
    def thread(self, value: str):
        """
        Type: choice
        """
        self.__data['thread'] = value


    @property
    def submission(self) -> str:
        return self.__data['submission']


    @submission.setter
    def submission(self, value: str):
        self.__data['submission'] = value


    @readonly
    @property
    def edited_by(self) -> str:
        return self.__data['edited_by']


    @readonly
    @property
    def edited_at(self) -> str:
        """
        Type: datetime
        """
        return self.__data['edited_at']


    @readonly
    @property
    def epic_count(self) -> int:
        return self.__data['epic_count']


    @readonly
    @property
    def abuse_count(self) -> int:
        return self.__data['abuse_count']


    @readonly
    @property
    def vote(self) -> str:
        return self.__data['vote']


    @readonly
    @property
    def translations(self) -> str:
        return self.__data['translations']


