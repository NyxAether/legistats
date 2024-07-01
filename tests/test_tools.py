from legistats.tools import fusion_url


def test_fusion_url() -> None:
    assert fusion_url(
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/index.html",
        "32/02/index.html",
    ) == (
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/32/02/index.html"
    )
    assert fusion_url(
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/index.html",
        "../32/02/index.html",
    ) == (
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/32/02/index.html"
    )
    assert fusion_url(
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/index.html",
        "32/32/02/index.html",
    ) == (
        "https://www.resultats-elections.interieur.gouv.fr/"
        "legislatives2024/ensemble_geographique/32/02/index.html"
    )
