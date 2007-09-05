#
# Conditional build:
%bcond_without	mpeg4ip		# without MPEG4 support in frontend (which requires mpeg4ip)
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Freeware Advanced Audio Codec
Summary(pl.UTF-8):	Freeware Advanced Audio Codec - darmowy zaawansowany kodek dźwięku
Name:		faac
Version:	1.25
Release:	2
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	75eaffd18ee072eaca52ae2d622bb1db
Patch0:		%{name}-link.patch
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dos2unix
BuildRequires:	libtool
%{?with_mpeg4ip:BuildRequires:	mpeg4ip-devel}
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
%setup -q -n %{name}
%patch0 -p1

# aclocal can't stand it
dos2unix configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_mpeg4ip:--without-mp4v2} \
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
