Name:		python-proton-core
Version:	0.7.0
Release:	1
URL: https://github.com/ProtonVPN/python-proton-core
Source0: https://github.com/ProtonVPN/python-proton-core/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	The proton-core component contains core logic used by other Proton components.
License:	GPL-3.0
Group:		Development/Python
BuildRequires:	pkgconfig(python)
BuildRequires: python%{pyver}dist(aiohttp)
BuildRequires: python%{pyver}dist(bcrypt)
BuildRequires: python%{pyver}dist(pyopenssl)
BuildRequires: python%{pyver}dist(python-gnupg)
BuildRequires: python%{pyver}dist(requests)
BuildRequires: python%{pyver}dist(importlib-metadata)
BuildRequires: python%{pyver}dist(setuptools)
BuildRequires: python%{pyver}dist(pyotp)
BuildRequires: git
BuildSystem:	python
BuildArch:	noarch
Requires:	python%{pyver}dist(aiohttp)
Requires:       python%{pyver}dist(bcrypt)
Requires:       python%{pyver}dist(python-gnupg)
Requires:       python%{pyver}dist(importlib-metadata)
Requires:       python%{pyver}dist(pyopenssl)
Requires:       python%{pyver}dist(requests)

%description
The proton-core component contains core logic used by the other Proton components, necessary for the Proton VPN app.



%files
%{py_sitedir}/proton
%{py_sitedir}/proton_core-*.egg-info
