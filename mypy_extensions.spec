#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mypy_extensions
Version  : 0.4.3
Release  : 19
URL      : https://files.pythonhosted.org/packages/63/60/0582ce2eaced55f65a4406fc97beba256de4b7a95a0034c6576458c6519f/mypy_extensions-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/60/0582ce2eaced55f65a4406fc97beba256de4b7a95a0034c6576458c6519f/mypy_extensions-0.4.3.tar.gz
Summary  : Experimental type system extensions for programs checked with the mypy typechecker.
Group    : Development/Tools
License  : MIT
Requires: mypy_extensions-license = %{version}-%{release}
Requires: mypy_extensions-python = %{version}-%{release}
Requires: mypy_extensions-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===============
        
        The "mypy_extensions" module defines experimental extensions to the
        standard "typing" module that are supported by the mypy typechecker.

%package license
Summary: license components for the mypy_extensions package.
Group: Default

%description license
license components for the mypy_extensions package.


%package python
Summary: python components for the mypy_extensions package.
Group: Default
Requires: mypy_extensions-python3 = %{version}-%{release}

%description python
python components for the mypy_extensions package.


%package python3
Summary: python3 components for the mypy_extensions package.
Group: Default
Requires: python3-core
Provides: pypi(mypy_extensions)

%description python3
python3 components for the mypy_extensions package.


%prep
%setup -q -n mypy_extensions-0.4.3
cd %{_builddir}/mypy_extensions-0.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588359972
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mypy_extensions
cp %{_builddir}/mypy_extensions-0.4.3/LICENSE %{buildroot}/usr/share/package-licenses/mypy_extensions/46cff502e1fd3dbe274f10467b70d3dcf82ed673
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mypy_extensions/46cff502e1fd3dbe274f10467b70d3dcf82ed673

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
