Summary:	GNOME HTTP client library
Summary(es.UTF-8):	Biblioteca cliente HTTP del GNOME
Summary(ko.UTF-8):	GNOME HTTP 클라이언트 라이브러리
Summary(pl.UTF-8):	Biblioteka funkcji klienta HTTP
Summary(pt_BR.UTF-8):	Biblioteca cliente para HTTP do GNOME
Summary(ru.UTF-8):	Библиотека HTTP-клиента для GNOME
Summary(uk.UTF-8):	Бібліотека HTTP-клієнта для GNOME
Name:		libghttp
Version:	1.0.9
Release:	12
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libghttp/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	0690e7456f9a15c635f240f3d6d5dab2
Patch0:		%{name}-ac.patch
Patch1:		%{name}-fixlocale.patch
Patch2:		%{name}-ssl.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for making HTTP 1.1 requests.

%description -l es.UTF-8
Biblioteca cliente HTTP 1.1 del GNOME.

%description -l pl.UTF-8
Biblioteka funkcji umożliwiających realizację zapytań HTTP 1.1.

%description -l pt_BR.UTF-8
Biblioteca cliente para HTTP 1.1 do GNOME.

%description -l ru.UTF-8
Библиотека для исполнения HTTP 1.1 запросов.

%description -l uk.UTF-8
Бібліотека для виконання HTTP 1.1 запитів.

%package devel
Summary:	GNOME HTTP client development
Summary(es.UTF-8):	Biblioteca cliente HTTP 1.1 del GNOME - desarrollo
Summary(ko.UTF-8):	GNOME HTTP 클라이언트 개발에 필요한 라이브러리와 헤더 파일
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe libghttp
Summary(pt_BR.UTF-8):	Componentes para desenvolvimento com o cliente HTTP do GNOME.
Summary(ru.UTF-8):	Разработка HTTP-клиентов под GNOME
Summary(uk.UTF-8):	Розробка HTTP-клієнтів під GNOME
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Libraries and includes files you can use for libghttp development.

%description devel -l es.UTF-8
Biblioteca cliente HTTP 1.1 del GNOME - desarrollo.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe potrzebne do programowania z
wykorzystaniem libghttp.

%description devel -l pt_BR.UTF-8
Componentes para desenvolvimento com o cliente HTTP do GNOME.

%description devel -l ru.UTF-8
Хедеры для разработки программ с использованием libghttp.

%description devel -l uk.UTF-8
Хедери для розробки програм з використанням libghttp.

%package static
Summary:	GNOME HTTP client static library
Summary(pl.UTF-8):	Statyczna biblioteka libghttp
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libghttp
Summary(ru.UTF-8):	Разработка HTTP-клиентов под GNOME - статические библиотеки
Summary(uk.UTF-8):	Розробка HTTP-клієнтів під GNOME - статичні бібліотеки
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	openssl-devel

%description static
GNOME HTTP client static library.

%description static -l pl.UTF-8
Wersja statyczna biblioteki libghttp.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libghttp.

%description static -l ru.UTF-8
Статические библиотеки для разработки программ с использованием
libghttp.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм з використанням libghttp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ssl
%{__make} \
	libghttp_la_LIBADD="-lssl -lcrypto"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install http_*.h $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libghttp.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ghttpConf.sh
%attr(755,root,root) %{_libdir}/libghttp.so
%{_libdir}/libghttp.la
%{_includedir}/ghttp*.h
%{_includedir}/ghttp-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libghttp.a
