from datasette.app import Datasette
import datasette_dns
import dns.resolver
from urllib.parse import urlencode
import pytest
import httpx


@pytest.mark.asyncio
async def test_plugin_is_installed():
    app = Datasette([], memory=True).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/-/plugins.json")
        assert 200 == response.status_code
        installed_plugins = {p["name"] for p in response.json()}
        assert "datasette-dns" in installed_plugins


@pytest.mark.asyncio
async def test_dns_txt_on_exception(mocker):
    m = mocker.patch.object(datasette_dns, "resolve_txt")
    m.side_effect = dns.resolver.NoAnswer
    app = Datasette([], memory=True).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get(
            "http://localhost/:memory:.json?"
            + urlencode({"sql": "select dns_txt('example.com')"})
        )
        assert response.status_code == 200
        assert (
            response.json()["rows"][0][0]
            == "The DNS response does not contain an answer to the question."
        )
