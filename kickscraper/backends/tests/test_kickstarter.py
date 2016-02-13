import pytest

from kickscraper.backends.kickstarter import client
from kickscraper.backends.kickstarter import models


@pytest.fixture
def k():
    return client.KickStarter()


@pytest.fixture
def p():
    return models.KickStarterProject(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


@pytest.mark.kickstarter
class TestKickStarterClient:

    def test_get_stats(self, k):
        uid = 'carrastasney/mamma-coal-reimagining-willie-nelsons-outlaw-conce'
        keys = ['pledged', 'backers_count']
        d = k._get_project_stats(uid)
        assert d['project']['id'] == 1946925378
        for k in keys:
            assert k in d['project']

    def test_get_projects(self, k):
        terms = "mamma coal"
        keys = ['total_hits', 'projects']
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        d = k.search_projects(terms)
        for k in keys:
            assert k in d
        for k in subkeys:
            assert k in d['projects'][0]


@pytest.mark.kickstarter
class TestKickStarterModel:

    def test_create(self):
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        p = models.KickStarterProject(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        p.load()
        assert p.project_json is not None
        for k in subkeys:
            assert k in p.project_json

    def test_get_id(self, p):
        assert type(p.id) == int

    def test_get_goal(self, p):
        assert type(p.goal) == float

    def test_get_pledged(self, p):
        assert type(p.pledged) == float
