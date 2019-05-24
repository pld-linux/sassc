Summary:	Wrapper around libsass to compile CSS stylesheet
Summary(pl.UTF-8):	Program obudowujący libsass do kompilowania arkuszy styli CSS
Name:		sassc
Version:	3.6.0
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://github.com/sass/sassc/releases
Source0:	https://github.com/sass/sassc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c8b53f92b61e8485f75552aece8879fc
URL:		https://github.com/sass/sassc
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libsass-devel >= 3.6.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
Requires:	libsass >= 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SassC is a wrapper around libsass used to generate a useful
command-line application that can be installed and packaged for
several operating systems.

%description -l pl.UTF-8
SassC to program obudowujący libsass, tworzący przydatną aplikację
linii poleceń, zdatną do użytku na kilku systemach operacyjnych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
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
%doc LICENSE Readme.md
%attr(755,root,root) %{_bindir}/sassc
