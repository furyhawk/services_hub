# coding: utf-8

"""
    Merged API Services

    This is a merged OpenAPI specification containing multiple API services

    The version of the OpenAPI document: 2025.05.17
    Contact: feedback@data.gov.sg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.twenty_four_hr_forecast_get200_response_data_area_metadata_inner import TwentyFourHrForecastGet200ResponseDataAreaMetadataInner
from openapi_server.models.two_hr_forecast_get200_response_data_items_inner import TwoHrForecastGet200ResponseDataItemsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TwoHrForecastGet200ResponseData(BaseModel):
    """
    TwoHrForecastGet200ResponseData
    """ # noqa: E501
    area_metadata: Optional[List[TwentyFourHrForecastGet200ResponseDataAreaMetadataInner]] = None
    items: Optional[List[TwoHrForecastGet200ResponseDataItemsInner]] = None
    pagination_token: Optional[StrictStr] = Field(default=None, description="Token to retrieve next page if exists", alias="paginationToken")
    __properties: ClassVar[List[str]] = ["area_metadata", "items", "paginationToken"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TwoHrForecastGet200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in area_metadata (list)
        _items = []
        if self.area_metadata:
            for _item in self.area_metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['area_metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TwoHrForecastGet200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "area_metadata": [TwentyFourHrForecastGet200ResponseDataAreaMetadataInner.from_dict(_item) for _item in obj.get("area_metadata")] if obj.get("area_metadata") is not None else None,
            "items": [TwoHrForecastGet200ResponseDataItemsInner.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "paginationToken": obj.get("paginationToken")
        })
        return _obj


