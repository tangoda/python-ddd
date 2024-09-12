from dataclasses import dataclass

from modules.catalog.domain.events import (
    ListingDraftUpdatedEvent
)
from seedwork.domain.entities import AggregateRoot
from seedwork.utils.common_types import GenericUUID, Money, UUID, datetime, Decimal


@dataclass(kw_only=True)
class Listing(AggregateRoot):
    title: str
    description: str
    ask_price: Money
    seller_id: GenericUUID
    status = "draft"

    def change_main_attributes(self, title: str, description: str, ask_price: Money):
        self.title = title
        self.description = description
        self.ask_price = ask_price
        self.register_event(ListingDraftUpdatedEvent(listing_id=self.id))
