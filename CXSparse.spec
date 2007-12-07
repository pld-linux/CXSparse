Summary:	CXSparse: extended version of a concise sparse matrix package
Name:		CXSparse
Version:	0
Release:	1
License:	LGPL
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
CXSparse is an extended version of CSparse - a small yet
feature-rich sparse matrix package, with support for double
or complex matrices, with int or long integers.

%package devel
Summary:	Header files for amd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki amd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for amd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki amd.

%package static
Summary:	Static amd library
Summary(pl.UTF-8):	Statyczna biblioteka amd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amd library.

%description static -l pl.UTF-8
Statyczna biblioteka amd.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	F77="gfortran" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install -D Include/cs.h $RPM_BUILD_ROOT%{_includedir}/cs.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libcxsparse.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcxsparse.so
%{_libdir}/libcxsparse.la
%{_includedir}/cs.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcxsparse.a
