Summary:	GNOME http client library
Summary(es):	Biblioteca cliente http del GNOME
Summary(ko):	GNOME http е╛╤Сюл╬Пф╝ ╤Сюл╨Й╥╞╦╝
Summary(pl):	Biblioteka funkcji klienta http
Summary(pt_BR):	Biblioteca cliente para http do GNOME
Summary(ru):	Библиотека http-клиента для GNOME
Summary(uk):	Б╕бл╕отека http-кл╕╓нта для GNOME
Name:		libghttp
Version:	1.0.9
Release:	9
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libghttp/1.0/%{name}-%{version}.tar.gz
# Source0-md5: 0690e7456f9a15c635f240f3d6d5dab2
Patch0:		%{name}-ac.patch
Patch1:		%{name}-fixlocale.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for making HTTP 1.1 requests.

%description -l es
Biblioteca cliente http 1.1 del GNOME.

%description -l pl
Biblioteka funkcji umo©liwiaj╠cych realizacjЙ zapytaЯ HTTP 1.1.

%description -l pt_BR
Biblioteca cliente para http 1.1 do GNOME.

%description -l ru
Библиотека для исполнения HTTP 1.1 запросов.

%description -l uk
Б╕бл╕отека для виконання HTTP 1.1 запит╕в.

%package devel
Summary:	GNOME http client development
Summary(es):	Biblioteca cliente http 1.1 del GNOME - desarrollo
Summary(ko):	GNOME http е╛╤Сюл╬Пф╝ ╟Ё╧ъ©║ гй©Дгя ╤Сюл╨Й╥╞╦╝©м гЛ╢У фдюо
Summary(pl):	Biblioteki i pliki nagЁСwkowe libghttp
Summary(pt_BR):	Componentes para desenvolvimento com o cliente http do GNOME.
Summary(ru):	Разработка http-клиентов под GNOME
Summary(uk):	Розробка http-кл╕╓нт╕в п╕д GNOME
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Libraries and includes files you can use for libghttp development.

%description devel -l es
Biblioteca cliente http 1.1 del GNOME - desarrollo.

%description devel -l pl
Biblioteki i pliki nagЁСwkowe potrzebne do programowania z
wykorzystaniem libghttp.

%description devel -l pt_BR
Componentes para desenvolvimento com o cliente http do GNOME.

%description devel -l ru
Хедеры для разработки программ с использованием libghttp.

%description devel -l uk
Хедери для розробки програм з використанням libghttp.

%package static
Summary:	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libghttp
Summary(ru):	Разработка http-клиентов под GNOME - статические библиотеки
Summary(uk):	Розробка http-кл╕╓нт╕в п╕д GNOME - статичн╕ б╕бл╕отеки
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GNOME http client static library.

%description static -l pl
Wersja statyczna biblioteki libghttp.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libghttp.

%description static -l ru
Статические библиотеки для разработки программ с использованием
libghttp.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм з використанням libghttp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install http_*.h $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
