Summary:	GNOME http client library
Summary(pl):	Biblioteka funkcji klienta http
Name:		libghttp
Version:	1.0.4
Release:	1
Group:		X11/GNOME/Libraries
Group(pl):	X11/GNOME/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Library for making HTTP 1.1 requests.

%description -l pl
Biblioteka funkcji umo¿liwiaj±cych realizacjê protoko³u HTTP 1.1

%package devel
Summary:	GNOME http client development
Summary(pl):	Biblioteki i pliki nag³owkowe libghttp
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and includes files you can use for libghttp development

%description devel -l pl
Biblioteki i pliki nag³owkowe potrzebne do programowania z wykorzystaniem 
libghttp

%package static
Summary:	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME http client static library.

%description static -l pl
Wersja statyczna biblioteki libghttp

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDCONFIG="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
