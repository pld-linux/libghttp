Summary:	GNOME http client library
Summary(pl):	Biblioteka funkcji klienta http
Name:		libghttp
Version:	1.0.9
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libghttp/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for making HTTP 1.1 requests.

%description -l pl
Biblioteka funkcji umo¿liwiaj±cych realizacjê protoko³u HTTP 1.1.

%package devel
Summary:	GNOME http client development
Summary(pl):	Biblioteki i pliki nag³ówkowe libghttp
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and includes files you can use for libghttp development.

%description -l pl devel
Biblioteki i pliki nag³ówkowe potrzebne do programowania z
wykorzystaniem libghttp.

%package static
Summary:	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME http client static library.

%description -l pl static
Wersja statyczna biblioteki libghttp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
