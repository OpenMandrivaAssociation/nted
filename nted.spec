Name: nted
Version: 0.22.3
Release: %mkrel 2
Summary: A new musical score editor for Linux
License: GPLv2+
URL: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/%name-%version.tgz
Patch0: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/slur_patch-0.22.3.patch
BuildRequires: gtk+2-devel
BuildRequires: libalsa-devel
BuildRequires: yelp kdesdk-po2xml

%description
NtEd is a new musical score editor for Linux.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=NtEd
Comment=A new musical score editor for Linux
Exec=nted
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;AudioVideo;GTK;
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif
