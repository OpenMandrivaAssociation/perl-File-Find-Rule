%define	modname	File-Find-Rule
%define modver 0.34

Summary:	Alternative interface to File::Find
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/File-Find-Rule-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Text::Glob)
BuildRequires:	perl(Number::Compare)
BuildRequires:  perl(Test::More)

%description 
File::Find::Rule is a friendlier interface to File::Find. It allows you to
build rules which specify the desired files and directories.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/File
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*


