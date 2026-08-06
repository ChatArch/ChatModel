from pathlib import Path


def test_publish_workflow_is_tag_only() -> None:
    text = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch" not in text
    assert "tags:" in text
    assert '"v*"' in text


def test_publish_workflow_tag_guard_is_unconditional() -> None:
    text = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")
    guard = "      - name: Check tag matches package version\n"
    start = text.index(guard)
    end = text.index("      - name: Check PyPI version", start)
    block = text[start:end]
    assert "if: github.event_name" not in block
    assert "GITHUB_REF_NAME" in block
    assert "RELEASE_TAG" in block
