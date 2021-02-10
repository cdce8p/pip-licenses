"""
Changelog

- Add SPDX license data (+ license information in NOTICE)
- Bump version to 4.0.0
- Bump min_required to 3.7:
    - Use for `importlib.resources` (https://docs.python.org/3.8/library/importlib.html#module-importlib.resources)
    - Data classes
    - Better typing support (PEP 563 - Postponed evaluation of type annotations)
- Added `typing-extensions` dependency -> better type support


--
https://github.com/spdx/spdx-spec
https://github.com/spdx/license-list-data
https://pypi.org/classifiers/
https://www.python.org/dev/peps/pep-0639/#classifier-multiple-use
"""



if __name__ == '__main__':
    import json
    from pathlib import Path
    data_path = Path(__file__).parent.joinpath("data/licenses.json")
    with open(data_path) as fp:
        data = json.load(fp)
    spdx_list = SPDXLicenseList.from_json(data)
    print(spdx_list)
    print(spdx_list._license_list[0])
    print(repr(spdx_list._license_list[0]))
    breakpoint()
    pass





if __name__ == '__main__':
    import json
    from importlib import resources as importlib_resources
    fp = importlib_resources.open_text("piplicenses.data", "licenses.json")
    text = json.load(fp)
    lst = SPDXLicenseList.from_json(text)
    apache_2 = lst.get_license_by_id("Apache-2.0")
    print(lst)
    print(apache_2)
