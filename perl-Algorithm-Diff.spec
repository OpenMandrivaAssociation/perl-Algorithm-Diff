%define upstream_name    Algorithm-Diff
%define upstream_version 1.1902

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5
Epoch:      1

Summary:    Compute `intelligent' differences between two files / lists
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2
Buildrequires:  perl-devel
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.190.200-5mdv2012.0
+ Revision: 765048
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.190.200-4
+ Revision: 763645
- bump release
- fix deps
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.1902

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.190.200-3
+ Revision: 676878
- rebuild
- rebuild
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.1902
    - update to new version 1.1902

* Fri Jul 23 2010 Funda Wang <fwang@mandriva.org> 1:1.190.200-2mdv2011.0
+ Revision: 557122
- rebuild

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.190.200-1mdv2010.1
+ Revision: 503913
- bump epoch
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1902-5mdv2010.0
+ Revision: 426410
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1902-4mdv2009.0
+ Revision: 223497
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1902-3mdv2008.1
+ Revision: 180364
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 1.1902-2mdv2008.0
+ Revision: 43093
- rebuild


* Fri Aug 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.1902-1mdv2007.0
- New version 1.1902

* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.1901-3mdv2007.0
- spec cleanup
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1901-2mdk 
- make test in %%check
- don't ship empty directories

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1901-1mdk 
- new release
- spec cleanup
- better url

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.15-3mdk
- fix buildrequires in a backward compatible way

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.15-2mdk 
- rpmbuildupdate aware

* Wed Jan 07 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.15-1mdk
- first mdk release

