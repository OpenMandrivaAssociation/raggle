%define name raggle
%define version 0.4.4
%define release %mkrel 5

Summary: A console RSS aggregator with a curses ui
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Networking/News
URL: http://www.raggle.org/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel
Requires: ruby-ncurses
BuildArch: noarch

%description
Raggle is a console RSS aggregator, written in Ruby. Features include 
customizable keybindings, basic HTML rendering, HTTP proxy support, 
OPML import/export, themes, support for various versions of RSS, 
Screen support. browser auto-detection, and more. 

%prep
%setup -q 

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
make install PREFIX=%buildroot/%_prefix
rm -Rf %buildroot/%_datadir/doc/

%files
%defattr(-,root,root)
%doc AUTHORS  ChangeLog  doc/*  README  TODO
%doc BUGS     COPYING 
%_bindir/*
%_mandir/man1/*
%_datadir/%name/




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-5mdv2010.0
+ Revision: 433055
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-4mdv2009.0
+ Revision: 260041
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-3mdv2009.0
+ Revision: 247819
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4.4-1mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 11 2006 Michael Scherer <misc@mandriva.org> 0.4.4-1mdv2007.0
+ Revision: 95046
- Import raggle

