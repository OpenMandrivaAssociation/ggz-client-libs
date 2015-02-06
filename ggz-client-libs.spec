%define mod_major 4
%define core_major 9
%define libggzmod %mklibname ggzmod %{mod_major}
%define libggzcore %mklibname ggzcore %{core_major}
%define devname %mklibname -d %{name}

Summary:	GGZ Client Libraries
Name:		ggz-client-libs
Version:	0.0.14.1
Release:	15
License:	GPLv2
Group:		Games/Other
Url:		http://ggzgamingzone.org/
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	libggz-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(popt)

%description
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains shared data files of GGZ and utility that
maintain installed game modules.

%package -n	%{libggzmod}
Summary:	GGZ Library containing functions interfacing game server and GGZ
Group:		System/Libraries
Suggests:	%{name} = %{version}

%description -n	%{libggzmod}
This package contains library that contains common functions for
interfacing a game server and GGZ.

%package -n	%{libggzcore}
Summary:	GGZ Library needed by GGZ clients
Group:		System/Libraries
Suggests:	%{name} = %{version}

%description -n	%{libggzcore}
This package contains library that contains core functions needed
by all GGZ clients.

%package -n	%{devname}
Summary:	Development files for GGZ game clients library
Group:		Development/C
Requires: 	%{libggzmod} = %{version}-%{release}
Requires:	%{libggzcore} = %{version}-%{release}
Provides: 	%{name}-devel = %{version}-%{release}
Conflicts:	%{name} < 0.0.14.1-10

%description -n	%{devname}
This package contains headers and other development files used for
building GGZ Gaming Zone clients or game modules.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-libggz-libraries=%{_libdir}

%make

%install
%makeinstall_std

%find_lang ggzcore
%find_lang ggz-config

# owns various directories
mkdir -p %{buildroot}%{_libdir}/ggz \
	 %{buildroot}%{_datadir}/ggz/ggz-config \
	 %{buildroot}%{_datadir}/ggz/pixmaps

mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ggz.modules

%post
touch %{_sysconfdir}/ggz.modules

%files -f ggzcore.lang
%doc AUTHORS COPYING NEWS README QuickStart.GGZ README.GGZ
%ghost %{_sysconfdir}/ggz.modules
%{_sysconfdir}/xdg/menus/ggz.menu
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_bindir}/ggz
%dir %{_libexecdir}/ggz
%dir %{_datadir}/ggz
%dir %{_datadir}/ggz/pixmaps
%{_datadir}/desktop-directories/ggz-games.directory
%{_datadir}/desktop-directories/ggz.directory
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n %{libggzmod}
%{_libdir}/libggzmod.so.%{mod_major}*

%files -n %{libggzcore}
%{_libdir}/libggzcore.so.%{core_major}*

%files -n %{devname} -f ggz-config.lang
%doc COPYING ChangeLog
%{_bindir}/ggz-config
%{_bindir}/ggz-wrapper
%dir %{_datadir}/ggz/ggz-config
%dir %{_libexecdir}/ggz/ggzwrap
%{_includedir}/*
%{_libdir}/lib*.so
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man6/*

