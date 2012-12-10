%define name    gtkdive
%define version 0.71
%define release 7

%define title       GtkDive
%define longtitle   Buehlmann ZH-L16 model diving simulation

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Buehlmann ZH-L16 model diving simulation
License:        GPL
Group:          Sciences/Other
URL:            http://mattzz.dyndns.org/twiki/bin/view/Projects/GtkDive
Source0:        http://mattzz.dyndns.org/twiki/pub/Projects/GtkDive/%{name}-%{version}.tar.bz2
Source1:        %{name}-16.png.bz2
Source2:        %{name}-32.png.bz2
Source3:        %{name}-48.png.bz2
BuildRequires:  gtk+2-devel
BuildRequires:  libxml2-devel

%description
This program was written to learn about the Buehlmann ZH-L16 model that deals
with accumulation of inert gas in body tissues. Currently it compiles for
GNU/Linux.

Do not use this to plan any dive! 

%prep
%setup -q
bzcat %{SOURCE1} > %{name}-16.png
bzcat %{SOURCE2} > %{name}-32.png
bzcat %{SOURCE3} > %{name}-48.png

%build
%configure LIBS="-lm"
%make

%install
%makeinstall

# icons
install -D -m 644 %{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png 
install -D -m 644 %{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 %{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png 

# menu entry

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=GTK;-MandrivaLinux-MoreApplications-Sciences-Other;Science
EOF

%find_lang %{name} || touch %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.71-7mdv2011.0
+ Revision: 619286
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.71-6mdv2010.0
+ Revision: 429335
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.71-5mdv2009.0
+ Revision: 246680
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-3mdv2008.1
+ Revision: 132439
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gtkdive


* Fri Aug 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-2mdv2007.0
- xdg menu

* Tue Mar 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-1mdk
- New release 0.71
- drop gcc4 patch, merged upstream

* Thu Sep 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-5mdk
- Fix group (fix #18917)

* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-4mdk
- Fix BuildRequires

* Fri Aug 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-3mdk
- fix build
- fix menu entry

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.7-2mdk 
- rebuild

* Mon Apr 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.7-1mdk
- first mdk release
