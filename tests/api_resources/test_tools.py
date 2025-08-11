# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from relaxai_test import RelaxaiTest, AsyncRelaxaiTest
from relaxai_test.types import ToolScrapResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_scrap(self, client: RelaxaiTest) -> None:
        tool = client.tools.scrap(
            query="query",
            urls=["string"],
        )
        assert_matches_type(ToolScrapResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_scrap(self, client: RelaxaiTest) -> None:
        response = client.tools.with_raw_response.scrap(
            query="query",
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolScrapResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_scrap(self, client: RelaxaiTest) -> None:
        with client.tools.with_streaming_response.scrap(
            query="query",
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolScrapResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_scrap(self, async_client: AsyncRelaxaiTest) -> None:
        tool = await async_client.tools.scrap(
            query="query",
            urls=["string"],
        )
        assert_matches_type(ToolScrapResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_scrap(self, async_client: AsyncRelaxaiTest) -> None:
        response = await async_client.tools.with_raw_response.scrap(
            query="query",
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolScrapResponse, tool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_scrap(self, async_client: AsyncRelaxaiTest) -> None:
        async with async_client.tools.with_streaming_response.scrap(
            query="query",
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolScrapResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
