# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate blake3

Name:           rust-blake3
Version:        1.3.3
Release:        %autorelease
Summary:        BLAKE3 hash function

License:        CC0-1.0 OR Apache-2.0
URL:            https://crates.io/crates/blake3
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
The BLAKE3 hash function.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CONTRIBUTING.md
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

%package     -n %{name}+digest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+digest-devel %{_description}

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%files       -n %{name}+digest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+neon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+neon-devel %{_description}

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%files       -n %{name}+neon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_avx2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_avx2-devel %{_description}

This package contains library source intended for building other packages which
use the "no_avx2" feature of the "%{crate}" crate.

%files       -n %{name}+no_avx2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_avx512-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_avx512-devel %{_description}

This package contains library source intended for building other packages which
use the "no_avx512" feature of the "%{crate}" crate.

%files       -n %{name}+no_avx512-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_neon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_neon-devel %{_description}

This package contains library source intended for building other packages which
use the "no_neon" feature of the "%{crate}" crate.

%files       -n %{name}+no_neon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_sse2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_sse2-devel %{_description}

This package contains library source intended for building other packages which
use the "no_sse2" feature of the "%{crate}" crate.

%files       -n %{name}+no_sse2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_sse41-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_sse41-devel %{_description}

This package contains library source intended for building other packages which
use the "no_sse41" feature of the "%{crate}" crate.

%files       -n %{name}+no_sse41-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prefer_intrinsics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prefer_intrinsics-devel %{_description}

This package contains library source intended for building other packages which
use the "prefer_intrinsics" feature of the "%{crate}" crate.

%files       -n %{name}+prefer_intrinsics-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pure-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pure-devel %{_description}

This package contains library source intended for building other packages which
use the "pure" feature of the "%{crate}" crate.

%files       -n %{name}+pure-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+traits-preview-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+traits-preview-devel %{_description}

This package contains library source intended for building other packages which
use the "traits-preview" feature of the "%{crate}" crate.

%files       -n %{name}+traits-preview-devel
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
