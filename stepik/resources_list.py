from typing import TypeVar, List, Generic, Iterator


Ty = TypeVar('Ty')


class ResourcesList(Generic[Ty]):
    def __init__(self, ty: TypeVar, stepik, holder: object, field_with_ids: str) -> None:
        from .stepik import Stepik
        self.__stepik: Stepik = stepik
        self.__field_with_ids = field_with_ids
        self.__holder = holder
        self.__ty = ty


    def __iter__(self) -> Iterator[Ty]:
        ids = getattr(self.__holder, self.__field_with_ids)
        objs = self.__stepik._fetch_objects(self.__ty, ids)
        yield from (self.__ty(self.__stepik, o) for o in objs)


    def list(self) -> List[Ty]:
        return [o for o in self]


    def add(self, value: Ty):
        print('add {} to list holder.{}, and PUT it to /api/{}s'
              .format(value.id, self.__field_with_ids, self.__holder.__class__.__name__.lower()))
        pass


    def remove(self, id):
        print('remove id {} from list holder.{}, and PUT it to /api/{}s'
              .format(id, self.__field_with_ids, self.__holder.__class__.__name__.lower()))
        pass
