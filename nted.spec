Name: nted
Version: 0.13.0
Release: %mkrel 1
Summary: A new musical score editor for Linux
License: GPLv2+
URL: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Group: Graphical desktop/GNOME
Source: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/%name-%version.tgz
BuildRequires: gtk+2-devel
BuildRequires: libalsa-devel

%description
NtEd is a new musical score editor for Linux.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
Name=NtEd
Comment=A new musical score editor for Linux
Exec=nted
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;AudioVideo;
EOF

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT_THE_EXAMPLES.TXT AUTHORS FAQ
%{_bindir}/*
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop

%post
%update_menus

%postun
%clean_menus
