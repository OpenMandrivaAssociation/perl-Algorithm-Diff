%define upstream_name    Algorithm-Diff
%define upstream_version 1.201

Summary:	Compute `intelligent' differences between two files / lists
Epoch:		1
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Algorithm::Diff
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz
Buildarch:	noarch
Buildrequires:	perl(Test)
Buildrequires:	perl-devel

%description
This module compute `intelligent' differences between two files / lists.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc README Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/man3/*
