# Generated by rust2rpm 24
%bcond_without check

%global crate bunyan

Name:           rust-bunyan
Version:        0.1.9
Release:        %autorelease
Summary:        CLI to pretty print structured logs

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bunyan
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A CLI to pretty print structured logs. A Rust port of the original
JavaScript bunyan CLI.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
# FIXME: no license files detected
%doc README.md
%doc benchmark_logs.txt
%{_bindir}/bunyan

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/benchmark_logs.txt
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog