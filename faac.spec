Summary:	Freeware Advanced Audio Codec
Name:		faac
Version:	1.23.1
Release:	1
License:	LGPL 2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	75aa397a9b123a2bf6f0ce9f78db8b3d
URL:		http://www.audiocoding.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.

%package devel
Summary:	Devel files for faac
Summary(pl):	Pliki nag³ówkowe faac
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for faac.

%description devel -l pl
Pliki nag³ówkowe faac.

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

%build
sh ./bootstrap
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
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
