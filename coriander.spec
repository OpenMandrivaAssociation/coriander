%define version		2.0.0
%define subversion	rc5
%define release		%mkrel 0.%{subversion}.1

Summary:	Coriander is a GUI for controlling IEEE1394 cameras
Name:		coriander
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Video
Source:		%{name}-%{version}-%{subversion}.tar.bz2
URL:		http://damien.douxchamps.net/ieee1394/coriander/
BuildRequires:	SDL-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libdc1394-devel >= 2.0.0-0.rc5
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

%setup -q -n %{name}-%{version}-%{subversion}

%build
%configure
%make

%install
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/coriander
%{_datadir}/pixmaps/coriander/coriander-icon.png
%{_datadir}/pixmaps/coriander/coriander-logo.png


