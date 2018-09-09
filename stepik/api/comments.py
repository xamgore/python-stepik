# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Comment:
    """
    Comments resource.
    """

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




class ListOfComments:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Comment:
        obj = self._stepik._fetch_object(Comment, id)
        return Comment(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Comment]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Comment, ids)
        iterable = (Comment(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                user: Any = None,
                parent: str = None,
                course: Any = None,
                target: str = None,
                by_time: bool = None,
                by_id: bool = None,
                by_last_time: bool = None,
                by_vote_delta: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Comment]:
        """
        There are base fields, like ``language``, that can be used to filter out
        objects. Also there are ordering fields, that starts with ``by_`` prefix.
        They are not used in queries if their value is ``None``. If ``True``
        objects are sorted in straight order, if ``False`` in reversed.
        The sorting is done on the server side, there is no guarantees will it be
        in ascending or descending order.

        ``skip`` parameter means how much objects to skip from the beginning.

        ``limit`` means how much objects to take. It can be set to ``None``,
        all objects will be fetched (not recommended, actually).
        """

        assert skip >= 0, 'skip must be positive'
        assert limit is None or limit >= 0, 'limit must be positive'

        vars = locals().copy()
        args, order = [], []

        for k, v in vars.items():
            is_ordering = k.startswith('by_')
            is_special = k in ['self', 'skip']

            if not v is None and not is_ordering and not is_special:
                args.append((k, v))

            if not v is None and is_ordering:
                sign = '-' if v else ''
                order.append(sign + k[3:])

        from urllib.parse import urlencode
        params = urlencode(args, doseq=True)
        ordering = ','.join(order)

        skip = 0 if skip is None else skip
        page_idx, count = divmod(skip, 20)
        page_idx += 1  # stepik counts from 1

        while True:
            page = self._stepik._get(f'comments?{params}&page={page_idx}&order={ordering}')

            for obj in page['comments']:
                if limit and count >= limit:
                    break

                yield Comment(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               target: str,
               parent: str = None,
               text: str = None,
               is_pinned: bool = None,
               is_reported: bool = None,
               attachments: str = None,
               thread: str = None,
               submission: str = None,
               **kwargs) -> Comment:
        vars = locals().copy()
        data = {'comment':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('comments', data)
        if 'comments' not in response:
            raise StepikError(response)

        return Comment(self._stepik, response['comments'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('comments', id)


    def update(self, obj: Comment) -> Comment:
        required = ['target', 'parent', 'text', 'is_pinned', 'is_reported', 'attachments', 'thread', 'submission']
        vars = obj._data
        data = {'comment':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'comments/{ obj.id }', data)
        if 'comments' not in response:
            raise StepikError(response)

        return Comment(self._stepik, response['comments'][0])

