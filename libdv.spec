Summary:	DV video software codec
Summary(pl):	Biblioteka do obs³ugi formatu wideo DV
Name:		libdv
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	http://download.sourceforge.net/libdv/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://libdv.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The Quasar DV codec (libdv) is a software codec for DV video. DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface. libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M. See http://libdv.sourceforge.net/ for more.

%package -n dv
Summary:	Programs to encode and play DV files
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description -n dv
Programs to encode and play DV files.

%package devel
Summary:	DV library headers
Summary(pl):	Pliki nag³ówkowe biblioteki DV
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%package static
Summary:	DV static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu DV
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
This is package with static libdv libraries.

%prep
%setup  -q
%patch0 -p1

%build
autoconf
%configure \
	--enable-shared \
	--without-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog NEWS TODO

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

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libdv

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
