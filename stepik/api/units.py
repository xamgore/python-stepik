# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList
from .assignments import Assignment
from .lessons import Lesson


class Unit:
    """
    Returns a single unit.
    Unit is a lesson within a course.
    """

    _resources_name = 'units'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Unit(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Unit are missing')


    @property
    def assignments(self) -> ResourcesList[Assignment]:
        return ResourcesList[Assignment]\
            (Assignment, self._stepik, holder=self, field_with_ids='assignments_ids')


    def lesson(self) -> Lesson:
        return Lesson(self._stepik, self._stepik._fetch_object(Lesson, self.lesson_id))


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def section(self) -> int:
        """
        Id of the section
        """
        return self._data['section']


    @section.setter
    def section(self, value: int):
        """
        Id of the section
        """
        self._data['section'] = value


    @required
    @property
    def position(self) -> int:
        """
        Position in the syllabus

        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Position in the syllabus

        Default value: ``1``
        """
        self._data['position'] = value


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self._data['progress']


    @readonly
    @property
    def begin_date(self) -> str:
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date', "None")


    @readonly
    @property
    def end_date(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date', "None")


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline', "None")


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline', "None")


    @readonly
    @property
    def grading_policy(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy', "None")


    @property
    def begin_date_source(self) -> str:
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date_source', "None")


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date_source', "None")


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline_source', "None")


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline_source', "None")


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy_source', "None")


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        """
        True, if the section is open, i.e. the server's current date is between `begin_date` and `end_date`
        """
        return self._data['is_active']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Creation time

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Time of the last update

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @required
    @property
    def assignments_ids(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['assignments']


    @assignments_ids.setter
    def assignments_ids(self, value: List[int]):
        """
        Type: List[int]
        """
        self._data['assignments'] = value


    @required
    @property
    def lesson_id(self) -> int:
        """
        Id of the lesson associated with the unit
        """
        return self._data['lesson']


    @lesson_id.setter
    def lesson_id(self, value: int):
        """
        Id of the lesson associated with the unit
        """
        self._data['lesson'] = value




class ListOfUnits:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Unit:
        obj = self._stepik._fetch_object(Unit, id)
        return Unit(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Unit]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Unit, ids)
        iterable = (Unit(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                lesson: str = None,
                course: Any = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Unit]:
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
            page = self._stepik._get(f'units?{params}&page={page_idx}&order={ordering}')

            for obj in page['units']:
                if limit and count >= limit:
                    break

                yield Unit(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               section: int,
               lesson: int,
               assignments: List[int] = None,
               position: int = None,
               begin_date_source: str = None,
               end_date_source: str = None,
               soft_deadline_source: str = None,
               hard_deadline_source: str = None,
               grading_policy_source: str = None,
               **kwargs) -> Unit:
        vars = locals().copy()
        data = {'unit':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('units', data)
        if 'units' not in response:
            raise StepikError(response)

        return Unit(self._stepik, response['units'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('units', id)


    def update(self, obj: Unit) -> Unit:
        required = ['section', 'lesson', 'assignments', 'position', 'begin_date_source', 'end_date_source', 'soft_deadline_source', 'hard_deadline_source', 'grading_policy_source']
        vars = obj._data
        data = {'unit':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'units/{ obj.id }', data)
        if 'units' not in response:
            raise StepikError(response)

        return Unit(self._stepik, response['units'][0])

