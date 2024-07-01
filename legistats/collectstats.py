import pandas as pd
import requests
from bs4 import BeautifulSoup

from legistats.data import Circo, Departement


class Collector:
    def __init__(self, url: str):
        """Collecte les informations des législatives

        Args:
            url (str): url du site gouv des législatives
        """
        self.url = url
        self._accros: pd.Series | None = None
        self._departements: list[Departement] = []
        self._circos: list[Circo] = []

    @property
    def departments(self) -> list[Departement]:
        if len(self._departements) != 0:
            return self._departements.copy()
        soup = self._parse_page(self.url)
        select_el = soup.find("select")
        options = select_el.find_all("option")[1:]
        self._departements = [
            Departement.build_from_soup(option, self.url) for option in options
        ]
        return self._departements.copy()

    @property
    def circos(self) -> list[Circo]:
        if len(self._circos) != 0:
            return self._circos.copy()
        for dep in self.departments:
            soup = self._parse_page(dep.url)
            select_el = soup.find("select")
            options = select_el.find_all("option")[1:]
            self._circos.extend(
                Circo.build_from_soup(option, self.url, dep) for option in options
            )
        return self._circos.copy()

    @property
    def accros(self) -> pd.Series:
        if self._accros is not None:
            return self._accros.copy()
        soup = self._parse_page(self.url)
        df = pd.read_html(str(soup))[0]
        self._accros = (
            df["Liste des nuances"]
            .str.split(" ", n=1, expand=True)
            .set_index(0)
            .iloc[:, 0]
        )
        return self._accros.copy()

    def _parse_page(self, url: str) -> BeautifulSoup:
        r = requests.get(url)
        r.raise_for_status()
        return BeautifulSoup(r.content, "html.parser")
