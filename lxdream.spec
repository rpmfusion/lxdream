Name:           lxdream
Version:        0.8.3
Release:        4%{?dist}
Summary:        Sega Dreamcast emulator
Group:          Applications/Emulators
License:        GPLv2+
URL:            http://www.lxdream.org
# Actual source URL is: http://www.lxdream.org/count.php?file=lxdream-0.8.3.tar.gz
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
Requires:       hicolor-icon-theme
ExclusiveArch:  %{ix86} x86_64

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
%config(noreplace) %{_sysconfdir}/%{name}rc
%doc RELEASE_NOTES STATUS CREDITS COPYING ChangeLog README.fedora
%exclude %{_datadir}/pixmaps/%{name}/dcemu.gif


%changelog
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
