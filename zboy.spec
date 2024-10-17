%if %{mdvver} >= 201100
%define		build_gui	1
%else
%define		build_gui	0
%endif

Name:		zboy
Version:	0.52
Release:	2
Summary:	Nintendo GameBoy Emulator
License:	GPLv3
Group:		Emulators
URL:		https://www.viste-family.net/mateusz/software/zboy/
Source0:	http://www.viste-family.net/mateusz/software/%{name}/%{name}_v%{version}_src.zip
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
Source4:	%{name}-64.png
Source5:	%{name}-96.png
Source6:	%{name}-128.png
Patch0:		zboy-0.52-makefile.patch
Patch1:		zboy-0.52-sfmt.patch
BuildRequires:	SDL-devel
%if %{build_gui}
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
%endif

%description
zBoy is a multiplatform GameBoy emulator that provides a load/save feature,
can perform PCX screenshots either manually or automatically (every few
seconds) and emulates an internal battery for ROMs that were designed to use
one (this allows to use the internal save option provided by such games,
remember highest scores, etc).

zBoy supports some additionnal features, too, like intelligent saving of
hi-scores for some games that aren't able to save their hi-scores table by
themselves because of the lack of a battery-backed RAM on the cartridge, and
improving screen's resolution output using graphic algorithms like Scale2x,
Scale3x, eagle... Here you can see a comparison between graphic algorithms
supported by zBoy. This is also one of the very few GameBoy emulators that
provides a 2-gameboys link emulation, which makes it possible to play some
games in 2-players mode on a LAN.

zBoy allows to play GameBoy games using a keyboard or a joypad (or both).

%if %{build_gui}
Since 0.52 zBoy features GTK3 GUI.
%else
WARNING! There is no GUI for zBoy in this Mandriva version because it
doesn't have GTK3 development libraries.
Run the emulator from terminal: zboy your_rom.gb
%endif

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%__cp Makefile.linux Makefile

%build
%setup_compile_flags
%if %{build_gui}
%make zboy-gui
%else
%make zboy-nogui
%endif

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__cp %{name} %{buildroot}%{_bindir}/%{name}

%if %{build_gui}
# icons
%__install -D %{SOURCE1} -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D %{SOURCE2} -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D %{SOURCE3} -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D %{SOURCE4} -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D %{SOURCE5} -m 644 %{buildroot}%{_iconsdir}/hicolor/96x96/apps/%{name}.png
%__install -D %{SOURCE6} -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=zBoy
Comment=Nintendo GameBoy Emulator
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Game;Emulator;
EOF
%endif

%clean
%__rm -rf %{buildroot}

%files
%doc zboy.txt history.txt todo.txt license.txt
%{_bindir}/%{name}
%if %{build_gui}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%endif


%changelog
* Mon Apr 23 2012 Andrey Bondrov <abondrov@mandriva.org> 0.52-1mdv2011.0
+ Revision: 792756
- New version 0.52, now with GTK3 GUI (in MDV 2011+)

* Sun Jan 15 2012 Andrey Bondrov <abondrov@mandriva.org> 0.51-1
+ Revision: 761186
- imported package zboy

