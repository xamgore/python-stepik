# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class RecommendationReaction:
    _resources_name = 'recommendation-reactions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'RecommendationReaction(id={self.user!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model RecommendationReaction are missing')


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self._data['lesson'] = value


    @required
    @property
    def reaction(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('reaction', "None")


    @reaction.setter
    def reaction(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['reaction'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        return self._data.setdefault('time', "2018-08-26T00:35:32.023Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        self._data['time'] = value




class ListOfRecommendationReactions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, users: Iterable[str], keep_order=False) -> Iterable[RecommendationReaction]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            users = list(users)

        objects = self._stepik._fetch_objects(RecommendationReaction, users)
        iterable = (RecommendationReaction(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'user')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[RecommendationReaction]:
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
            page = self._stepik._get(f'recommendation-reactions?{params}&page={page_idx}&order={ordering}')

            for obj in page['recommendation-reactions']:
                if limit and count >= limit:
                    break

                yield RecommendationReaction(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               user: str,
               lesson: str,
               reaction: str,
               time: str = None,
               **kwargs) -> RecommendationReaction:
        vars = locals().copy()
        data = {'recommendation-reaction':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('recommendation-reactions', data)
        if 'recommendation-reactions' not in response:
            raise StepikError(response)

        return RecommendationReaction(self._stepik, response['recommendation-reactions'][0])

