Name:           lxdream
Version:        0.9.1
Release:        1%{?dist}
Summary:        Sega Dreamcast emulator
Group:          Applications/Emulators
License:        GPLv2+
URL:            http://www.lxdream.org
# Actual source URL is: http://www.lxdream.org/count.php?file=%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        README.fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libGL-devel
BuildRequires:  lirc-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL-devel
# there should be a {ix86} instead of i386 in the ExclusiveArch line but
# that would make plague build the package for athlon, i386, i586 and i686 :-/
%if 0%{?fedora} >= 11
ExclusiveArch:  i586 x86_64
%else
ExclusiveArch:  i386 x86_64
%endif

%description
lxdream is a linux-based emulator of the Sega Dreamcast system. While it is
still in heavy development (and many features are buggy or unimplemented), it
is already capable of running many demos and some games.


%prep
%setup -q

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


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/lxdream
%{_libdir}/lxdream
%{_datadir}/applications/lxdream.desktop
%{_mandir}/man1/lxdream.1*
%{_datadir}/pixmaps/lxdream
%{_datadir}/pixmaps/lxdream.png
%config(noreplace) %{_sysconfdir}/lxdreamrc
%doc COPYING ChangeLog README.fedora


%changelog
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
