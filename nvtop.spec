Name:           nvtop
Version:        3.2.0
Release:        1
Summary:        GPU process monitoring for AMD, Intel and NVIDIA
Group:          Monitoring
License:        GPL-3.0-or-later and BSD-3-Clause
URL:            https://github.com/Syllo/nvtop
Source0:        https://github.com/Syllo/nvtop/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(udev)

Requires:       hicolor-icon-theme

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD, Intel
and NVIDIA GPUs. It can handle multiple GPUs and print information about them in
a htop familiar way.

%prep
%autosetup -p1

%build
%cmake  \
        -DNVIDIA_SUPPORT=ON \
        -DAMDGPU_SUPPORT=ON \
        -DINTEL_SUPPORT=ON

%make_build

%install
%make_install -C build

%files
%license COPYING
%doc README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/nvtop.svg
%{_datadir}/metainfo/nvtop.metainfo.xml
