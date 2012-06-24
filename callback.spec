Summary:	Callback package for Linux
Summary(pl):	Pakiet Callback dla Linuxa
Name:		callback
Version:	4.24
Release:	1
License:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Source0:	ftp://ftp.icce.rug.nl/pub/unix/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.icce.rug.nl/pub/unix/%{name}.FAQ
Patch0:		%{name}-Makefiles.patch
URL:		http://www.icce.rug.nl/docs/programs/callback/callback.html
Requires:	mgetty
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows callback for Linux systems which are equipped with a
modem. The package contains three programs: cblogin, a login-program for
dial-in connections, cbmgetty, a pseudo-getty and cb, a callback control
unit.

%description -l pl
Ten pakiet udost�pnia us�ug� callback na systemach z Linuxem wyposa�onych w
modem. Pakiet zawiera trzy programy: cblogin, program zast�puj�cy login
przy wdzwanianych po��czeniach, cbmgetty, pseudo-getty, oraz cb, program
steruj�cy.

%prep
%setup -q -n %{name}
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,4}}
	
install cb/cb login/cblogin mgetty/cbmgetty $RPM_BUILD_ROOT%{_bindir}
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/*.4 $RPM_BUILD_ROOT%{_mandir}/man4
install %{SOURCE1} .

gzip -9nf %{name}.FAQ CHANGELOG $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.gz %{name}.FAQ.gz examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
