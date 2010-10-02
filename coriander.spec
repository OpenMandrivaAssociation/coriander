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
BuildRequires:	libgnomeui2-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libxv-devel
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
