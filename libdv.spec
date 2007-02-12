#
# Conditional build:
%bcond_without	gui		# don't build gui stuff
%bcond_with	mmx		# use MMX asm (won't run on non-MMX CPU!)
%bcond_without	static_libs	# don't build static library
#
%ifarch athlon pentium3 pentium4 %{x8664}
%define		with_mmx	1
%endif
Summary:	DV video software codec
Summary(pl.UTF-8):   Biblioteka do obsługi formatu wideo DV
Name:		libdv
Version:	1.0.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdv/%{name}-%{version}.tar.gz
# Source0-md5:	f895162161cfa4bb4a94c070a7caa6c7
Patch0:		%{name}-include_fix.patch
URL:		http://libdv.sourceforge.net/
%if %{with gui}
BuildRequires:	SDL-devel >= 1.1.6
BuildRequires:	gtk+-devel >= 1.2.10-3
BuildRequires:	xorg-lib-libXv-devel
%endif
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Quasar DV codec (libdv) is a software codec for DV video. DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface. libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M. See http://libdv.sourceforge.net/ for more.

%description -l pl.UTF-8
Quasar DV (libdv) jest biblioteką do obsługi obrazu DV. DV jest
formatem stosowanym przez większość cyfrowych urządzeń, zwykle tych,
które używają interfejsu IEEE 1394 (FireWire/i.Link). libdv jest
pisany zgodnie z oficjalnymi standardami DV, IEC 61834, SMPTE 314M.

%package -n dv
Summary:	Programs to encode and play DV files
Summary(pl.UTF-8):   Programy do kodowania i odtwarzania plików DV
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description -n dv
Programs to encode and play DV files.

%description -n dv -l pl.UTF-8
Programy do kodowania i odtwarzania plików DV.

%package devel
Summary:	DV library headers
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki DV
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów korzystających z
libdv.

%package static
Summary:	DV static libraries
Summary(pl.UTF-8):   Statyczne biblioteki do obsługi formatu DV
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libdv libraries.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libdv.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
%if %{with gui}
	--enable-sdl \
	--enable-gtk \
%else
	--disable-sdl \
	--disable-gtk \
%endif
	--without-debug \
	%{!?with_mmx:--disable-asm} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.* TODO
%attr(755,root,root) %{_libdir}/libdv.so.*.*.*

%if %{with gui}
%files -n dv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdv.so
%{_libdir}/libdv.la
%{_includedir}/libdv
%{_pkgconfigdir}/libdv.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdv.a
%endif
