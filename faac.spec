Summary:	Freeware Advanced Audio Codec
Summary(pl):	Freeware Advanced Audio Codec - darmowy zaawansowany kodek d德i瘯u
Name:		faac
Version:	1.24
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	191a457d0a7139792e5dc0c5b607b6f1
Patch0:		%{name}-link.patch
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mpeg4ip-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%description -l pl
FAAC to biblioteka kodera ISO/MPEG 2/4 AAC stworzona dla projektu
Freeware Advanced Audio Coding (darmowego zaawansowanego kodowania
d德i瘯u).

%package libs
Summary:	Freeware Advanced Audio Codec library
Summary(pl):	Freeware Advanced Audio Codec - biblioteka darmowego zaawansowanego kodeka d德i瘯u
Group:		Libraries

%description libs
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%description libs -l pl
FAAC to biblioteka kodera ISO/MPEG 2/4 AAC stworzona dla projektu
Freeware Advanced Audio Coding (darmowego zaawansowanego kodowania
d德i瘯u).

%package devel
Summary:	Header files for faac library
Summary(pl):	Pliki nag堯wkowe biblioteki faac
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for faac library.

%description devel -l pl
Pliki nag堯wkowe biblioteki faac.

%package static
Summary:	Static faac library
Summary(pl):	Statyczna biblioteka faac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%doc ChangeLog README TODO docs/faac.html
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
