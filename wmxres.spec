Summary:	wmxres - dockable resolution changer
Summary(pl):	wmxres - dokowalny zmieniacz rozdzielczo¶ci
Name:		wmxres
Version:	1.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://yalla.free.fr/wn/%{name}-%{version}-0.tar.gz
# Source0-md5:	a1b44620bd2f567c3f2a4b6767dedb33
Source1:	%{name}.desktop
URL:		http://yalla.free.fr/wn/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		xbitmapsdir	/usr/X11R6/include/X11/bitmaps

%description
Dockable resolution changer.

%description -l pl
Dokowalny zmieniacz rozdzielczo¶ci.

%prep
%setup -q -n %{name}.app

%build
%{__make} OPTS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets,%{_pixmapsdir},%{xbitmapsdir}}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}-mask.xbm $RPM_BUILD_ROOT%{xbitmapsdir}
install %{name}/%{name}-master.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{xbitmapsdir}/*
%{_pixmapsdir}/*
%{_desktopdir}/docklets/%{name}.desktop
