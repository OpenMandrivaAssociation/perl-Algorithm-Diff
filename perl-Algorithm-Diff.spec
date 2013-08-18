%define upstream_name    Algorithm-Diff
%define upstream_version 1.1902

Summary:	Compute `intelligent' differences between two files / lists
Epoch:	1
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2
Buildarch:	noarch
Buildrequires:	perl-devel

%description
This module compute `intelligent' differences between two files / lists.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc README Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/man3/*

