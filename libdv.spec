#
# Conditional build:
%bcond_with	mmx	# use MMX asm (won't run on non-MMX CPU!)
#
%ifarch athlon
%define	with_mmx	1
%endif
Summary:	DV video software codec
Summary(pl):	Biblioteka do obs³ugi formatu wideo DV
Name:		libdv
Version:	0.101
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libdv/%{name}-%{version}.tar.gz
# Source0-md5:	d42832cbe0ad2c1c1f6a7eccf35f9323
Patch0:		%{name}-extern.patch
Patch1:		%{name}-include_fix.patch
URL:		http://libdv.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel >= 1.2.10-3
BuildRequires:	pkgconfig >= 0.7
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Quasar DV codec (libdv) is a software codec for DV video. DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface. libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M. See http://libdv.sourceforge.net/ for more.

%description -l pl
Quasar DV (libdv) jest bibliotek± do obs³ugi obrazu DV. DV jest
formatem stosowanym przez wiêkszo¶æ cyfrowych urz±dzeñ, zwykle tych,
które u¿ywaj± interfejsu IEEE 1394 (FireWire/i.Link). libdv jest
pisany zgodnie z oficjalnymi standardami DV, IEC 61834, SMPTE 314M.

%package -n dv
Summary:	Programs to encode and play DV files
Summary(pl):	Programy do kodowania i odtwarzania plików DV
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description -n dv
Programs to encode and play DV files.

%description -n dv -l pl
Programy do kodowania i odtwarzania plików DV.

%package devel
Summary:	DV library headers
Summary(pl):	Pliki nag³ówkowe biblioteki DV
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów korzystaj±cych z
libdv.

%package static
Summary:	DV static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu DV
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is package with static libdv libraries.

%description static -l pl
Statyczna wersja biblioteki libdv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--without-debug \
	%{!?with_mmx:--disable-asm}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files -n dv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/libdv
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
