"""Tests for ad set tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.ad_sets import (
    list_ad_sets,
    create_ad_set,
    update_ad_set,
    pause_ad_set,
    delete_ad_set,
)
from tests.conftest import make_meta_response, make_create_response

ACCOUNT = "act_111"


# ── list_ad_sets ─────────────────────────────────────────────────

async def test_list_ad_sets_by_account(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/adsets").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "adset_1", "name": "Ad Set A", "effective_status": "ACTIVE", "optimization_goal": "LINK_CLICKS", "daily_budget": "3000", "billing_event": "IMPRESSIONS"},
        ]))
    )
    result = await list_ad_sets(account_id="111", ctx=mock_ctx)
    assert "Ad Set A" in result


async def test_list_ad_sets_by_campaign(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/adsets").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "adset_2", "name": "Set B", "effective_status": "PAUSED", "optimization_goal": "REACH", "daily_budget": "1000", "billing_event": "IMPRESSIONS"},
        ]))
    )
    result = await list_ad_sets(campaign_id="camp_1", ctx=mock_ctx)
    assert "Set B" in result


async def test_list_ad_sets_no_parent(mock_ctx):
    result = await list_ad_sets(ctx=mock_ctx)
    assert "Error" in result


async def test_list_ad_sets_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/adsets").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_ad_sets(account_id="111", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "ad_sets" in parsed


# ── create_ad_set ────────────────────────────────────────────────

async def test_create_ad_set_success(mock_api, mock_ctx):
    # Mock campaign CBO check
    mock_api.get(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"id": "camp_1"})
    )
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adsets").mock(
        return_value=httpx.Response(200, json=make_create_response("adset_new"))
    )
    result = await create_ad_set(
        campaign_id="camp_1", account_id="111", name="New Set",
        optimization_goal="LINK_CLICKS", billing_event="IMPRESSIONS",
        daily_budget=5000, ctx=mock_ctx,
    )
    assert "adset_new" in result
    assert "PAUSED" in result


async def test_create_ad_set_cbo_skips_budget(mock_api, mock_ctx):
    # Campaign has CBO active (daily_budget set at campaign level)
    mock_api.get(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"id": "camp_1", "daily_budget": "10000"})
    )
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adsets").mock(
        return_value=httpx.Response(200, json=make_create_response("adset_cbo"))
    )
    result = await create_ad_set(
        campaign_id="camp_1", account_id="111", name="CBO Set",
        optimization_goal="LINK_CLICKS", billing_event="IMPRESSIONS",
        daily_budget=5000, ctx=mock_ctx,
    )
    assert "CBO" in result or "adset_cbo" in result


async def test_create_ad_set_with_targeting(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"id": "camp_1"})
    )
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adsets").mock(
        return_value=httpx.Response(200, json=make_create_response("adset_tgt"))
    )
    targeting = json.dumps({"geo_locations": {"countries": ["US"]}, "age_min": 25})
    result = await create_ad_set(
        campaign_id="camp_1", account_id="111", name="Targeted",
        optimization_goal="REACH", billing_event="IMPRESSIONS",
        targeting=targeting, ctx=mock_ctx,
    )
    assert "adset_tgt" in result


# ── update_ad_set ────────────────────────────────────────────────

async def test_update_ad_set(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/adset_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await update_ad_set(ad_set_id="adset_1", name="Updated Set", ctx=mock_ctx)
    assert "Updated Set" in result


async def test_update_ad_set_no_changes(mock_ctx):
    result = await update_ad_set(ad_set_id="adset_1", ctx=mock_ctx)
    assert "No updates" in result


# ── pause_ad_set ─────────────────────────────────────────────────

async def test_pause_ad_set(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/adset_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await pause_ad_set(ad_set_id="adset_1", ctx=mock_ctx)
    assert "paused" in result.lower()


# ── delete_ad_set ────────────────────────────────────────────────

async def test_delete_ad_set(mock_api, mock_ctx):
    mock_api.delete(f"{META_GRAPH_URL}/adset_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await delete_ad_set(ad_set_id="adset_1", ctx=mock_ctx)
    assert "deleted" in result.lower()
