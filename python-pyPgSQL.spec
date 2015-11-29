%define 	module	pyPgSQL

Summary:	Python DB-API 2.0 PostgreSQL module
Summary(pl.UTF-8):	Moduł PostgreSQL dla Pythona zgodny z DB-API 2.0
Name:		python-%{module}
Version:	2.5.1
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pypgsql/%{module}-%{version}.tar.gz
# Source0-md5:	82670f6f1652aa4766fdaec2cb43debd
URL:		http://pypgsql.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	postgresql-libs
%pyrequires_eq	python-modules
Requires:	python-mx-DateTime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyPgSQL is a package of two modules that provide a Python DB-API 2.0
compliant interface to PostgreSQL databases. The first module, libpq,
exports the PostgreSQL C API to Python. This module is written in C
and can be compiled into Python or can be dynamically loaded on
demand. The second module, PgSQL, provides the DB-API 2.0 compliant
interface and support for various PostgreSQL data types, such as INT8,
NUMERIC, MONEY, BOOL, ARRAYS, etc. This module is written in Python.

%description -l pl.UTF-8
pyPgSQL to pakiet dwóch modułów dostarczających zgodny z Python DB-API
2.0 interfejs do baz danych PostgreSQL. Pierwszy moduł, libpq,
eksportuje API C PostgreSQL-a do Pythona. Ten moduł jest napisany w C
i może być wkompilowany w Pythona lub ładowany dynamicznie na
żądanie. Drugi moduł, PgSQL, dostarcza zgodny z DB-API 2.0 interfejs
oraz wsparcie dla różnych typów danych PostgreSQL-a, takich jak INT8,
NUMERIC, MONEY, BOOL, ARRAYS itp. Ten moduł jest napisany w Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

find $RPM_BUILD_ROOT%{py_sitedir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog README examples/*.py
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/libpq
%{py_sitedir}/%{module}/libpq/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/libpq/*.so
