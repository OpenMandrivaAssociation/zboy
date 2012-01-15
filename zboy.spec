%define		oversion 51

Summary:	Nintendo GameBoy Emulator
Name:		zboy
Version:	0.%{oversion}
Release:	%mkrel 1
License:	GPLv3
Group:		Emulators
URL:		http://www.viste-family.net/mateusz/software/zboy/
Source0:	http://www.viste-family.net/mateusz/software/%{name}/%{name}0%{oversion}-src.zip
BuildRequires:	SDL-devel

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

WARNING! There is no GUI yet. Run the emulator from terminal: zboy your_rom.gb

%prep
%setup -q -n %{name}_source

%build
%ifarch x86_64
%make linux64
%else
%make linux
%endif

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__cp %{name} %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc zboy.txt history.txt todo.txt license.txt
%{_bindir}/%{name}
