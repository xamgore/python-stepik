# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class StoryTemplate:
    _resources_name = 'story-templates'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StoryTemplate(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StoryTemplate are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def title(self) -> str:
        return self._data['title']


    @title.setter
    def title(self, value: str):
        self._data['title'] = value


    @required
    @property
    def parts(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self._data['parts']


    @parts.setter
    def parts(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        self._data['parts'] = value


    @required
    @property
    def cover(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cover', "None")


    @cover.setter
    def cover(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['cover'] = value


    @property
    def is_published(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_published']


    @is_published.setter
    def is_published(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_published'] = value




class ListOfStoryTemplates:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> StoryTemplate:
        return StoryTemplate(self._stepik, self._stepik._fetch_object(StoryTemplate, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[StoryTemplate]:
        objects = self._stepik._fetch_objects(StoryTemplate, ids)
        iterable = (StoryTemplate(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
