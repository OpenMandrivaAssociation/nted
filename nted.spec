Name: nted
Version: 1.9.10
Release: %mkrel 1
Summary: A new musical score editor for Linux
License: GPLv2+
URL: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/%name-%version.tar.gz
Patch0: nted-1.4.17-fix-desktop.patch
Patch1: nted-1.9.10-mdv-fix-str-fmt.patch
BuildRequires: gtk+2-devel
BuildRequires: libalsa-devel
BuildRequires: yelp kdesdk4-po2xml xmlto
BuildRequires: gettext-devel

%description
NtEd is a new musical score editor for Linux.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .strfmt

%build
autoreconf -fi
%configure2_5x --docdir=%_datadir/docs
%make

%install
rm -rf %buildroot
%makeinstall_std

mv %buildroot%_datadir/docs .

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT_THE_EXAMPLES.TXT AUTHORS FAQ
%doc docs/*
%{_bindir}/*
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/nted.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif
