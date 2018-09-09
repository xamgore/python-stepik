# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class StorageRecord:
    _resources_name = 'storage-records'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StorageRecord(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StorageRecord are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @property
    def kind(self) -> str:
        """
        Default value: ````
        """
        return self._data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Default value: ````
        """
        self._data['kind'] = value


    @property
    def data(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['data']


    @data.setter
    def data(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self._data['data'] = value


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




class ListOfStorageRecords:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> StorageRecord:
        obj = self._stepik._fetch_object(StorageRecord, id)
        return StorageRecord(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[StorageRecord]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(StorageRecord, ids)
        iterable = (StorageRecord(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[StorageRecord]:
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
            page = self._stepik._get(f'storage-records?{params}&page={page_idx}&order={ordering}')

            for obj in page['storage-records']:
                if limit and count >= limit:
                    break

                yield StorageRecord(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               kind: str = None,
               data: str = None,
               **kwargs) -> StorageRecord:
        vars = locals().copy()
        data = {'storage-record':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('storage-records', data)
        if 'storage-records' not in response:
            raise StepikError(response)

        return StorageRecord(self._stepik, response['storage-records'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('storage-records', id)


    def update(self, obj: StorageRecord) -> StorageRecord:
        required = ['kind', 'data']
        vars = obj._data
        data = {'storage-record':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'storage-records/{ obj.id }', data)
        if 'storage-records' not in response:
            raise StepikError(response)

        return StorageRecord(self._stepik, response['storage-records'][0])

