%define upstream_name Gtk2-Recent
%define upstream_version 0.031

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	13

Summary:	Perl module for the Recently used Files list
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Gtk2-Recent-0.031-error-format-security.patch

BuildRequires:	pkgconfig(glitz)
Buildrequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib) > 1.00
Buildrequires:	perl(Gnome2::VFS)
BuildRequires:	perl(Gtk2)
Buildrequires:	perl-devel

Requires:	gtk+2

%description
This module allows a Perl programmer to access the Recently used Files list
using the libegg component.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 
%patch0 -p0 -b .fmtsec

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
#%make test || :

%install
%makeinstall_std

%files
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/Gtk2


%changelog
* Tue Feb 14 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 0.31.0-11
+ Revision: 774113
- add missing '-p0' flag to patch
- don't pass '-s' to compiler flags
- cleanout spec
- use pkgconfig() dependencies for buildrequires
- mass rebuild of perl extensions against perl 5.14.2

* Tue Mar 16 2010 J√©r√¥me Quelin <jquelin@mandriva.org> 0.31.0-10mdv2011.0
+ Revision: 521904
- rebuild using %%perl_convert_version; fix error format security

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.031-8mdv2009.0
+ Revision: 257167
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.031-6mdv2008.1
+ Revision: 152111
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.031-5mdv2008.0
+ Revision: 43102
- rebuild


* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.031-4mdk
- BuildRequiress glitz-devel

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.031-3mdk
- Another buildrequire fix

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.031-2mdk
- Add buildrequires
- mkrel

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.031-1mdk
- initial release

