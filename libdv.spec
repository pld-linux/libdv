#
# _with_mmx - uses MMX asm (won't run on non-MMX CPU!)
Summary:	DV video software codec
Summary(pl):	Biblioteka do obs�ugi formatu wideo DV
Name:		libdv
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	http://download.sourceforge.net/libdv/%{name}-%{version}.tar.gz
URL:		http://libdv.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The Quasar DV codec (libdv) is a software codec for DV video. DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface. libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M. See http://libdv.sourceforge.net/ for more.

%description -l pl
Quasar DV (libdv) jest bibliotek� do obs�ugi obrazu DV. DV jest
formatem stosowanym przez wi�kszo�� cyfrowych urz�dze�, zwykle tych,
kt�re u�ywaj� interfejsu IEEE 1394 (FireWire/i.Link). libdv jest
pisany zgodnie z oficjalnymi standardami DV, IEC 61834, SMPTE 314M.

%package -n dv
Summary:	Programs to encode and play DV files
Summary(pl):	Programy do kodowania i odtwarzania plik�w DV
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description -n dv
Programs to encode and play DV files.

%description -n dv -l pl
Programy do kodowania i odtwarzania plik�w DV.

%package devel
Summary:	DV library headers
Summary(pl):	Pliki nag��wkowe biblioteki DV
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania program�w korzystaj�cych z
libdv.

%package static
Summary:	DV static libraries
Summary(pl):	Statyczne biblioteki do obs�ugi formatu DV
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
This is package with static libdv libraries.

%description static -l pl
Statyczna wersja biblioteki libdv.

%prep
%setup  -q

%build
%configure \
	--enable-shared \
	--without-debug \
	%{!?_with_mmx:--disable-asm}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README.* TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files -n dv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libdv
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
