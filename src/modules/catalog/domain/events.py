from seedwork.domain.events import DomainEvent
from seedwork.utils.common_types import GenericUUID, Money, UUID, datetime, Decimal


class ListingDraftCreatedEvent(DomainEvent):
    listing_id: GenericUUID


class ListingDraftUpdatedEvent(DomainEvent):
    listing_id: GenericUUID
