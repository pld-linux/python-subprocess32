#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Backport of the subprocess module from Python 3 for use on 2.x
Summary(pl.UTF-8):	Backport modułu subprocess z Pythona 3 do użycia w 2.x
Name:		python-subprocess32
Version:	3.5.2
Release:	1
License:	PSF v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/subprocess32/
Source0:	https://files.pythonhosted.org/packages/source/s/subprocess32/subprocess32-%{version}.tar.gz
# Source0-md5:	4bd55a9fe9504a683255c4f51b1679ae
URL:		https://github.com/google/python-subprocess32
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
Requires:	python-modules >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a backport of the subprocess standard library module from
Python 3.2 - 3.5 for use on Python 2.
        
It includes bugfixes and some new features. On POSIX systems it is
guaranteed to be reliable when used in threaded applications. It
includes timeout support from Python 3.3 and the run() API from 3.5
but otherwise matches 3.2's API.

%description -l pl.UTF-8
Ten moduł jest backportem modułu subprocess z biblioteki standardowej
Pythona 3.2 - 3.5 przeznaczonym do używania z Pythonem 2.

Zawiera poprawki błędów i kilka nowych funkcji. Na systemach zgodnych
z POSIX można go używać w aplikacjach wielowątkowych. Zawiera obsługę
limitu czasu z Pythona 3.3 oraz interfejs run() z 3.5, a poza tym
jest zgodny z API 3.2.

%prep
%setup -q -n subprocess32-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%attr(755,root,root) %{py_sitedir}/_posixsubprocess32.so
%{py_sitedir}/subprocess32.py[co]
%{py_sitedir}/subprocess32-%{version}-py*.egg-info
