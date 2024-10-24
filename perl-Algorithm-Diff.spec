%define upstream_name    Algorithm-Diff

Summary:	Compute `intelligent' differences between two files / lists
Name:		perl-%{upstream_name}
Version:	1.201
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Algorithm::Diff
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{version}.tar.gz
Buildarch:	noarch
Buildrequires:	perl(Test)
Buildrequires:	perl-devel

%description
This module compute `intelligent' differences between two files / lists.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
make test

%files 
%doc README Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/man3/*
