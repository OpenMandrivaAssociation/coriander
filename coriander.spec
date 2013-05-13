%define version		2.0.1
%define release		%mkrel 1

Summary:	GUI for controlling IEEE1394 cameras
Name:		coriander
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Video
Source:		http://downloads.sourceforge.net/project/coriander/coriander-2/%{version}/%{name}-%{version}.tar.gz
URL:		http://damien.douxchamps.net/ieee1394/coriander/
BuildRequires:	SDL-devel
BuildRequires:	ftp-devel
BuildRequires:	dc1394-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(xv)
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Coriander is the Linux graphical user interface (GUI) for controlling
a Digital Camera through the IEEE1394 bus (aka FireWire, or iLink).
Coriander is full featured and besides changing the parameters of the
camera it will also let you record video, send images to an FTP site,
convert the video to a V4L stream,... A live display is of course
provided too. Best of all, Coriander will work with any camera that is
compatible with the IIDC specifications (also known as DCAM specs).
This includes most 1394 webcams and a majority of industrial or
scientific cameras too.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/coriander
%dir %{_datadir}/pixmaps/coriander
%{_datadir}/pixmaps/coriander/coriander-icon.png
%{_datadir}/pixmaps/coriander/coriander-logo.png


%changelog
* Sat Oct 02 2010 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 582469
- New version 2.0.1

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-2mdv2010.0
+ Revision: 437126
- rebuild

* Sat Jun 21 2008 Stefan van der Eijk <stefan@mandriva.org> 2.0.0-1mdv2009.0
+ Revision: 227806
- 2.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Jan 18 2008 Stefan van der Eijk <stefan@mandriva.org> 2.0.0-0.rc6.1mdv2008.1
+ Revision: 154563
- 2.0.0 rc6

  + Funda Wang <fwang@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 11 2007 Stefan van der Eijk <stefan@mandriva.org> 2.0.0-0.rc5.1mdv2008.0
+ Revision: 38012
- 2.0.0-rc5


* Sun Jan 21 2007 Stefan van der Eijk <stefan@mandriva.org> 2.0.0-0.rc4.1mdv2007.0
+ Revision: 111251
- 2.0.0-rc4
- 2.0.0-rc3
- 2.0.0-rc2

* Wed Oct 25 2006 Stefan van der Eijk <stefan@mandriva.org> 2.0.0-0.rc1.1mdv2007.0
+ Revision: 72245
- 2.0.0-rc1
- Import coriander

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0.0-0.pre6.3mdv2007.0
- Rebuild with latest dbus

* Mon Jun 12 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.0-0.pre6.2mdk
- fix BuildRequires for sparc64

* Thu May 11 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.0-0.pre6.1mdk
- 2.0.0-pre6

* Wed Mar 22 2006 Jerome Martin <jerome.f.martin@free.fr> 2.0.0-0.pre5.2mdk
- Fixed BuildRequires

* Mon Mar 20 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.0-0.pre5.1mdk
- 2.0.0-pre5

* Tue Dec 27 2005 Stefan van der Eijk <stefan@eijk.nu> 2.0.0-0.pre4.1mdk
- initial package

