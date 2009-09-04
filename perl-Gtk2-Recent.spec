%define module Gtk2-Recent
%define fmodule Gtk2/Recent

Summary: Perl module for the Recently used Files list
Name:    perl-%module
Version: 0.031
Release: %mkrel 9
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: gtkspell-devel perl-ExtUtils-Depends perl-Gtk2
BuildRequires: perl-Glib > 1.00 perl-ExtUtils-PkgConfig 
Buildrequires: perl-devel
Buildrequires: perl-Gnome2-VFS
Buildrequires: gnomeui2-devel
BuildRequires: glitz-devel

Requires: gtk+2

%description
This module allows a Perl programmer to access the Recently used Files list
using the libegg component.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}*
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule

