"""Smoke: HF domain charter stream schema for research-space-systems."""

from __future__ import annotations

from datasets import load_dataset


def test_wikitext_stream_schema() -> None:
    rows = list(
        load_dataset(
            "Salesforce/wikitext",
            "wikitext-2-raw-v1",
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "text" in r
