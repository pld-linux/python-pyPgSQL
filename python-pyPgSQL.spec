
%include	/usr/lib/rpm/macros.python
%define 	module pyPgSQL

Summary:	Python DB-API 2.0 PostgreSQL module
Name:		python-%{module}
Version:	2.4
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pypgsql/%{module}-%{version}.tar.gz
# Source0-md5:	56d4003e5192de9a09de468a7641bd11
URL:		http://pypgsql.sourceforge.net/
Requires:	postgresql-libs
%pyrequires_eq	python-modules
Requires:	python-mx-DateTime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python DB-API 2.0 PostgreSQL module.

%prep
%setup -q -n pypgsql

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
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
