from __future__ import annotations

from dataclasses import dataclass
from email.message import Message

from typing_extensions import TypedDict


class SPDXLicenseDictT(TypedDict, total=False):
    isDeprecatedLicenseId: bool
    detailsUrl: str
    name: str
    licenseId: str
    isOsiApproved: bool
    isFsfLibre: bool  # Can be missing


class SPDXLicenseListT(TypedDict):
    licenseListVersion: str
    licenses: list[SPDXLicenseDictT]
    releaseDate: str


@dataclass
class SPDXLicense:
    license_id: str
    name: str
    details_url: str
    is_osi_approved: bool
    is_deprecated_license_id: bool
    is_fsf_libre: bool

    def __str__(self) -> str:
        return "{}(license_id='{}', name='{}')".format(
            self.__class__.__qualname__, self.license_id, self.name)

    @classmethod
    def from_json(cls, json_dict: SPDXLicenseDictT) -> SPDXLicense:
        return cls(
            license_id=json_dict["licenseId"],
            name=json_dict["name"],
            details_url=json_dict["detailsUrl"],
            is_osi_approved=json_dict["isOsiApproved"],
            is_deprecated_license_id=json_dict["isDeprecatedLicenseId"],
            is_fsf_libre=json_dict.get("isFsfLibre", False),
        )


class SPDXLicenseList:
    def __init__(
            self,
            license_list: list[SPDXLicense],
            license_list_version: str,
            release_date: str,
    )  -> None:
        self._license_list = license_list
        self.license_list_version = license_list_version
        self.release_date = release_date
        self._map_license_id: dict[str, SPDXLicense] = {}
        self._map_license_name: dict[str, SPDXLicense] = {}
        self._build_mapping_dicts()

    def __repr__(self) -> str:
        return "{}(version='{}', release_date='{}', #licenses={})".format(
            self.__class__.__qualname__,
            self.license_list_version, self.release_date,
            len(self._license_list))

    def _build_mapping_dicts(self) -> None:
        for license in self._license_list:
            self._map_license_id[license.license_id.lower()] = license
            self._map_license_name[license.name.lower()] = license

    def get_license_by_id(self, license_id: str) -> SPDXLicense | None:
        return self._map_license_id.get(license_id.lower())

    def get_license_by_name(self, license_name: str) -> SPDXLicense | None:
        return self._map_license_name.get(license_name.lower())

    @classmethod
    def from_json(cls, json_dict: SPDXLicenseListT) -> SPDXLicenseList:
        return cls(
            license_list=[
                SPDXLicense.from_json(license_dict)
                for license_dict in json_dict["licenses"]],
            license_list_version=json_dict["licenseListVersion"],
            release_date=json_dict["releaseDate"],
        )


class LicenseInformation:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_classifier(cls, message: Message) -> LicenseInformation:
        classifier: list[str] = []
        for key, value in message.items():
            if key != 'Classifier' or not value.startswith('License'):
                continue
            classifier.append(value)
        pass

    @classmethod
    def from_metadata(cls, metadata: str) -> LicenseInformation:
        pass
