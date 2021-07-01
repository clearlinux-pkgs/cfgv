#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cfgv
Version  : 3.3.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/02/a9/19a33d254b54fbf105208bfbb4ecbce1b42a40f970e39db8f8186fdcc171/cfgv-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/02/a9/19a33d254b54fbf105208bfbb4ecbce1b42a40f970e39db8f8186fdcc171/cfgv-3.3.0.tar.gz
Summary  : Validate configuration and produce human readable error messages.
Group    : Development/Tools
License  : MIT
Requires: cfgv-python = %{version}-%{release}
Requires: cfgv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.cfgv?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=24&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/24/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=24&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/cfgv/master.svg)](https://results.pre-commit.ci/latest/github/asottile/cfgv/master)

%package python
Summary: python components for the cfgv package.
Group: Default
Requires: cfgv-python3 = %{version}-%{release}

%description python
python components for the cfgv package.


%package python3
Summary: python3 components for the cfgv package.
Group: Default
Requires: python3-core
Provides: pypi(cfgv)

%description python3
python3 components for the cfgv package.


%prep
%setup -q -n cfgv-3.3.0
cd %{_builddir}/cfgv-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623347787
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
