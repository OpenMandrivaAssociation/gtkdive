%define name    gtkdive
%define version 0.71
%define release %mkrel 3

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
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%configure
%make

%install
rm -rf %{buildroot}
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

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

