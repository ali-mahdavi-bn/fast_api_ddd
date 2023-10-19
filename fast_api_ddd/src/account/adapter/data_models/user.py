from __future__ import annotations

from sqlalchemy import Column, String, ForeignKey, Table, Integer, Uuid, func, DateTime

from backbone.adapter.abstract_data_model import MAPPER_REGISTRY

user_data_model = Table(
    "users",
    MAPPER_REGISTRY.metadata,
    Column("id", Integer, primary_key=True),
    Column("uuid", Uuid, unique=True),
    Column("first_name", String(100)),
    Column("last_name", String(100)),
    Column("mobile", String(100)),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime),
    Column("deleted_at", DateTime),

    schema="account"
)
