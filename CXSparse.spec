Summary:	CXSparse: extended version of a concise sparse matrix package
Summary(pl.UTF-8):	CXSparse - rozszerzona wersja zwięzłego pakietu do macierzy rzadkich
Name:		CXSparse
Version:	0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/CXSparse/%{name}.tar.gz
# Source0-md5:	b8061452b75014dee69e5c5fc33cfd25
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/CXSparse/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CXSparse is an extended version of CSparse - a small yet feature-rich
sparse matrix package, with support for double or complex matrices,
with int or long integers.

%description -l pl.UTF-8
CXSparse to rozszerzona wersja CSparse - małego, ale mającego wiele
możliwości pakietu do macierzy rzadkich z obsługą macierzy typu double
i zespolonych, z liczbami int i long.

%package devel
Summary:	Header files for CXSparse library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CXSparse
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for CXSparse library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CXSparse.

%package static
Summary:	Static CXSparse library
Summary(pl.UTF-8):	Statyczna biblioteka CXSparse
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CXSparse library.

%description static -l pl.UTF-8
Statyczna biblioteka CXSparse.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/cxsparse

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/cxsparse

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/libcxsparse.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcxsparse.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcxsparse.so
%{_libdir}/libcxsparse.la
%{_includedir}/cxsparse

%files static
%defattr(644,root,root,755)
%{_libdir}/libcxsparse.a
