Summary:	Creates virtual networks and host
Summary(pl):	Tworzy wirtualne sieci i serwery
Name:		honeyd
Version:	0.7a
Release:	0.01
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.citi.umich.edu/u/provos/honeyd/%{name}-%{version}.tar.gz
# Source0-md5:	04ae109952d274aba4c0ab398e213ef2
URL:		http://www.citi.umich.edu/u/provos/honeyd/
BuildRequires:	libdnet-devel libevent-devel
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

Honeyd jest ma�ym programem tworz�cym wirtualne sieci i serwery.
Serwery te mog� zosta� skonfigurowane tak, by uruchamia� konkretne
serwisy, i ich osobowo�� mo�e zosta� dostosowana w ten spos�b, by
wygl�da�o, �e dzia�aj�na r�nych systemach operacyjnych. Honeyd daje
mo�liwo�� aby jeden komputer symulowa� wiele serwer�w w wielu
podsieciach.

%prep
%setup -q

%build
#%{__gettextize}
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

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}