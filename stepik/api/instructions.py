# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Instruction:
    """
    Instruction resource.
    Instruction enables peer review for the step.
    """

    _resources_name = 'instructions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Instruction(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Instruction are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @required
    @property
    def min_reviews(self) -> int:
        """
        Default value: ``3``
        """
        return self._data.setdefault('min_reviews', 3)


    @min_reviews.setter
    def min_reviews(self, value: int):
        """
        Default value: ``3``
        """
        self._data['min_reviews'] = value


    @property
    def strategy_type(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('strategy_type', "None")


    @strategy_type.setter
    def strategy_type(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['strategy_type'] = value


    @required
    @property
    def rubrics(self) -> str:
        return self._data['rubrics']


    @rubrics.setter
    def rubrics(self, value: str):
        self._data['rubrics'] = value


    @readonly
    @property
    def is_frozen(self) -> bool:
        return self._data['is_frozen']


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value




class ListOfInstructions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Instruction:
        obj = self._stepik._fetch_object(Instruction, id)
        return Instruction(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Instruction]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Instruction, ids)
        iterable = (Instruction(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Instruction]:
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
            page = self._stepik._get(f'instructions?{params}&page={page_idx}&order={ordering}')

            for obj in page['instructions']:
                if limit and count >= limit:
                    break

                yield Instruction(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               step: str,
               min_reviews: int = None,
               strategy_type: str = None,
               rubrics: str = None,
               text: str = None,
               **kwargs) -> Instruction:
        vars = locals().copy()
        data = {'instruction':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('instructions', data)
        if 'instructions' not in response:
            raise StepikError(response)

        return Instruction(self._stepik, response['instructions'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('instructions', id)


    def update(self, obj: Instruction) -> Instruction:
        required = ['step', 'min_reviews', 'strategy_type', 'rubrics', 'text']
        vars = obj._data
        data = {'instruction':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'instructions/{ obj.id }', data)
        if 'instructions' not in response:
            raise StepikError(response)

        return Instruction(self._stepik, response['instructions'][0])

