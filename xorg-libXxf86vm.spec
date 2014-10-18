Summary:	Xxf86vm library
Name:		xorg-libXxf86vm
Version:	1.1.3
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2
# Source0-md5:	e46f6ee4f4567349a3189044fe1bb712
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86vm library.

%package devel
Summary:	Header files for libXxf86vm library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xxf86vm library.

This package contains the header files needed to develop programs that
use libXxf86vm.

%prep
%setup -qn libXxf86vm-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXxf86vm.so.?
%attr(755,root,root) %{_libdir}/libXxf86vm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86vm.so
%{_includedir}/X11/extensions/xf86vmode.h
%{_pkgconfigdir}/xxf86vm.pc
%{_mandir}/man3/*.3x*

