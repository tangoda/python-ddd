from modules.catalog.domain.events import ListingDraftUpdatedEvent
from seedwork.infrastructure.logging import logger
from modules.catalog.application import catalog_module


@catalog_module.handler(ListingDraftUpdatedEvent)
def do_nothing_when_listing_updated(event: ListingDraftUpdatedEvent):
    logger.info(f"Message from a handler: Listing {event.listing_id} was updated")
