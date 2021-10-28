#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cfgv
Version  : 3.3.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/c4/bf/d0d622b660d414a47dc7f0d303791a627663f554345b21250e39e7acb48b/cfgv-3.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/bf/d0d622b660d414a47dc7f0d303791a627663f554345b21250e39e7acb48b/cfgv-3.3.1.tar.gz
Summary  : Validate configuration and produce human readable error messages.
Group    : Development/Tools
License  : MIT
Requires: cfgv-license = %{version}-%{release}
Requires: cfgv-python = %{version}-%{release}
Requires: cfgv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.cfgv?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=24&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/24/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=24&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/cfgv/master.svg)](https://results.pre-commit.ci/latest/github/asottile/cfgv/master)

%package license
Summary: license components for the cfgv package.
Group: Default

%description license
license components for the cfgv package.


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
%setup -q -n cfgv-3.3.1
cd %{_builddir}/cfgv-3.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630086666
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cfgv
cp %{_builddir}/cfgv-3.3.1/LICENSE %{buildroot}/usr/share/package-licenses/cfgv/e40bc52991f4a8aeed9b655de7dc4f7ea9b836fe
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cfgv/e40bc52991f4a8aeed9b655de7dc4f7ea9b836fe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
