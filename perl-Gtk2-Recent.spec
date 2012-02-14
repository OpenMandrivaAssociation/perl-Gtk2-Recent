%define upstream_name Gtk2-Recent
%define upstream_version 0.031

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11

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
