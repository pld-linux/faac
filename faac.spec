#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_with	sse2		# SSE2 instructions

%ifarch %{x8664} x32 pentium4
%define	with_sse2	1
%endif
Summary:	Freeware Advanced Audio Codec
Summary(pl.UTF-8):	Freeware Advanced Audio Codec - darmowy zaawansowany kodek dźwięku
Name:		faac
Version:	1.31.1
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
#Source0Download: https://github.com/knik0/faac/releases
Source0:	https://github.com/knik0/faac/archive/faac-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a3f8194516769cfc3f8743364cc57824
URL:		https://faac.sourceforge.net/
BuildRequires:	autoconf >= 2.69
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
%setup -q -n faac-faac-%{version}

%if %{without sse2}
%{__sed} -i -e '/^common_CFLAGS += -msse2$/d' libfaac/Makefile.am
%endif

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfaac*.la

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
%ghost %{_libdir}/libfaac.so.0
%attr(755,root,root) %{_libdir}/libfaac_drm.so.*.*.*
%ghost %{_libdir}/libfaac_drm.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libfaac.so
%{_libdir}/libfaac_drm.so
%{_includedir}/faac*.h
%{_pkgconfigdir}/faac.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfaac.a
%{_libdir}/libfaac_drm.a
%endif
