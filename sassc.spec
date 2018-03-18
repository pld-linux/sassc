Summary:	Wrapper around libsass to compile CSS stylesheet
Name:		sassc
Version:	3.5.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/sass/sassc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5c6aeb4e98c96d093f20295fc490f2c
URL:		https://github.com/sass/sassc
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libsass-devel >= 3.5.0
BuildRequires:	libtool
Requires:	libsass >= 3.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SassC is a wrapper around libsass used to generate a useful
command-line application that can be installed and packaged for
several operating systems.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md
%attr(755,root,root) %{_bindir}/sassc
