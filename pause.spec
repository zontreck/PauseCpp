Name:           pause
Version:        1.0.0
Release:        1%{?dist}
Summary:        Pause

License:        GPLv3
URL:            https://github.com/zontreck/PauseCpp
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc cmake


%description
A terminal pause command that waits for user input

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Mon May 22 2023 Aria <tarapiccari@gmail.com>
- 1.0.0 initial release
