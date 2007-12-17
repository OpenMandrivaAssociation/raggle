%define name raggle
%define version 0.4.4
%define release %mkrel 1

Summary: A console RSS aggregator with a curses ui
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Networking/News
URL: http://www.raggle.org/
Source0: %{name}-%{version}.tar.bz2
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


