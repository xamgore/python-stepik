# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class SearchReaction:
    _resources_name = 'search-reactions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SearchReaction(id={self.result!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SearchReaction are missing')


    @required
    @property
    def result(self) -> str:
        return self._data['result']


    @result.setter
    def result(self, value: str):
        self._data['result'] = value




class ListOfSearchReactions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def create(self,
               result: str,
               **kwargs) -> SearchReaction:
        vars = locals().copy()
        data = {'search-reaction':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('search-reactions', data)
        if 'search-reactions' not in response:
            raise StepikError(response)

        return SearchReaction(self._stepik, response['search-reactions'][0])

