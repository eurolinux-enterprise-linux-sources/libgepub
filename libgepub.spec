Name:           libgepub
Version:        0.4
Release:        1%{?dist}
Summary:        Library for epub documents

License:        LGPLv2+
URL:            https://git.gnome.org/browse/libgepub
Source0:        https://download.gnome.org/sources/libgepub/0.4/libgepub-%{version}.tar.xz

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
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gepub-0.4.typelib
%{_libdir}/libgepub.so.0*

%files devel
%{_includedir}/libgepub/
%{_libdir}/libgepub.so
%{_libdir}/pkgconfig/libgepub.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gepub-0.4.gir


%changelog
* Thu Sep 01 2016 Kalev Lember <klember@redhat.com> - 0.4-1
- Update to 0.4

* Mon Aug 22 2016 Kalev Lember <klember@redhat.com> - 0.3-0.1.git395779e
- Initial Fedora build
