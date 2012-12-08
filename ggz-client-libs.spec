%define mod_major 4
%define core_major 9
%define modlibname %mklibname ggzmod %{mod_major}
%define corelibname %mklibname ggzcore %{core_major}

%define libggz_version %{version}
%define lib_name %mklibname %{name} %{core_major}
%define develname %mklibname -d %{name}

Name:		ggz-client-libs
Summary:	GGZ Client Libraries
Version:	0.0.14.1
Release:	9
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
Source0:	http://ftp.ggzgamingzone.org/pub/ggz/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	popt-devel
BuildRequires:	expat-devel
Requires(pre):	%{modlibname} = %{version}
Requires(pre):	%{corelibname} = %{version}

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

%package -n	%{develname}
Summary:	Development files for GGZ game clients library
Group:		Development/C
Requires:	libggz-devel = %{libggz_version}
Requires: 	%{modlibname} = %{version}-%{release}
Requires:	%{corelibname} = %{version}-%{release}
Provides: 	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

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

%post
touch %{_sysconfdir}/ggz.modules

%files -f ggzcore.lang
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
%{_libdir}/libggzmod.so.%{mod_major}*

%files -n %{corelibname}
%{_libdir}/libggzcore.so.%{core_major}*

%files -n %{develname}
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/lib*.so
%{_mandir}/man3/*


%changelog
* Tue Dec 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.0.14.1-9
+ Revision: 738061
- rebuild
- clean up spec
- removed defattr, clean section, BuildRoot, mkrel
- removed old ldconfig scriptlets
- removed .la files
- disabled static build
- left dep loop for now

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-8
+ Revision: 664827
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-7mdv2011.0
+ Revision: 605450
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-6mdv2010.1
+ Revision: 521480
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.0.14.1-5mdv2010.0
+ Revision: 424873
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-4mdv2009.1
+ Revision: 352745
- use configure2_5x

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.0.14.1-3mdv2009.0
+ Revision: 221068
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-2mdv2008.1
+ Revision: 189658
- Fix groups

* Tue Feb 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-1mdv2008.1
+ Revision: 175200
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Götz Waschk <waschk@mandriva.org> 0.0.14-4mdv2008.1
+ Revision: 116931
- new version
- new devel name
- move ggz-config to the main package
- ggz.modules is a ghost file

* Mon Jul 16 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-3mdv2008.0
+ Revision: 52682
- add checking on major version


* Sat Feb 10 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-2mdv2007.0
+ Revision: 118743
- fix core major to 9

* Wed Feb 07 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-1mdv2007.1
+ Revision: 117341
- New version 0.0.14
- Import ggz-client-libs

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-7mdv2007.0
- fix x86_64 build

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-6mdv2007.0
- rebuild

* Sat Jul 29 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-5mdv2007.0
- try to fix deps mess

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-4mdk
- improve libs management

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-3mdk
- really fix devel

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-2mdk
- fix devel

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-1mdk
- 0.0.13
- mkrel

* Wed Oct 19 2005 Emmanuel Blindauer <blindauer@mandriva.org> 0.0.12-1mdk
- 0.0.12

* Mon Nov 29 2004 Abel Cheung <deaddog@mandrake.org> 0.0.9-2mdk
- Split libraries

* Sun Nov 28 2004 Abel Cheung <deaddog@mandrake.org> 0.0.9-1mdk
- New version

* Tue Feb 10 2004 Abel Cheung <deaddog@deaddog.org> 0.0.8-1mdk
- New version

