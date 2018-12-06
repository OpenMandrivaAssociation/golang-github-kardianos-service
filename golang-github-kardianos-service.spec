# Run tests in check section
# Tests fail on COPR
%bcond_with check

%global goipath         github.com/kardianos/service
%global commit          615a14ed75099c9eaac6949e22ac2341bf9d3197

%global common_description %{expand:
service will install / un-install, start / stop, and run a program as a 
service (daemon). Currently supports Windows XP+, Linux/(systemd | Upstart |
SysV), and OSX/Launchd.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Run go programs as a service on major platforms
License:        zlib
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git615a14e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180509git615a14e
- First package for Fedora

