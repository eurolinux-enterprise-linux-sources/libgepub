%global apiver 0.6

Name:           libgepub
Version:        0.6.0
Release:        1%{?dist}
Summary:        Library for epub documents

License:        LGPLv2+
URL:            https://git.gnome.org/browse/libgepub
Source0:        https://download.gnome.org/sources/libgepub/0.6/libgepub-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

%description
libgepub is a GObject based library for handling and rendering epub
documents.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gepub-%{apiver}.typelib
%{_libdir}/libgepub-%{apiver}.so.0*

%files devel
%{_includedir}/libgepub-%{apiver}/
%{_libdir}/libgepub-%{apiver}.so
%{_libdir}/pkgconfig/libgepub-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gepub-%{apiver}.gir


%changelog
* Thu Mar 15 2018 Kalev Lember <klember@redhat.com> - 0.6.0-1
- Update to 0.6.0
- Resolves: #1569288

* Thu Sep 01 2016 Kalev Lember <klember@redhat.com> - 0.4-1
- Update to 0.4

* Mon Aug 22 2016 Kalev Lember <klember@redhat.com> - 0.3-0.1.git395779e
- Initial Fedora build
