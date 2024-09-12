from uuid import UUID
from seedwork.utils.common_types import GenericUUID, Money, UUID, datetime, Decimal

import pytest

from modules.catalog.application.command.create_listing_draft import (
    CreateListingDraftCommand,
    create_listing_draft,
)
from seedwork.utils.common_types import Money
from seedwork.infrastructure.repository import InMemoryRepository
from seedwork.tests.application.test_utils import FakeEventPublisher

@pytest.mark.unit
def test_create_listing_draft():
    # arrange
    listing_id = GenericUUID(int=1)
    command = CreateListingDraftCommand(
        listing_id=listing_id,
        title="foo",
        description="bar",
        ask_price=Money(1),
        seller_id=GenericUUID.next_id(),
    )
    publish = FakeEventPublisher()
    repository = InMemoryRepository()

    # act
    create_listing_draft(command, repository, publish)

    # assert
    assert repository.get_by_id(listing_id).title == "foo"
    assert publish.contains('ListingDraftCreatedEvent')
