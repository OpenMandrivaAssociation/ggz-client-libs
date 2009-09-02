%define version 0.0.14.1
%define release %mkrel 5

%define mod_major 4
%define core_major 9

%define modlibname %mklibname ggzmod %{mod_major}
%define corelibname %mklibname ggzcore %{core_major}

%define libggz_version %{version}
%define lib_name        %mklibname %{name} %{core_major}
%define develname %mklibname -d %name

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
Group:		System/Libraries
Requires:	%{name} = %{version}
Provides:	libggzmod = %{version}

%description -n	%{modlibname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains library that contains common functions for
interfacing a game server and GGZ.


%package -n	%{corelibname}
Summary:	GGZ Library needed by GGZ clients
Group:		System/Libraries
Requires:	%{name} = %{version}
Provides:	libggzcore = %{version}

%description -n	%{corelibname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains library that contains core functions needed
by all GGZ clients.


%package -n	%develname
Summary:	Development files for GGZ game clients library
Group:		Development/C
Requires:	libggz-devel = %{libggz_version}
Requires: 	%{modlibname} = %{version}
Requires:       %{corelibname} = %{version}
Provides: 	%{name}-devel = %version-%release
Obsoletes: %mklibname -d %name 9

%description -n	%develname
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains headers and other development files used for
building GGZ Gaming Zone clients or game modules.


%prep
%setup -q

%build
%configure2_5x --with-libggz-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot} ggz*.lang
%makeinstall_std

%find_lang ggzcore
%find_lang ggz-config
cat ggz-config.lang >> ggzcore.lang

# owns various directories
mkdir -p %{buildroot}%{_libdir}/ggz \
	 %{buildroot}%{_datadir}/ggz/ggz-config \
	 %{buildroot}%{_datadir}/ggz/pixmaps

mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ggz.modules

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{modlibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{modlibname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{corelibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{corelibname} -p /sbin/ldconfig
%endif

%post
touch %{_sysconfdir}/ggz.modules


%files -f ggzcore.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README QuickStart.GGZ README.GGZ
%ghost %{_sysconfdir}/ggz.modules
%{_sysconfdir}/xdg/menus/ggz.menu
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_bindir}/ggz-config
%{_bindir}/ggz-wrapper
%{_bindir}/ggz
%dir %{_libexecdir}/ggz
%dir %{_libexecdir}/ggz/ggzwrap
%dir %{_datadir}/ggz
%dir %{_datadir}/ggz/ggz-config
%dir %{_datadir}/ggz/pixmaps
%{_datadir}/desktop-directories/ggz-games.directory
%{_datadir}/desktop-directories/ggz.directory
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_mandir}/man7/*


%files -n %{modlibname}
%defattr(-,root,root)
%{_libdir}/libggzmod.so.%{mod_major}
%{_libdir}/libggzmod.so.%{mod_major}.*


%files -n %{corelibname}
%defattr(-,root,root)
%{_libdir}/libggzcore.so.%{core_major}
%{_libdir}/libggzcore.so.%{core_major}.*

%files -n %develname
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*


