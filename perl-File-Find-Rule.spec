%define	upstream_name	 File-Find-Rule
%define upstream_version 0.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Alternative interface to File::Find
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Glob)
BuildRequires:	perl(Number::Compare)
BuildArch:	noarch

%description 
File::Find::Rule is a friendlier interface to File::Find. It allows you to
build rules which specify the desired files and directories.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/File
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-4mdv2012.0
+ Revision: 765240
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-3
+ Revision: 763753
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.320.0-2
+ Revision: 676629
- rebuild

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2011.0
+ Revision: 471052
- update to 0.32

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 403168
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.30-4mdv2009.0
+ Revision: 241215
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-2mdv2008.0
+ Revision: 46977
- rebuild


* Tue Jun 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2007.0
- New release 0.30
- HTTP source URL

* Wed May 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdk
- New release 0.29
- better source URL
- better buildrequires syntax

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-3mdk 
- don't ship useless empty dirs
- spec cleanup
- rpmbuildupdate aware
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.28-2mdk
- fix buildrequires in a backward compatible way

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.28-1mdk
- 0.28

* Tue Mar 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.27-1mdk
- first mdk release

