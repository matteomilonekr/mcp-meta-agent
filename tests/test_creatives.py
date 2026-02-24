"""Tests for creative tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.creatives import list_creatives, create_creative, upload_image, preview_ad
from tests.conftest import make_meta_response, make_create_response

ACCOUNT = "act_111"


# ── list_creatives ───────────────────────────────────────────────

async def test_list_creatives_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/adcreatives").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"id": "cr_1", "name": "Creative A", "title": "Title", "status": "ACTIVE", "image_url": "https://example.com/img.jpg"},
        ]))
    )
    result = await list_creatives(account_id="111", ctx=mock_ctx)
    assert "Creative A" in result
    assert "Yes" in result  # has image


async def test_list_creatives_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/{ACCOUNT}/adcreatives").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await list_creatives(account_id="111", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "creatives" in parsed


# ── create_creative ──────────────────────────────────────────────

async def test_create_creative_image(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adcreatives").mock(
        return_value=httpx.Response(200, json=make_create_response("cr_new"))
    )
    result = await create_creative(
        account_id="111", name="Image Creative", page_id="page_1",
        message="Check this out", link="https://example.com",
        image_hash="abc123", headline="Great Deal", ctx=mock_ctx,
    )
    assert "cr_new" in result
    assert "LEARN_MORE" in result


async def test_create_creative_video(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adcreatives").mock(
        return_value=httpx.Response(200, json=make_create_response("cr_vid"))
    )
    result = await create_creative(
        account_id="111", name="Video Creative", page_id="page_1",
        link="https://example.com", video_id="vid_1",
        message="Watch now", ctx=mock_ctx,
    )
    assert "cr_vid" in result


async def test_create_creative_text_only(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adcreatives").mock(
        return_value=httpx.Response(200, json=make_create_response("cr_txt"))
    )
    result = await create_creative(
        account_id="111", name="Text Post", page_id="page_1",
        message="Just a text post", ctx=mock_ctx,
    )
    assert "cr_txt" in result


# ── upload_image ─────────────────────────────────────────────────

async def test_upload_image_success(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adimages").mock(
        return_value=httpx.Response(200, json={
            "images": {"img1": {"hash": "abc123hash", "url": "https://cdn.example.com/img.jpg"}},
        })
    )
    result = await upload_image(account_id="111", image_url="https://example.com/img.jpg", ctx=mock_ctx)
    assert "abc123hash" in result
    assert "uploaded" in result.lower()


async def test_upload_image_fallback_to_bytes(mock_api, mock_ctx):
    """When URL upload fails with error #3, fallback to bytes upload."""
    from tests.conftest import make_meta_error
    # First call (url) fails, second call (bytes) succeeds
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adimages").mock(
        side_effect=[
            httpx.Response(200, json=make_meta_error("App does not have capability", code=3)),
            httpx.Response(200, json={
                "images": {"bytes": {"hash": "fallback_hash", "url": "https://cdn.example.com/fallback.jpg"}},
            }),
        ]
    )
    # Mock the image download
    mock_api.get("https://example.com/img.jpg").mock(
        return_value=httpx.Response(200, content=b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)
    )
    result = await upload_image(account_id="111", image_url="https://example.com/img.jpg", ctx=mock_ctx)
    assert "fallback_hash" in result
    assert "uploaded" in result.lower()


async def test_upload_image_no_images(mock_api, mock_ctx):
    mock_api.post(f"{META_GRAPH_URL}/{ACCOUNT}/adimages").mock(
        return_value=httpx.Response(200, json={"images": {}})
    )
    result = await upload_image(account_id="111", image_url="https://example.com/img.jpg", ctx=mock_ctx)
    assert "upload response" in result.lower()


# ── preview_ad ───────────────────────────────────────────────────

async def test_preview_ad_success(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/cr_1/previews").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"body": "<div>Preview HTML</div>"},
        ]))
    )
    result = await preview_ad(creative_id="cr_1", ctx=mock_ctx)
    assert "Preview HTML" in result
    assert "DESKTOP_FEED_STANDARD" in result


async def test_preview_ad_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/cr_1/previews").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await preview_ad(creative_id="cr_1", ctx=mock_ctx)
    assert "No preview" in result
