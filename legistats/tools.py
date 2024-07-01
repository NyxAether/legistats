import re


def fusion_url(main_url: str, sub_url: str) -> str:
    main_p = re.compile(r"(.*/)index.html")
    sub_p = re.compile(r"(\.\./)?(.*)")
    fusion_p = re.compile(r"((/[^/]+)\2)")

    new_main_res = main_p.search(main_url)
    assert new_main_res is not None
    new_main_url = new_main_res.group(1)

    new_sub_res = sub_p.search(sub_url)
    assert new_sub_res is not None
    new_sub_url = new_sub_res.group(2)

    fusion_url = new_main_url + new_sub_url

    return fusion_p.sub(r"\2", fusion_url)
