from pytest import fixture

from legistats.collectstats import Collector


@fixture
def collector() -> Collector:
    return Collector(
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/index.html"
    )


def test_accro(collector: Collector) -> None:
    accros = collector.accros
    assert len(accros) == 22
    assert accros["FI"] == "La France insoumise"


def test_departments(collector: Collector) -> None:
    departments = collector.departments
    assert len(departments) == 107
    assert departments[0].code == "01"
    assert departments[0].nom == "Ain"
    assert departments[0].url == (
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/84/01/index.html"
    )


def test_circos(collector: Collector) -> None:
    circos = collector.circos
    assert len(circos) == 577
    assert circos[0].code == "0101"
    assert circos[0].nom == "1ère circonscription"
