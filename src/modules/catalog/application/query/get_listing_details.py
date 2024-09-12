from dataclasses import dataclass

from sqlalchemy.orm import Session

from modules.catalog.application import catalog_module
from modules.catalog.application.query.model_mappers import map_listing_model_to_dao
from modules.catalog.infrastructure.listing_repository import ListingModel
from seedwork.application.queries import Query
from seedwork.application.query_handlers import QueryResult
from seedwork.utils.common_types import GenericUUID, Money, UUID, datetime, Decimal


class GetListingDetails(Query):
    listing_id: GenericUUID


@catalog_module.handler(GetListingDetails)
def get_listing_details(query: GetListingDetails, session: Session) -> QueryResult:
    row = session.query(ListingModel).filter_by(id=query.listing_id).one()
    details = map_listing_model_to_dao(row)
    return details
