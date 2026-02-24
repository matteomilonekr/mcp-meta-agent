"""Tests for account tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.account import list_ad_accounts, health_check
from tests.conftest import make_meta_response, make_meta_error


# ── list_ad_accounts ─────────────────────────────────────────────

async def test_list_ad_accounts_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me/adaccounts").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "act_111", "name": "Test Account", "account_status": 1, "currency": "USD", "timezone_name": "US/Eastern"},
        ]))
    )
    result = await list_ad_accounts(response_format="markdown", ctx=mock_ctx)
    assert "Test Account" in result
    assert "ACTIVE" in result
    assert "Ad Accounts (1)" in result


async def test_list_ad_accounts_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me/adaccounts").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "act_222", "name": "Account 2", "account_status": 2, "currency": "EUR", "timezone_name": "Europe/Rome"},
        ]))
    )
    result = await list_ad_accounts(response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert parsed["accounts"][0]["status"] == "DISABLED"


async def test_list_ad_accounts_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me/adaccounts").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_ad_accounts(ctx=mock_ctx)
    assert "Ad Accounts (0)" in result


# ── health_check ─────────────────────────────────────────────────

async def test_health_check_healthy(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me").mock(
        return_value=httpx.Response(200, json={"id": "12345", "name": "Test User"})
    )
    mock_api.get(f"{META_GRAPH_URL}/me/adaccounts").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "act_111"},
        ]))
    )
    result = await health_check(ctx=mock_ctx)
    assert "Healthy" in result
    assert "Test User" in result


async def test_health_check_unhealthy(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me").mock(
        return_value=httpx.Response(200, json=make_meta_error("Invalid token", code=190))
    )
    result = await health_check(ctx=mock_ctx)
    assert "Unhealthy" in result
