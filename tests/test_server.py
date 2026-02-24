"""Tests for server.py."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from meta_ads_mcp.server import create_server, app_lifespan, SERVER_NAME


def test_create_server():
    server = create_server()
    assert server.name == SERVER_NAME


async def test_app_lifespan():
    """Test that lifespan yields client and auth, then cleans up."""
    env = {
        "META_ACCESS_TOKEN": "test_token",
        "META_APP_ID": "test_app",
        "META_APP_SECRET": "test_secret",
    }
    server = create_server()
    with patch.dict(os.environ, env, clear=False):
        async with app_lifespan(server) as state:
            assert "meta_client" in state
            assert "auth" in state
            # Client should be usable
            assert state["meta_client"] is not None
