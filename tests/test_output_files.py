"""Tests for listing and detecting output files from code execution."""

import mcp_python_interpreter.server as server


def test_run_python_code_reports_created_files(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "WORKING_DIR", tmp_path)

    code = "open('out.txt', 'w').write('data')"
    result = server.run_python_code(code)

    assert "- out.txt" in result


def test_run_python_file_reports_created_files(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "WORKING_DIR", tmp_path)

    script = tmp_path / "script.py"
    script.write_text("open('script_out.txt', 'w').write('x')")

    result = server.run_python_file(str(script))

    assert "- script_out.txt" in result


def test_list_directory_includes_non_python_files(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "WORKING_DIR", tmp_path)

    (tmp_path / "data.csv").write_text("a,b\n1,2")

    listing = server.list_directory()

    assert "data.csv" in listing
