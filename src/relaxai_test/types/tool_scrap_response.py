# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ToolScrapResponse", "ToolScrapResponseItem"]


class ToolScrapResponseItem(BaseModel):
    error: str
    """Error message if scraping failed"""

    markdown: str

    summarize: str

    title: str

    url: str


ToolScrapResponse: TypeAlias = List[ToolScrapResponseItem]
