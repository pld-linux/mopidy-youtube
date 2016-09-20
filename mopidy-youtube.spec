#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module

%define 	module		mopidy_youtube
%define 	egg_name	Mopidy_Youtube
%define		pypi_name	Mopidy-Youtube
Summary:	Mopidy extension that plays sound from YouTube
Name:		mopidy-youtube
Version:	2.0.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	4105886936d766c3995a96022d52ec35
URL:		https://github.com/mopidy/mopidy-youtube
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mopidy extension that plays sound from YouTube.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
