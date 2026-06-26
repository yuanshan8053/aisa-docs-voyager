import importlib.util
import unittest
from pathlib import Path


def load_accept_all():
    repo = Path(__file__).resolve().parents[1]
    module_path = repo / "accept_all.py"
    spec = importlib.util.spec_from_file_location("accept_all", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return repo, module


class AcceptAllTests(unittest.TestCase):
    def test_projection_jobs_cover_two_languages_for_site_specs(self):
        repo, module = load_accept_all()

        jobs = module.projection_jobs(repo)

        self.assertEqual(len(jobs), 60)
        self.assertEqual({job.lang for job in jobs}, {"en", "zh"})
        self.assertNotIn("openapi", {job.name for job in jobs})
        self.assertTrue(all(job.enhanced.exists() for job in jobs))
        self.assertTrue(all(job.projected.exists() for job in jobs))
