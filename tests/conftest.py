"""Shared test fixtures for Meta Ads MCP."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
import httpx
import respx

from meta_ads_mcp.auth import AuthManager, MetaAuthConfig
from meta_ads_mcp.client import MetaAdsClient


@pytest.fixture
def auth_config() -> MetaAuthConfig:
    return MetaAuthConfig(
        access_token="test_token_123",
        app_id="test_app_id",
        app_secret="test_app_secret",
    )


@pytest.fixture
def auth_manager(auth_config: MetaAuthConfig) -> AuthManager:
    return AuthManager(auth_config)


@pytest.fixture
def mock_api():
    """Activate respx mock for all httpx requests."""
    with respx.mock(assert_all_called=False) as mock:
        yield mock


@pytest.fixture
async def meta_client(auth_manager: AuthManager) -> MetaAdsClient:
    client = MetaAdsClient(auth_manager)
    yield client
    await client.close()


# ── Mock MCP Context ─────────────────────────────────────────────


class FakeMCPContext:
    """Minimal fake MCP Context for tool testing."""

    def __init__(self, client: MetaAdsClient, auth: AuthManager) -> None:
        self.request_context = MagicMock()
        self.request_context.lifespan_state = {
            "meta_client": client,
            "auth": auth,
        }


@pytest.fixture
async def mock_ctx(auth_manager: AuthManager) -> FakeMCPContext:
    """Provide a fake MCP context with a real MetaAdsClient (HTTP mocked by respx)."""
    client = MetaAdsClient(auth_manager)
    ctx = FakeMCPContext(client, auth_manager)
    yield ctx
    await client.close()


# ── Response Factories ───────────────────────────────────────────


def make_meta_response(
    data: list[dict[str, Any]] | None = None,
    paging: dict[str, Any] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    """Build a standard Meta Graph API list response."""
    resp: dict[str, Any] = {}
    if data is not None:
        resp["data"] = data
    if paging is not None:
        resp["paging"] = paging
    resp.update(extra)
    return resp


def make_meta_error(
    message: str = "An error occurred",
    error_type: str = "OAuthException",
    code: int = 100,
    error_subcode: int = 0,
) -> dict[str, Any]:
    """Build a Meta Graph API error response."""
    error: dict[str, Any] = {
        "message": message,
        "type": error_type,
        "code": code,
    }
    if error_subcode:
        error["error_subcode"] = error_subcode
    return {"error": error}


def make_create_response(object_id: str = "123456789") -> dict[str, Any]:
    """Build a standard creation success response."""
    return {"id": object_id}
