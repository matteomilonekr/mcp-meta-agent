"""Tests for campaign tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.campaigns import (
    list_campaigns,
    create_campaign,
    update_campaign,
    pause_campaign,
    resume_campaign,
    delete_campaign,
)
from tests.conftest import make_meta_response, make_create_response, make_meta_error

ACCOUNT = "act_111"


# ── list_campaigns ───────────────────────────────────────────────

async def test_list_campaigns_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/campaigns").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "camp_1", "name": "Spring Sale", "objective": "OUTCOME_SALES", "effective_status": "ACTIVE", "daily_budget": "5000"},
        ]))
    )
    result = await list_campaigns(account_id="111", ctx=mock_ctx)
    assert "Spring Sale" in result
    assert "Campaigns" in result


async def test_list_campaigns_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/campaigns").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "camp_1", "name": "Test", "objective": "OUTCOME_TRAFFIC", "effective_status": "PAUSED", "daily_budget": "1000"},
        ]))
    )
    result = await list_campaigns(account_id="111", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "campaigns" in parsed
    assert parsed["campaigns"][0]["name"] == "Test"


async def test_list_campaigns_with_status_filter(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/campaigns").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_campaigns(account_id="111", status="ACTIVE", ctx=mock_ctx)
    assert "Campaigns (0/0)" in result


# ── create_campaign ──────────────────────────────────────────────

async def test_create_campaign_success(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/campaigns").mock(
        return_value=httpx.Response(200, json=make_create_response("camp_new_1"))
    )
    result = await create_campaign(
        account_id="111", name="New Campaign", objective="OUTCOME_LEADS",
        daily_budget=5000, ctx=mock_ctx,
    )
    assert "camp_new_1" in result
    assert "PAUSED" in result


async def test_create_campaign_invalid_objective(mock_ctx):
    try:
        await create_campaign(
            account_id="111", name="Bad", objective="INVALID_OBJECTIVE", ctx=mock_ctx,
        )
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


# ── update_campaign ──────────────────────────────────────────────

async def test_update_campaign_success(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await update_campaign(campaign_id="camp_1", name="Updated Name", ctx=mock_ctx)
    assert "Updated Name" in result
    assert "updated" in result.lower()


async def test_update_campaign_no_changes(mock_ctx):
    result = await update_campaign(campaign_id="camp_1", ctx=mock_ctx)
    assert "No updates" in result


# ── pause_campaign ───────────────────────────────────────────────

async def test_pause_campaign(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await pause_campaign(campaign_id="camp_1", ctx=mock_ctx)
    assert "paused" in result.lower()


# ── resume_campaign ──────────────────────────────────────────────

async def test_resume_campaign(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await resume_campaign(campaign_id="camp_1", ctx=mock_ctx)
    assert "ACTIVE" in result


# ── delete_campaign ──────────────────────────────────────────────

async def test_delete_campaign(mock_api, mock_ctx):
    mock_api.delete(f"{META_GRAPH_URL}/camp_1").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    result = await delete_campaign(campaign_id="camp_1", ctx=mock_ctx)
    assert "deleted" in result.lower()
