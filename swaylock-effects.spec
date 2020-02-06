Name:       swaylock-effects
Version:    1.4.1
Release:    1%{?dist}
Summary:    Swaylock, with fancy effects

%define commit 6f29f07654b289e870ffb0c619410c2f09c9259b

License:    MIT
URL:        https://github.com/mortie/swaylock-effects
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Older versions were part of the sway package
Conflicts:      sway < 1.0

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

%define program_name swaylock

%description
swaylock-effects is a screen locking utility for Wayland compositors, with fancy effects.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{program_name}
%{_mandir}/man1/%{program_name}.1*
%config(noreplace) %{_sysconfdir}/pam.d/%{program_name}

# Co-own completion directories
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{program_name}

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{program_name}

%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/fish/completions/%{program_name}.fish


%changelog
* Tue Feb 04 2020 Edd Salkield <edd@salkield.uk> - 1.4-1
- Initial package import
