#!/usr/bin/env python3
# Verified with NVIDIA Nemotron 120B Tier 1 Worker
"""
Unit tests for Worker MCP Server & CLI components.
"""

import os
import sys
import unittest
from pathlib import Path

# Add scripts directory to python path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from worker_mcp import (
    load_profiles,
    resolve_profile,
    sanitize_and_resolve_path,
    find_repo_root,
    MODEL_SETTINGS_PATH,
    MODEL_METADATA_PATH
)


class TestWorkerEcosystem(unittest.TestCase):

    def test_load_profiles(self):
        config = load_profiles()
        self.assertIn("profiles", config)
        self.assertIn("minimax-m3", config["profiles"])
        self.assertIn("nemotron-550b", config["profiles"])
        self.assertIn("glm-5.2", config["profiles"])
        self.assertIn("nemotron-120b", config["profiles"])
        self.assertIn("cohere-code", config["profiles"])
        self.assertEqual(config.get("default_profile"), "minimax-m3")
        self.assertIn("fallback_chain", config)

    def test_resolve_profile_default(self):
        p_name, profile, _ = resolve_profile("minimax-m3")
        self.assertEqual(p_name, "minimax-m3")
        self.assertEqual(profile["provider"], "openrouter")
        self.assertIn("openrouter.ai", profile["api_base"])

    def test_resolve_profile_nemotron(self):
        p_name, profile, _ = resolve_profile("nemotron-120b")
        self.assertEqual(p_name, "nemotron-120b")
        self.assertEqual(profile["provider"], "openrouter")

    def test_sanitize_and_resolve_path_safe(self):
        repo_root = find_repo_root()
        safe_path = sanitize_and_resolve_path(repo_root, "scripts/worker_mcp.py")
        self.assertTrue(str(safe_path).startswith(str(repo_root)))

    def test_sanitize_and_resolve_path_traversal_attack(self):
        repo_root = find_repo_root()
        with self.assertRaises(ValueError):
            sanitize_and_resolve_path(repo_root, "../../etc/passwd")

    def test_model_settings_metadata_files_present(self):
        self.assertTrue(MODEL_SETTINGS_PATH.is_file(), "config/.aider.model.settings.yml missing!")
        self.assertTrue(MODEL_METADATA_PATH.is_file(), "config/.aider.model.metadata.json missing!")


if __name__ == "__main__":
    unittest.main()
