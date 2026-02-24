"""Tests for OAuth tools."""

from __future__ import annotations

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.oauth import (
    generate_auth_url,
    exchange_code_for_token,
    refresh_to_long_lived_token,
    get_token_info,
    validate_token,
)


# ── generate_auth_url ────────────────────────────────────────────

async def test_generate_auth_url_default(mock_ctx):
    result = await generate_auth_url(ctx=mock_ctx)
    assert "OAuth Authorization" in result
    assert "facebook.com" in result


async def test_generate_auth_url_custom_scopes(mock_ctx):
    result = await generate_auth_url(scopes="ads_read,business_management", ctx=mock_ctx)
    assert "ads_read" in result


# ── exchange_code_for_token ──────────────────────────────────────

async def test_exchange_code(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/oauth/access_token").mock(
        return_value=httpx.Response(200, json={
            "access_token": "EAAG_long_token_abcdefghijk",
            "token_type": "bearer",
            "expires_in": 5184000,
        })
    )
    result = await exchange_code_for_token(code="test_code_123", ctx=mock_ctx)
    assert "Token obtained" in result
    assert "EAAG_lon" in result  # masked token
    assert "5184000" in result


# ── refresh_to_long_lived_token ──────────────────────────────────

async def test_refresh_long_lived(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/oauth/access_token").mock(
        return_value=httpx.Response(200, json={
            "access_token": "EAAG_long_lived_token_12345",
            "token_type": "bearer",
            "expires_in": 5184000,
        })
    )
    result = await refresh_to_long_lived_token(ctx=mock_ctx)
    assert "Long-lived token" in result
    assert "60 days" in result


# ── get_token_info ───────────────────────────────────────────────

async def test_get_token_info_full(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/debug_token").mock(
        return_value=httpx.Response(200, json={
            "data": {
                "is_valid": True,
                "app_id": "test_app_id",
                "user_id": "12345",
                "scopes": ["ads_management", "ads_read"],
                "expires_at": 1700000000,
            },
        })
    )
    result = await get_token_info(ctx=mock_ctx)
    assert "Token Debug Info" in result
    assert "Yes" in result  # is_valid
    assert "ads_management" in result


async def test_get_token_info_no_app_credentials(mock_api, mock_ctx):
    # Remove app credentials to trigger fallback
    mock_ctx.request_context.lifespan_state["auth"] = type(mock_ctx.request_context.lifespan_state["auth"])(
        mock_ctx.request_context.lifespan_state["auth"].with_token("test_token_123")
    )
    # Actually just test the branch with app_id and secret set — already covered above
    # Test the /me fallback path by using a manager without app credentials
    from meta_ads_mcp.auth import AuthManager, MetaAuthConfig
    bare_config = MetaAuthConfig(access_token="test_token_123", app_id="", app_secret="")
    bare_auth = AuthManager(bare_config)
    from tests.conftest import FakeMCPContext
    from meta_ads_mcp.client import MetaAdsClient
    client = MetaAdsClient(bare_auth)
    bare_ctx = FakeMCPContext(client, bare_auth)

    mock_api.get(f"{META_GRAPH_URL}/me").mock(
        return_value=httpx.Response(200, json={"id": "12345", "name": "Test User"})
    )
    result = await get_token_info(ctx=bare_ctx)
    assert "Token Info (basic)" in result
    assert "Test User" in result
    await client.close()


# ── validate_token ───────────────────────────────────────────────

async def test_validate_token_valid(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me").mock(
        return_value=httpx.Response(200, json={"id": "12345", "name": "Test User"})
    )
    result = await validate_token(ctx=mock_ctx)
    assert "valid" in result.lower()
    assert "Test User" in result


async def test_validate_token_invalid(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/me").mock(
        return_value=httpx.Response(200, json={"error": {"message": "Invalid token", "type": "OAuthException", "code": 190}})
    )
    result = await validate_token(ctx=mock_ctx)
    assert "invalid" in result.lower()
