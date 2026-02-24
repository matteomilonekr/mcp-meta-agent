"""Tests for _helpers.py and server.py."""

from __future__ import annotations

import pytest

from meta_ads_mcp.tools._helpers import get_client, get_auth, normalize_account_id, safe_get
from tests.conftest import FakeMCPContext


# ── normalize_account_id ─────────────────────────────────────────

def test_normalize_adds_prefix():
    assert normalize_account_id("123456") == "act_123456"


def test_normalize_keeps_prefix():
    assert normalize_account_id("act_123456") == "act_123456"


def test_normalize_strips_whitespace():
    assert normalize_account_id("  act_123  ") == "act_123"


# ── safe_get ─────────────────────────────────────────────────────

def test_safe_get_existing_key():
    assert safe_get({"a": 1}, "a") == 1


def test_safe_get_missing_key():
    assert safe_get({"a": 1}, "b", "default") == "default"


def test_safe_get_none_value_returns_default():
    assert safe_get({"a": None}, "a", "fallback") == "fallback"


# ── get_client / get_auth ────────────────────────────────────────

async def test_get_client_from_ctx(mock_ctx):
    client = get_client(mock_ctx)
    assert client is not None


async def test_get_auth_from_ctx(mock_ctx):
    auth = get_auth(mock_ctx)
    assert auth is not None


def test_get_client_none_raises():
    with pytest.raises(RuntimeError, match="MCP context required"):
        get_client(None)


def test_get_auth_none_raises():
    with pytest.raises(RuntimeError, match="MCP context required"):
        get_auth(None)
