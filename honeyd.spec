# ToDo:
# - split into subpackage / drop headers
# - include scripts/ (where?)
Summary:	Creates virtual networks and host
Summary(pl):	Tworzy wirtualne sieci i serwery
Name:		honeyd
Version:	0.8
Release:	0.1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.citi.umich.edu/u/provos/honeyd/%{name}-%{version}.tar.gz
# Source0-md5:	d8d3692176d2f78841f7a3384ccb0b73
URL:		http://www.citi.umich.edu/u/provos/honeyd/
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

%description -l pl
Honeyd jest ma³ym programem tworz±cym wirtualne sieci i serwery.
Serwery te mog± zostaæ skonfigurowane tak, by uruchamiaæ konkretne
serwisy, i ich osobowo¶æ mo¿e zostaæ dostosowana w ten sposób, by
wygl±da³o, ¿e dzia³aj± na ró¿nych systemach operacyjnych. Honeyd 
daje mo¿liwo¶æ aby jeden komputer symulowa³ wiele serwerów w wielu
podsieciach.

%prep
%setup -q

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
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_datadir}/%{name}
%{_includedir}/*
%{_mandir}/man8/*
