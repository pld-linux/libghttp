Summary:     	GNOME http client library
Summary(pl):	Biblioteka funkcji klienta http
Name:        	libghttp
Version:     	1.0.2
Release:     	1
Group:       	X11/GNOME/Libraries
Group(pl):   	X11/GNOME/Biblioteki
Copyright:   	GPL
Source:      	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         	http://www.gnome.org/
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Library for making HTTP 1.1 requests.

%description -l pl
Biblioteka funkcji umo¿liwiaj±cych realizacjê protoko³u HTTP 1.1

%package devel
Summary:     	GNOME http client development
Summary(pl):	Biblioteki i pliki nag³owkowe libghttp
Group:       	X11/GNOME/Development/Libraries
Group(pl):   	X11/GNOME/Programowanie/Biblioteki
Requires:    	%{name} = %{version}

%description devel
Libraries and includes files you can use for libghttp development

%description devel -l pl
Biblioteki i pliki nag³owkowe potrzebne do programowania z wykorzystaniem 
libghttp

%package static
Summary:    	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Group:       	X11/GNOME/Development/Libraries
Group(pl):   	X11/GNOME/Programowanie/Biblioteki
Requires:    	%{name}-devel = %{version}

%description static
GNOME http client static library.

%description static -l pl
Wersja statyczna biblioteki libghttp

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDCONFIG="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%attr(755, root, root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.99-2]
- added Group(pl)
- added gzipping documentation

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99-1]
- added LDFLAGS="-s" to ./configure enviroment,
- fixed permission on /usr/X11R6/lib/lib* files.

* Fri Oct  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- changed Copyright field to GPL,
- removed Packager field (this must be placed in private ~/.rpmrc),
- removed COPYING from %doc,
- all %doc moved to devel,
- added full %attr description in %files,
- added stripping shared libraries.
