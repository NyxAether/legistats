import re

from bs4 import BeautifulSoup
from pydantic import BaseModel

from legistats.tools import fusion_url


class Departement(BaseModel):
    code: str
    nom: str
    url: str

    @classmethod
    def build_from_soup(cls, soup: BeautifulSoup, url: str) -> "Departement":
        code, nom = soup.text.strip().split(" - ")
        return cls(code=code, nom=nom, url=fusion_url(url, soup.get("value")))


class Circo(BaseModel):
    code: str
    nom: str
    departement: Departement
    url: str

    @classmethod
    def build_from_soup(
        cls, soup: BeautifulSoup, url: str, dep: Departement
    ) -> "Circo":
        res = re.search(r"(\w+) - (.*)$", soup.text.strip())
        assert res is not None
        return cls(
            code=res.group(1),
            nom=res.group(2),
            departement=dep,
            url=fusion_url(url, soup.get("value")),
        )
