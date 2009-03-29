Name:           lxdream
Version:        0.9
Release:        2%{?dist}
Summary:        Sega Dreamcast emulator
Group:          Applications/Emulators
License:        GPLv2+
URL:            http://www.lxdream.org
# Actual source URL is: http://www.lxdream.org/count.php?file=%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        README.fedora
Source2:        %{name}.desktop
Patch0:         %{name}-0.8.2-sanerconfig.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  ImageMagick
BuildRequires:  libGL-devel
BuildRequires:  pulseaudio-libs-devel
Requires:       hicolor-icon-theme
# there should be a {ix86} instead of i386 in the ExclusiveArch line but
# that would make plague build the package for athlon, i386, i586 and i686 :-/
ExclusiveArch:  i386 x86_64

%description
lxdream is a linux-based emulator of the Sega Dreamcast system. While it is
still in heavy development (and many features are buggy or unimplemented), it
is already capable of running many demos and some games.


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags}

# Create icon
convert -scale 128 pixmaps/dcemu.gif %{name}.png



%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -pm0644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -pm0644 %{SOURCE1} README.fedora

#Find locales
%find_lang %{name}

desktop-file-install --vendor "" \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{SOURCE2}


%clean
rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/lxdream
%config(noreplace) %{_sysconfdir}/%{name}rc
%doc COPYING ChangeLog README.fedora


%changelog
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
