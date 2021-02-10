from __future__ import annotations

from .const import LICENSE_EXPR_PROPRIETARY,  LICENSE_EXPR_PUBLIC_DOMAIN


MAP_CLASSIFIER_LICENSE_EXPRESSION: dict[str, str | None] = {
    "License :: Aladdin Free Public License (AFPL)": "Aladdin",
    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication": "CC0-1.0",
    "License :: CeCILL-B Free Software License Agreement (CECILL-B)": "CECILL-B",
    "License :: CeCILL-C Free Software License Agreement (CECILL-C)": "CECILL-C",
    "License :: DFSG approved": None,  # IGNORED
    "License :: Eiffel Forum License (EFL)": "",  # EFL-1.0, EFL-2.0
    "License :: Free For Educational Use": "LicenseRef-Proprietary",
    "License :: Free For Home Use": "LicenseRef-Proprietary",
    "License :: Free To Use But Restricted": "LicenseRef-Proprietary",
    "License :: Free for non-commercial use": "LicenseRef-Proprietary",
    "License :: Freely Distributable": "LicenseRef-Proprietary",
    "License :: Freeware": "LicenseRef-Proprietary",
    "License :: GUST Font License 1.0": None,  # Not Assigned
    "License :: GUST Font License 2006-09-30": None,  # Not Assigned
    "License :: Netscape Public License (NPL)": "",  # NPL-1.0, NPL-1.1
    "License :: Nokia Open Source License (NOKOS)": "Nokia",
    "License :: OSI Approved": None,  # IGNORED
    "License :: OSI Approved :: Academic Free License (AFL)": "",  # AFL-1.1, AFT-1.2, AFL-2.0, AFL-2.1, AFL-3.0
    "License :: OSI Approved :: Apache Software License": "",  # Apache-1.0, Apache-1.1, Apache-2.0
    "License :: OSI Approved :: Apple Public Source License": "",  # APSL-1.0, APSL-1.1, APSL-1.2, APSL-2.0
    "License :: OSI Approved :: Artistic License": "",  # Artistic-1.0, Artistic-2.0
    "License :: OSI Approved :: Attribution Assurance License": "AAL",
    "License :: OSI Approved :: BSD License": "",  # many!
    "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)": "BSL-1.0",
    "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)": "CECILL-2.1",
    "License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)": "CDDL-1.0",
    "License :: OSI Approved :: Common Public License": "CPL-1.0",
    "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)": "EPL-1.0",
    "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)": "EPL-2.0",
    "License :: OSI Approved :: Eiffel Forum License": "",  # EFL-1.0, EFL-2.0
    "License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)": "EUPL-1.0",
    "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)": "EUPL-1.1",
    "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)": "EUPL-1.2",
    "License :: OSI Approved :: GNU Affero General Public License v3": "AGPL-3.0-only",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)": "AGPL-3.0-or-later",
    "License :: OSI Approved :: GNU Free Documentation License (FDL)": "",  # many!
    "License :: OSI Approved :: GNU General Public License (GPL)": "",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)": "GPL-2.0-only",
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)": "GPL-2.0-or-later",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)": "GPL-3.0-only",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)": "GPL-3.0-or-later",
    "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)": "LGPL-2.0-only",
    "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)": "LGPL-2.0-or-later",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0-only",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)": "LGPL-3.0-or-later",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)": "",  # multiple
    "License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)": "",  # multiple
    "License :: OSI Approved :: IBM Public License": "",  # multiple
    "License :: OSI Approved :: ISC License (ISCL)": "ISC",
    "License :: OSI Approved :: Intel Open Source License": "Intel",
    "License :: OSI Approved :: Jabber Open Source License": "",  # ???
    "License :: OSI Approved :: MIT License": "",  # multiple
    "License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)": "",  # ???
    "License :: OSI Approved :: MirOS License (MirOS)": "MirOS",
    "License :: OSI Approved :: Motosoto License": "Motosoto",
    "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)": "MPL-1.0",
    "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)": "MPL-1.1",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)": "MPL-2.0",
    "License :: OSI Approved :: Nethack General Public License": "",
    "License :: OSI Approved :: Nokia Open Source License": "Nokia",
    "License :: OSI Approved :: Open Group Test Suite License": "OGTSL",
    "License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)": "OSL-3.0",
    "License :: OSI Approved :: PostgreSQL License": "PostgreSQL",
    "License :: OSI Approved :: Python License (CNRI Python License)": "",  # multiple
    "License :: OSI Approved :: Python Software Foundation License": "PSF-2.0",
    "License :: OSI Approved :: Qt Public License (QPL)": "QPL-1.0",
    "License :: OSI Approved :: Ricoh Source Code Public License": "RSCPL",
    "License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)": "",  # multiple
    "License :: OSI Approved :: Sleepycat License": "Sleepycat",
    "License :: OSI Approved :: Sun Industry Standards Source License (SISSL)": "",  # multiple
    "License :: OSI Approved :: Sun Public License": "SPL-1.0",
    "License :: OSI Approved :: The Unlicense (Unlicense)": "Unlicense",
    "License :: OSI Approved :: Universal Permissive License (UPL)": "UPL-1.0",
    "License :: OSI Approved :: University of Illinois/NCSA Open Source License": "NCSA",
    "License :: OSI Approved :: Vovida Software License 1.0": "VSL-1.0",
    "License :: OSI Approved :: W3C License": "",  # multiple
    "License :: OSI Approved :: X.Net License": "Xnet",
    "License :: OSI Approved :: Zope Public License": "",  # multiple
    "License :: OSI Approved :: zlib/libpng License": "Zlib",
    "License :: Other/Proprietary License": "LicenseRef-Proprietary",
    "License :: Public Domain": "LicenseRef-Public-Domain",
    "License :: Repoze Public License": None,  # not assigned
}