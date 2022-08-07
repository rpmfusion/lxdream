Name:           lxdream
Version:        0.9.1
Release:        22%{?dist}
Summary:        Sega Dreamcast emulator
License:        GPLv2+
URL:            http://www.lxdream.org
# Actual source URL is: http://www.lxdream.org/count.php?file=%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        README.fedora
Patch0:         %{name}-%{version}-glib.patch
Patch1:         %{name}-%{version}-implicit.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libGL-devel
BuildRequires:  lirc-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL-devel
BuildRequires:  zlib-devel
# there should be a {ix86} instead of i386 in the ExclusiveArch line but
# that would make plague build the package for athlon, i386, i586 and i686 :-/
ExclusiveArch:  i686 x86_64

%description
lxdream is a linux-based emulator of the Sega Dreamcast system. While it is
still in heavy development (and many features are buggy or unimplemented), it
is already capable of running many demos and some games.


%prep
%setup -q
%patch0 -p1 -b .glib
%patch1 -p1 -b .implicit

#Fix the desktop file
sed -i "s/Categories=Game;Emulator/Categories=Game;Emulator;/" lxdream.desktop


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -pm0644 %{SOURCE1} README.fedora

#Validate the desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/lxdream.desktop

#Find locales
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/lxdream
%{_libdir}/lxdream
%{_datadir}/applications/lxdream.desktop
%{_mandir}/man1/lxdream.1*
%{_datadir}/pixmaps/lxdream
%{_datadir}/pixmaps/lxdream.png
%config(noreplace) %{_sysconfdir}/lxdreamrc
%doc COPYING ChangeLog README.fedora


%changelog
* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 Sérgio Basto <sergio@serjux.com> - 0.9.1-10
- Fix another "relocation R_X86_64_PC32 against undefined symbol recompile with
  -fPIC"

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon May 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-8
- Rebuilt and drop esound support
- Add BR perl(Pod::Man) for lxdream.pod

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-7
- Mass rebuilt for Fedora 19 Features

* Sun Apr 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-6
- Rebuilt

* Sat Feb 11 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.1-4
- Ensured the i686 version is built as well

* Fri Feb 10 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.1-3
- Fixed build failures
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.1-1
- Updated to 0.9.1
- Dropped the sanerconfig patch
- Conditionalised the ExclusiveArch line
- Dropped the icon conversion, upstream now ships a png one
- Dropped hicolor-icon-theme from Requires
- Dropped the desktop file, upstream now ships it as well
- Added SDL-devel and lirc-devel to BuildRequires

* Sun Apr 12 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9-3
- s/i386/i586/ in ExclusiveArch for F11

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9-2
- rebuild for new F11 features

* Tue Oct 28 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9-1
- Updated to 0.9
- dcemu.gif is not installed anymore, so don't exclude it

* Sat Oct 25 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.4-2
- use i386 instead of ix86 for ExcludeArch

* Sun Oct 19 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.4-1
- Updated to 0.8.4
- Added pulseaudio-libs-devel to BuildRequires
- Dropped some docs which were no longer available

* Fri Sep 12 2008 Xavier Lamien <lxtnow[at]gmail.com - 0.8.3-4
- Update files and rebuild for rpmfusion inclusion.

* Wed Mar 05 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.3-3
- Exclusivearch x86/x86_64 for the moment. Others seem broken.

* Mon Mar 03 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.3-2
- Minor spec cleanups

* Sun Feb 03 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.3-1
- Upgrade to 0.8.3

* Wed Jan 09 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.2-1
- Initial release
