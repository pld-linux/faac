#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Freeware Advanced Audio Codec
Summary(pl.UTF-8):	Freeware Advanced Audio Codec - darmowy zaawansowany kodek dźwięku
Name:		faac
Version:	1.29.9.2
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	2b58d621fad8fda879f07b7cad8bfe10
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dos2unix
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%description -l pl.UTF-8
FAAC to biblioteka kodera ISO/MPEG 2/4 AAC stworzona dla projektu
Freeware Advanced Audio Coding (darmowego zaawansowanego kodowania
dźwięku).

%package libs
Summary:	Freeware Advanced Audio Codec library
Summary(pl.UTF-8):	Freeware Advanced Audio Codec - biblioteka darmowego zaawansowanego kodeka dźwięku
Group:		Libraries

%description libs
FAAC is an ISO/MPEG 2/4 AAC encoder library developed for the Freeware
Advanced Audio Coding project.

%description libs -l pl.UTF-8
FAAC to biblioteka kodera ISO/MPEG 2/4 AAC stworzona dla projektu
Freeware Advanced Audio Coding (darmowego zaawansowanego kodowania
dźwięku).

%package devel
Summary:	Header files for faac library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki faac
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for faac library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki faac.

%package static
Summary:	Static faac library
Summary(pl.UTF-8):	Statyczna biblioteka faac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static faac library.

%description static -l pl.UTF-8
Statyczna biblioteka faac.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%attr(755,root,root) %{_bindir}/faac
%{_mandir}/man1/faac.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libfaac.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfaac.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfaac.so
%{_libdir}/libfaac.la
%{_includedir}/faac*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfaac.a
%endif
