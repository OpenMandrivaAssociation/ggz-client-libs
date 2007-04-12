%define version 0.0.14
%define release %mkrel 2

%define modlibname %mklibname ggzmod 4
%define corelibname %mklibname ggzcore 9

%define libggz_version %{version}
%define lib_name        %mklibname %{name} 9

Name:		ggz-client-libs
Summary:	GGZ Client Libraries
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	popt-devel expat-devel
Requires(pre):		%{modlibname} = %{version}
Requires(pre):		%{corelibname} = %{version}

%description
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains shared data files of GGZ and utility that
maintain installed game modules.


%package -n	%{modlibname}
Summary:	GGZ Library containing functions interfacing game server and GGZ
Group:		Games/Other
Requires:	%{name} = %{version}
Provides:	libggzmod = %{version}

%description -n	%{modlibname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains library that contains common functions for
interfacing a game server and GGZ.


%package -n	%{corelibname}
Summary:	GGZ Library needed by GGZ clients
Group:		Games/Other
Requires:	%{name} = %{version}
Provides:	libggzcore = %{version}

%description -n	%{corelibname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains library that contains core functions needed
by all GGZ clients.


%package -n	%{lib_name}-devel
Summary:	Development files for GGZ game clients library
Group:		Development/Other
Requires:	libggz-devel = %{libggz_version}
Requires: 	%{modlibname} = %{version}
Requires:       %{corelibname} = %{version}
Provides: 	%{name}-devel

%description -n	%{lib_name}-devel
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains headers and other development files used for
building GGZ Gaming Zone clients or game modules.


%prep
%setup -q

%build
%configure --with-libggz-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}
# owns various directories
mkdir -p %{buildroot}%{_libdir}/ggz \
	 %{buildroot}%{_datadir}/ggz/ggz-config \
	 %{buildroot}%{_datadir}/ggz/pixmaps

mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ggz.modules

%clean
rm -rf %{buildroot}

%post -n %{modlibname} -p /sbin/ldconfig
%postun -n %{modlibname} -p /sbin/ldconfig

%post -n %{corelibname} -p /sbin/ldconfig
%postun -n %{corelibname} -p /sbin/ldconfig




%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README QuickStart.GGZ README.GGZ
%config(noreplace) %{_sysconfdir}/ggz.modules
%{_bindir}/ggz-wrapper
%{_bindir}/ggz
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_mandir}/man7/*
%dir %{_libexecdir}/ggz
%dir %{_libexecdir}/ggz/ggzwrap
%dir %{_datadir}/ggz
%dir %{_datadir}/ggz/ggz-config
%dir %{_datadir}/ggz/pixmaps
%dir %{_datadir}/locale/de/LC_MESSAGES/*
%{_sysconfdir}/xdg/menus/ggz.menu
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_datadir}/desktop-directories/ggz-games.directory
%{_datadir}/desktop-directories/ggz.directory
%{_datadir}/locale/de/LC_MESSAGES/ggz-config.mo



%files -n %{modlibname}
%defattr(-,root,root)
%{_libdir}/libggzmod.so.*

%files -n %{corelibname}
%defattr(-,root,root)
%{_libdir}/libggzcore.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_includedir}/*
%{_bindir}/ggz-config
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*


