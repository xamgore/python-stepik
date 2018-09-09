# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class BlockEdit:
    _resources_name = 'step-sources'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'BlockEdit(id={self.name!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model BlockEdit are missing')


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


    @property
    def video(self) -> str:
        return self._data['video']


    @video.setter
    def video(self, value: str):
        self._data['video'] = value


    @property
    def animation(self) -> str:
        return self._data['animation']


    @animation.setter
    def animation(self, value: str):
        self._data['animation'] = value


    @readonly
    @property
    def options(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['options']


    @readonly
    @property
    def subtitle_files(self) -> str:
        return self._data['subtitle_files']


    @property
    def source(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['source']


    @source.setter
    def source(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self._data['source'] = value


    @property
    def subtitles(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['subtitles']


    @subtitles.setter
    def subtitles(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self._data['subtitles'] = value


    @readonly
    @property
    def tests_archive(self) -> str:
        return self._data['tests_archive']


    @property
    def feedback_correct(self) -> str:
        return self._data['feedback_correct']


    @feedback_correct.setter
    def feedback_correct(self, value: str):
        self._data['feedback_correct'] = value


    @property
    def feedback_wrong(self) -> str:
        return self._data['feedback_wrong']


    @feedback_wrong.setter
    def feedback_wrong(self, value: str):
        self._data['feedback_wrong'] = value




class StepSource:
    _resources_name = 'step-sources'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StepSource(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StepSource are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @required
    @property
    def position(self) -> int:
        """
        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
        """
        self._data['position'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @required
    @property
    def block(self) -> str:
        """
        Type: str
        """
        return self._data['block']


    @block.setter
    def block(self, value: str):
        """
        Type: str
        """
        self._data['block'] = value


    @readonly
    @property
    def actions(self) -> str:
        return self._data['actions']


    @readonly
    @property
    def progress(self) -> str:
        return self._data['progress']


    @readonly
    @property
    def subscriptions(self) -> str:
        return self._data['subscriptions']


    @required
    @readonly
    @property
    def instruction(self) -> str:
        return self._data['instruction']


    @readonly
    @property
    def session(self) -> str:
        return self._data['session']


    @readonly
    @property
    def instruction_type(self) -> str:
        return self._data['instruction_type']


    @readonly
    @property
    def viewed_by(self) -> str:
        return self._data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> str:
        return self._data['passed_by']


    @readonly
    @property
    def correct_ratio(self) -> str:
        return self._data['correct_ratio']


    @readonly
    @property
    def worth(self) -> str:
        return self._data['worth']


    @property
    def is_solutions_unlocked(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_solutions_unlocked']


    @is_solutions_unlocked.setter
    def is_solutions_unlocked(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_solutions_unlocked'] = value


    @required
    @property
    def solutions_unlocked_attempts(self) -> int:
        """
        Default value: ``3``
        """
        return self._data.setdefault('solutions_unlocked_attempts', 3)


    @solutions_unlocked_attempts.setter
    def solutions_unlocked_attempts(self, value: int):
        """
        Default value: ``3``
        """
        self._data['solutions_unlocked_attempts'] = value


    @property
    def has_submissions_restrictions(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_submissions_restrictions']


    @has_submissions_restrictions.setter
    def has_submissions_restrictions(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['has_submissions_restrictions'] = value


    @required
    @property
    def max_submissions_count(self) -> int:
        """
        Default value: ``3``
        """
        return self._data.setdefault('max_submissions_count', 3)


    @max_submissions_count.setter
    def max_submissions_count(self, value: int):
        """
        Default value: ``3``
        """
        self._data['max_submissions_count'] = value


    @readonly
    @property
    def variation(self) -> str:
        return self._data['variation']


    @readonly
    @property
    def variations_count(self) -> str:
        return self._data['variations_count']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @readonly
    @property
    def discussions_count(self) -> str:
        return self._data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        return self._data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> str:
        return self._data['discussion_threads']


    @readonly
    @property
    def reason_of_failure(self) -> str:
        return self._data['reason_of_failure']


    @readonly
    @property
    def error(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{'text': '', 'code': '', 'params': {}}``
        """
        return self._data.setdefault('error', {'text': '', 'code': '', 'params': {}})


    @required
    @readonly
    @property
    def warnings(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self._data['warnings']


    @required
    @property
    def cost(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['cost']


    @cost.setter
    def cost(self, value: int):
        """
        Default value: ``0``
        """
        self._data['cost'] = value




class ListOfStepSources:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> StepSource:
        obj = self._stepik._fetch_object(StepSource, id)
        return StepSource(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[StepSource]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(StepSource, ids)
        iterable = (StepSource(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[StepSource]:
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
            page = self._stepik._get(f'step-sources?{params}&page={page_idx}&order={ordering}')

            for obj in page['step-sources']:
                if limit and count >= limit:
                    break

                yield StepSource(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               lesson: str,
               block: str,
               position: int = None,
               is_solutions_unlocked: bool = None,
               solutions_unlocked_attempts: int = None,
               has_submissions_restrictions: bool = None,
               max_submissions_count: int = None,
               cost: int = None,
               **kwargs) -> StepSource:
        vars = locals().copy()
        data = {'step-source':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('step-sources', data)
        if 'step-sources' not in response:
            raise StepikError(response)

        return StepSource(self._stepik, response['step-sources'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('step-sources', id)


    def update(self, obj: StepSource) -> StepSource:
        required = ['lesson', 'block', 'position', 'is_solutions_unlocked', 'solutions_unlocked_attempts', 'has_submissions_restrictions', 'max_submissions_count', 'cost']
        vars = obj._data
        data = {'step-source':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'step-sources/{ obj.id }', data)
        if 'step-sources' not in response:
            raise StepikError(response)

        return StepSource(self._stepik, response['step-sources'][0])

