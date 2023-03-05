# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate page_size

Name:           rust-page_size
Version:        0.5.0
Release:        %autorelease
Summary:        Easy, fast, cross-platform way to retrieve the memory page size

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/page_size
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          page_size-fix-metadata-auto.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Provides an easy, fast, cross-platform way to retrieve the memory page
size.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_std-devel %{_description}

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%files       -n %{name}+no_std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+spin-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spin-devel %{_description}

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

%files       -n %{name}+spin-devel
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
