# Generated by rust2rpm 24
%bcond_without check

%global crate zenith
%global tag 0.14.0

Name:           rust-zenith
Version:        %{tag}
Release:        %autorelease
Summary:        Similar to top or htop but with CPU, Network Usage, and Disk Usage charts

License:        MIT
URL:            https://github.com/bvaisvil/zenith
Source0:	https://github.com/bvaisvil/zenith/archive/refs/tags/%{tag}.tar.gz

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Similar to top or htop but with CPU, Network Usage, and Disk Usage
charts.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/zenith

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f nvidia

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
