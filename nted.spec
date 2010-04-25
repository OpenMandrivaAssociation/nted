Name:		nted
Version:	1.10.1
Release:	%mkrel 1
Summary:	A new musical score editor for Linux
License:	GPLv2+
URL:		http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/sources/%{name}-%{version}.tar.gz
Patch0:		nted-1.10.1-fix-desktop.patch
Patch1:		nted-1.10.1-fix-str-fmt.patch
BuildRequires:	gtk+2-devel
BuildRequires:	libalsa-devel
BuildRequires:	yelp kdesdk4-po2xml xmlto
BuildRequires:	gettext-devel

%description
NtEd is a new musical score editor for Linux.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .strfmt

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
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/nted.png
