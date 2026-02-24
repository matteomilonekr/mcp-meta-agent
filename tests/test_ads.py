"""Tests for ad tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.ads import list_ads, create_ad, update_ad, delete_ad
from tests.conftest import make_meta_response, make_create_response

ACCOUNT = "act_111"


# ── list_ads ─────────────────────────────────────────────────────

async def test_list_ads_by_account(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/ads").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "ad_1", "name": "Ad One", "effective_status": "ACTIVE", "adset_id": "adset_1", "creative": {"id": "cr_1"}},
        ]))
    )
    result = await list_ads(account_id="111", ctx=mock_ctx)
    assert "Ad One" in result


async def test_list_ads_by_ad_set(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/adset_1/ads").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_ads(ad_set_id="adset_1", ctx=mock_ctx)
    assert "Ads (0/0)" in result


async def test_list_ads_no_parent(mock_ctx):
    result = await list_ads(ctx=mock_ctx)
    assert "Error" in result


async def test_list_ads_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/ads").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "ad_1", "name": "Ad", "effective_status": "PAUSED", "adset_id": "as1", "creative": {}},
        ]))
    )
    result = await list_ads(campaign_id="camp_1", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "ads" in parsed


# ── create_ad ────────────────────────────────────────────────────

async def test_create_ad_success(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/ads").mock(
        return_value=httpx.Response(200, json=make_create_response("ad_new"))
    )
    result = await create_ad(
        ad_set_id="adset_1", account_id="111", name="New Ad",
        creative_id="cr_1", ctx=mock_ctx,
    )
    assert "ad_new" in result
    assert "PAUSED" in result


# ── update_ad ────────────────────────────────────────────────────

async def test_update_ad(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/ad_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await update_ad(ad_id="ad_1", name="Renamed Ad", ctx=mock_ctx)
    assert "Renamed Ad" in result


async def test_update_ad_no_changes(mock_ctx):
    result = await update_ad(ad_id="ad_1", ctx=mock_ctx)
    assert "No updates" in result


# ── delete_ad ────────────────────────────────────────────────────

async def test_delete_ad(mock_api, mock_ctx):
    mock_api.delete(f"{META_GRAPH_URL}/ad_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await delete_ad(ad_id="ad_1", ctx=mock_ctx)
    assert "deleted" in result.lower()
