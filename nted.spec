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

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT_THE_EXAMPLES.TXT AUTHORS FAQ
%{_bindir}/*
%{_datadir}/%name
%{_mandir}/man1/*
