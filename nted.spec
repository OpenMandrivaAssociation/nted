Summary:	Musical score editor
Name:		nted
Version:	1.10.18
Release:	2
License:	GPLv2+
Group:		Sound
Url:		http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Source0:	http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/sources/%{name}-%{version}.tar.gz
Patch0:		nted-1.10.18-sfmt.patch
Patch1:		nted-1.10.18-headers.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)

%description
NtEd is a GTK score editor. It intends to be really WYSIWYG:
what you see on the screen is exactly what you get on printer
output. It supports up to 4 voices per staff, drum notes, 5 lyrics
lines, N-Tuplets, context changes, repeats with alternatives,
configurable music instruments per staff, MIDI and Postscript
export, MusicXML import. Scores can be played through the ALSA sequencer.

%files -f %{name}.lang
%doc COPYING AUTHORS FAQ
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/packages

#new style menu
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=NtEd
GenericName=Score editor
GenericName[de]=Partitureditor
GenericName[fr]=Éditeur de partition
GenericName[it]=Redattore di spartiti
Comment=Edit musical scores
Comment[de]=Bearbeitet (musikal.) Partituren
Comment[fr]=Ėdite des partitions musicales
Comment[it]=Redige spartiti musicali
Exec=%{name}
Icon=%{name}
StartupNotify=true
Terminal=false
MimeType=application/x-%{name};
Type=Application
Categories=Audio;Midi;Music;
EOF

#new style mime-type
cat > %{buildroot}%{_datadir}/mime/packages/%{name}.xml <<EOF
<?xml version="1.0"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-nted">
    <comment>nted file</comment>
    <glob pattern="*.ntd"/>
     <magic priority="60">
       <match value="nted-file" type="string" offset="20:140"/>
     </magic>
  </mime-type>
</mime-info>
EOF

%find_lang %{name}

