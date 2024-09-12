from dataclasses import dataclass, field
from typing import Generic, TypeVar

from seedwork.domain.events import DomainEvent
from seedwork.domain.mixins import BusinessRuleValidationMixin
from seedwork.utils.common_types import GenericUUID, Money, UUID, datetime, Decimal

EntityId = TypeVar("EntityId", bound=GenericUUID)


@dataclass
class Entity(Generic[EntityId]):
    id: EntityId = field(hash=True)

    @classmethod
    def next_id(cls) -> EntityId:
        return GenericUUID.next_id()


@dataclass(kw_only=True)
class AggregateRoot(BusinessRuleValidationMixin, Entity[EntityId]):
    """Consists of 1+ entities. Spans transaction boundaries."""

    events: list = field(default_factory=list)

    def register_event(self, event: DomainEvent):
        self.events.append(event)

    def collect_events(self):
        events = self.events
        self.events = []
        return events
