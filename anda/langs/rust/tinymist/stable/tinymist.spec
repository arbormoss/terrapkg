Name:           tinymist
Version:        0.14.6
Release:        1%?dist
Summary:        Tinymist [ˈtaɪni mɪst] is an integrated language service for Typst [taɪpst]
URL:            https://myriad-dreamin.github.io/%{name}
Source0:        https://github.com/Myriad-Dreamin/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        Apache-2.0
BuildRequires:  cargo-rpm-macros mold

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/%{name}                %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies
%doc README.md CHANGELOG.md CODEOWNERS MAINTAINERS.md CONTRIBUTING.md
%{_bindir}/%{name}

%changelog
* Sat Jan 3 2026 arbormoss <arbormoss@woodsprite.dev>
- Initial commit
