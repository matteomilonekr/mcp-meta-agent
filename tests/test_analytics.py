"""Tests for analytics tools."""

from __future__ import annotations

import json

import httpx
import respx

from meta_ads_mcp.models.common import META_GRAPH_URL
from meta_ads_mcp.tools.analytics import (
    get_insights,
    compare_performance,
    export_insights,
    get_daily_trends,
    get_attribution_data,
)
from tests.conftest import make_meta_response

SAMPLE_INSIGHT = {
    "impressions": "10000",
    "clicks": "500",
    "spend": "150.50",
    "ctr": "5.0",
    "cpc": "0.30",
    "cpm": "15.05",
    "reach": "8000",
    "frequency": "1.25",
    "actions": [{"action_type": "lead", "value": "20"}],
}


# ── get_insights ─────────────────────────────────────────────────

async def test_get_insights_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[SAMPLE_INSIGHT]))
    )
    result = await get_insights(object_id="camp_1", ctx=mock_ctx)
    assert "Insights" in result
    assert "camp_1" in result


async def test_get_insights_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[SAMPLE_INSIGHT]))
    )
    result = await get_insights(object_id="camp_1", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "insights" in parsed


async def test_get_insights_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await get_insights(object_id="camp_1", ctx=mock_ctx)
    assert "No insights" in result


async def test_get_insights_custom_time_range(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[SAMPLE_INSIGHT]))
    )
    result = await get_insights(
        object_id="camp_1", date_preset=None,
        time_range_start="2026-01-01", time_range_end="2026-01-31",
        ctx=mock_ctx,
    )
    assert "camp_1" in result


# ── compare_performance ──────────────────────────────────────────

async def test_compare_performance_markdown(mock_api, mock_ctx):
    for oid in ["camp_1", "camp_2"]:
        mock_api.get(f"{META_GRAPH_URL}/{oid}/insights").mock(
            return_value=httpx.Response(200, json=make_meta_response(data=[
                {"impressions": "5000", "clicks": "200", "spend": "50", "ctr": "4.0", "cpc": "0.25", "conversions": "10", "object_id": oid},
            ]))
        )
    result = await compare_performance(object_ids="camp_1,camp_2", ctx=mock_ctx)
    assert "Comparison" in result


async def test_compare_performance_too_few_ids(mock_ctx):
    result = await compare_performance(object_ids="camp_1", ctx=mock_ctx)
    assert "at least 2" in result.lower()


async def test_compare_performance_json(mock_api, mock_ctx):
    for oid in ["camp_1", "camp_2"]:
        mock_api.get(f"{META_GRAPH_URL}/{oid}/insights").mock(
            return_value=httpx.Response(200, json=make_meta_response(data=[
                {"impressions": "5000", "clicks": "200"},
            ]))
        )
    result = await compare_performance(
        object_ids="camp_1,camp_2", response_format="json", ctx=mock_ctx,
    )
    parsed = json.loads(result)
    assert "comparison" in parsed


# ── export_insights ──────────────────────────────────────────────

async def test_export_insights_csv(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"impressions": "1000", "clicks": "50", "spend": "10.00"},
        ]))
    )
    result = await export_insights(object_id="camp_1", export_format="csv", ctx=mock_ctx)
    assert "impressions" in result  # CSV header
    assert "1000" in result


async def test_export_insights_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"impressions": "1000"},
        ]))
    )
    result = await export_insights(object_id="camp_1", export_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert isinstance(parsed, list)


async def test_export_insights_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await export_insights(object_id="camp_1", ctx=mock_ctx)
    assert "No data" in result


# ── get_daily_trends ─────────────────────────────────────────────

async def test_daily_trends_markdown(mock_api, mock_ctx):
    days = [
        {"date_start": "2026-01-01", "impressions": "1000", "clicks": "50", "spend": "10", "ctr": "5.0"},
        {"date_start": "2026-01-02", "impressions": "1200", "clicks": "60", "spend": "12", "ctr": "5.0"},
        {"date_start": "2026-01-03", "impressions": "1500", "clicks": "80", "spend": "15", "ctr": "5.3"},
    ]
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=days))
    )
    result = await get_daily_trends(object_id="camp_1", ctx=mock_ctx)
    assert "Trends" in result
    assert "increasing" in result or "stable" in result or "decreasing" in result


async def test_daily_trends_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await get_daily_trends(object_id="camp_1", ctx=mock_ctx)
    assert "No trend" in result


async def test_daily_trends_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[
            {"date_start": "2026-01-01", "impressions": "1000", "clicks": "50", "spend": "10", "ctr": "5.0"},
        ]))
    )
    result = await get_daily_trends(object_id="camp_1", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "trends" in parsed


# ── get_attribution_data ─────────────────────────────────────────

async def test_attribution_data_markdown(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[{
            "impressions": "10000",
            "clicks": "500",
            "spend": "150.50",
            "actions": [
                {"action_type": "link_click", "value": "450"},
                {"action_type": "lead", "value": "20"},
            ],
        }]))
    )
    result = await get_attribution_data(object_id="camp_1", ctx=mock_ctx)
    assert "Attribution" in result
    assert "lead" in result


async def test_attribution_data_json(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[SAMPLE_INSIGHT]))
    )
    result = await get_attribution_data(object_id="camp_1", response_format="json", ctx=mock_ctx)
    parsed = json.loads(result)
    assert "attribution" in parsed


async def test_attribution_data_empty(mock_api, mock_ctx):
    mock_api.get(f"{META_GRAPH_URL}/camp_1/insights").mock(
        return_value=httpx.Response(200, json=make_meta_response(data=[]))
    )
    result = await get_attribution_data(object_id="camp_1", ctx=mock_ctx)
    assert "No attribution" in result
