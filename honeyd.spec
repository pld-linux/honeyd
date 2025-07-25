# ToDo:
# - split into subpackage / drop headers
# - include scripts/ (where?)
Summary:	Creates virtual networks and host
Summary(pl.UTF-8):	Tworzy wirtualne sieci i serwery
Name:		honeyd
Version:	1.5c
Release:	0.1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.citi.umich.edu/u/provos/honeyd/%{name}-%{version}.tar.gz
# Source0-md5:	9887b44333e380a2205f64fa245cb727
Patch0:		%{name}-lib64.patch
URL:		http://www.honeyd.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Honeyd is a small daemon that creates virtual hosts on a network. The
hosts can be configured to run arbitrary services, and their
personality can be adapted so that they appear to be running certain
operating systems. Honeyd enables a single host to claim multiple
addresses on a LAN for network simulation. Honeyd improves cyber
security by providing mechanisms for threat detection and assessment.
It also deters adversaries by hiding real systems in the middle of
virtual systems.

%description -l pl.UTF-8
Honeyd jest małym programem tworzącym wirtualne sieci i serwery.
Serwery te mogą zostać skonfigurowane tak, by uruchamiać konkretne
serwisy, i ich osobowość może zostać dostosowana w ten sposób, by
wyglądało, że działają na różnych systemach operacyjnych. Honeyd 
daje możliwość aby jeden komputer symulował wiele serwerów w wielu
podsieciach.

%prep
%setup -q
%if "%{_lib}" == "lib64"
%patch -P0 -p1
%endif

%build
glib-gettextize
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_datadir}/%{name}
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
