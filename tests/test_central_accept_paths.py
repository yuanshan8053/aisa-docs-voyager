import importlib.util
import unittest
from pathlib import Path


def load_central_accept():
    repo = Path(__file__).resolve().parents[1]
    module_path = repo / "ws-v2" / "central_accept.py"
    spec = importlib.util.spec_from_file_location("central_accept", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return repo, module


class CentralAcceptPathTests(unittest.TestCase):
    def test_default_paths_are_repo_relative(self):
        repo, module = load_central_accept()

        self.assertEqual(Path(module.ROOT), repo)
        self.assertEqual(Path(module.WS), repo / "ws-v2")
        self.assertEqual(Path(module.SRC), repo / "docs-mirror" / "openapi")
        self.assertEqual(Path(module.T), repo / "skill-local" / "aisa-doc-enhance" / "tools")
