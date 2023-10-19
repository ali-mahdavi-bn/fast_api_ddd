from __future__ import annotations

from sqlalchemy.orm.session import Session

from account.adapter import repositories as account_repo
from backbone.infrastructure.databases.postgres_connection import DEFAULT_SESSION_FACTORY
from backbone.service_layer.abstract_unit_of_work import AbstractUnitOfWork


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.user = account_repo.SqlalchemyUserRepository(self.session)
        self.a = account_repo.SqlalchemyUserRepository(self.session)
        self.b = account_repo.SqlalchemyUserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def repositories(self):
        repos = []
        try:
            repos.append(self.user)
            repos.append(self.a)
            repos.append(self.b)
        except:
            pass
        return repos
