from uuid import UUID

from backbone.adapter.abstract_entity import BaseEntity


class UserEntity(BaseEntity):
    id: int
    uuid: UUID
    name: str

    def __init__(self, id=None, uuid=None, name=None):
        self.id: int = id
        self.uuid: UUID = uuid
        self.name = name
