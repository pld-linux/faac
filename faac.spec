Summary:	Freeware Advanced Audio Codec
Summary(pl):	Freeware Advanced Audio Codec - darmowy zaawansowany kodek d¼wiêku
Name:		faac
Version:	1.23.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	ef74cf6049df76fa2a99c65d1b565ad3
Patch0:		%{name}-link.patch
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%description -l pl
FAAC to biblioteka kodera ISO/MPEG 2/4 AAC stworzona dla projektu
Freeware Advanced Audio Coding (darmowego zaawansowanego kodowania
d¼wiêku).

%package devel
Summary:	Header files for faac library
Summary(pl):	Pliki nag³ówkowe biblioteki faac
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for faac library.

%description devel -l pl
Pliki nag³ówkowe biblioteki faac.

%package static
Summary:	Static faac library
Summary(pl):	Statyczna biblioteka faac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static faac library.

%description static -l pl
Statyczna biblioteka faac.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO docs/faac.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/libfaac.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
