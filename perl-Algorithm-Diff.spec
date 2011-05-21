%define upstream_name    Algorithm-Diff
%define upstream_version 1.1902

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch:      1

Summary:    Compute `intelligent' differences between two files / lists
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module compute `intelligent' differences between two files / lists.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*
