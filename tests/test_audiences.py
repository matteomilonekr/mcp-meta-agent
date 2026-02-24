"""Tests for audience tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.audiences import (
    list_audiences,
    create_custom_audience,
    create_lookalike,
    estimate_audience_size,
    delete_audience,
)
from tests.conftest import make_meta_response, make_create_response

ACCOUNT = "act_111"


# ── list_audiences ───────────────────────────────────────────────

async def test_list_audiences_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/customaudiences").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {
                "id": "aud_1", "name": "Website Visitors", "subtype": "WEBSITE",
                "approximate_count_lower_bound": 5000,
                "approximate_count_upper_bound": 10000,
                "operation_status": {"status": "READY"},
            },
        ]))
    )
    result = await list_audiences(account_id="111", ctx=mock_ctx)
    assert "Website Visitors" in result
    assert "5,000" in result or "5000" in result


async def test_list_audiences_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/customaudiences").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_audiences(account_id="111", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "audiences" in parsed


# ── create_custom_audience ───────────────────────────────────────

async def test_create_custom_audience(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/customaudiences").mock(
        return_value=httpx.Response(200, json=make_create_response("aud_new"))
    )
    result = await create_custom_audience(
        account_id="111", name="Checkout Visitors",
        subtype="WEBSITE", description="People who visited checkout",
        ctx=mock_ctx,
    )
    assert "aud_new" in result
    assert "WEBSITE" in result


# ── create_lookalike ─────────────────────────────────────────────

async def test_create_lookalike(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/customaudiences").mock(
        return_value=httpx.Response(200, json=make_create_response("lal_1"))
    )
    result = await create_lookalike(
        account_id="111", name="US Lookalike",
        origin_audience_id="aud_1", country="US", ratio=0.01,
        ctx=mock_ctx,
    )
    assert "lal_1" in result
    assert "US" in result


async def test_create_lookalike_invalid_ratio(mock_ctx):
    result = await create_lookalike(
        account_id="111", name="Bad Ratio",
        origin_audience_id="aud_1", country="US", ratio=0.50,
        ctx=mock_ctx,
    )
    assert "Error" in result


# ── estimate_audience_size ───────────────────────────────────────

async def test_estimate_audience_size(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/delivery_estimate").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[{
            "daily_outcomes_curve": [{"reach": 50000, "impressions": 100000, "spend": 500}],
        }]))
    )
    targeting = json.dumps({"geo_locations": {"countries": ["US"]}})
    result = await estimate_audience_size(
        account_id="111", targeting=targeting, ctx=mock_ctx,
    )
    assert "Estimate" in result
    assert "50,000" in result or "50000" in result


async def test_estimate_audience_size_no_data(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/delivery_estimate").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[{}]))
    )
    result = await estimate_audience_size(
        account_id="111", targeting="{}", ctx=mock_ctx,
    )
    assert "N/A" in result


# ── delete_audience ──────────────────────────────────────────────

async def test_delete_audience(mock_api, mock_ctx):
    mock_api.delete(f"{META_GRAPH_URL}/aud_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await delete_audience(audience_id="aud_1", ctx=mock_ctx)
    assert "deleted" in result.lower()
