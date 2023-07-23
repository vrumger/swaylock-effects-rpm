%define upstreamversion 1.6
%define forkversion 4

Name:       swaylock-effects
Version:    %{upstreamversion}.%{forkversion}
Release:    1%{?dist}
Summary:    Swaylock, with fancy effects

License:    MIT
Source0:    https://github.com/mortie/swaylock-effects/archive/refs/tags/v%{upstreamversion}-%{forkversion}.tar.gz

# Older versions were part of the sway package
Conflicts:      sway < 1.0

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  scdoc

%define program_name swaylock

%description
swaylock-effects is a screen locking utility for Wayland compositors, with fancy effects.

%prep
%autosetup -n %{name}-%{upstreamversion}-%{forkversion}

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
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{program_name}.fish


%changelog
* Sun Jul 23 2023 TRS-SoD <the_real_skull@hotmail.com> - 1.6-4
- Upgrade to version 1.6-3 https://github.com/mortie/swaylock-effects/releases/tag/v1.6-4
* Thu Feb 11 2021 Edd Salkield <edd@salkield.uk> - 1.6-3
- Upgrade to version 1.6-3 https://github.com/mortie/swaylock-effects/releases/tag/v1.6-3
* Wed Sep 23 2020 Edd Salkield <edd@salkield.uk> - 1.6-1
- Upgrade to version 1.6-1 https://github.com/mortie/swaylock-effects/releases/tag/v1.6-1
* Thu Feb 06 2020 Edd Salkield <edd@salkield.uk> - 1.6-0
- Upgrade to version 1.6-0 https://github.com/mortie/swaylock-effects/releases/tag/v1.6-0
* Tue Feb 04 2020 Edd Salkield <edd@salkield.uk> - 1.4-1
- Initial package import
