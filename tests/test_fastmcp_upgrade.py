"""Tests for FastMCP compatibility and basic code execution."""

import mcp_python_interpreter.server as server


def test_server_initializes():
    """Server should expose expected name and instructions."""
    assert server.mcp.name == "Python Interpreter"
    assert server.mcp.instructions is not None


def test_run_python_code_basic(tmp_path, monkeypatch):
    """run_python_code should execute code and capture output."""
    monkeypatch.setattr(server, "WORKING_DIR", tmp_path)

    result = server.run_python_code("print('hi')")

    assert "hi" in result
