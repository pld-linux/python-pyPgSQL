%define 	module	pyPgSQL

Summary:	Python DB-API 2.0 PostgreSQL module
Summary(pl):	Modu³ PostgreSQL dla Pythona zgodny z DB-API 2.0
Name:		python-%{module}
Version:	2.4
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pypgsql/%{module}-%{version}.tar.gz
# Source0-md5:	56d4003e5192de9a09de468a7641bd11
URL:		http://pypgsql.sourceforge.net/
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	python-devel >= 2.0
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

%description -l pl
pyPgSQL to pakiet dwóch modu³ów dostarczaj±cych zgodny z Python DB-API
2.0 interfejs do baz danych PostgreSQL. Pierwszy modu³, libpq,
eksportuje API C PostgreSQL-a do Pythona. Ten modu³ jest napisany w C
i mo¿e byæ wkompilowany w Pythona lub ³adowany dynamicznie na
¿±danie. Drugi modu³, PgSQL, dostarcza zgodny z DB-API 2.0 interfejs
oraz wsparcie dla ró¿nych typów danych PostgreSQL-a, takich jak INT8,
NUMERIC, MONEY, BOOL, ARRAYS itp. Ten modu³ jest napisany w Pythonie.

%prep
%setup -q -n pypgsql

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO examples/*.py
%dir %{py_sitedir}/%{module}
%dir %{py_sitedir}/%{module}/libpq
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/libpq/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/libpq/*.so
