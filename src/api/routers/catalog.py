from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import Application, User, get_application, get_authenticated_user
from api.models.catalog import ListingIndexModel, ListingReadModel
from config.container import inject
from modules.catalog.application.command import (
    CreateListingDraftCommand,
    UpdateListingDraftCommand,
)
from modules.catalog.application.query.get_all_listings import GetAllListings
from modules.catalog.application.query.get_listing_details import GetListingDetails
from seedwork.domain.value_objects import GenericUUID, Money

"""
Inspired by https://developer.ebay.com/api-docs/sell/inventory/resources/offer/methods/createOffer
"""

router = APIRouter()


@router.get("/catalog", tags=["catalog"], response_model=ListingIndexModel)
@inject
def get_all_listings(app: Annotated[Application, Depends(get_application)]):
    """
    Shows all published listings in the catalog
    """
    query = GetAllListings()
    result = app.execute(query)
    return dict(data=result)


@router.get("/catalog/{listing_id}", tags=["catalog"], response_model=ListingReadModel)
@inject
async def get_listing_details(
    listing_id, app: Annotated[Application, Depends(get_application)]
):
    """
    Shows listing details
    """
    query = GetListingDetails(listing_id=listing_id)
    query_result = app.execute_query(query)
    return dict(data=query_result.payload)


@router.post(
    "/catalog", tags=["catalog"], status_code=201, response_model=None
)
@inject
async def create_listing(
    request_body: CreateListingDraftCommand,
    app: Annotated[Application, Depends(get_application)],
    current_user: Annotated[User, Depends(get_authenticated_user)],
):
    """
    Creates a new listing
    """
    app.execute(request_body)


@router.put(
    "/catalog/{listing_id}",
    tags=["catalog"],
    status_code=200,
    response_model=None,
)
@inject
async def update_listing(
    listing_id: GenericUUID,
    request_body: UpdateListingDraftCommand,
    app: Annotated[Application, Depends(get_application)],
    current_user: Annotated[User, Depends(get_authenticated_user)],
):
    """
    Updates a listing
    """
    app.execute(request_body)
