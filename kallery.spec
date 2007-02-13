# TODO: fix applnk/Applications/kallery.desktop hack
Summary:	Image gallery generator program for KDE
Summary(pl.UTF-8):	Generator galerii plików graficznych dla KDE
Name:		kallery
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://kallery.kdewebdev.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	5318e3b8d4e04e1ea9f9a53e5a565d9c
URL:		http://kallery.kdewebdev.org/index.php
BuildRequires:	ImageMagick-devel >= 6.1.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kallery is an easy to use image gallery generator application with a
wizard-like interfaces. One can create nicely looking,
ready-to-publish web pages from your digitally stored images. Some of
the most important features are:
- handles a lot of image formats, thanks to ImageMagick
- automatically generates thumbnails with the help of ImageMagick
- converts the images in other formats (eg. JPEG)
- it's possible to create descriptions for images
- the output HTML gallery is highly configurable
- uses templates for the gallery
- save and load of the project files, so you can regenerate the
  gallery later with the same or different settings.

%description -l pl.UTF-8
Kallery jest łatwym w użyciu generatorem galerii grafik z podobnym do
czarodziei interfejsem. Można nim robić ładnie wyglądające gotowe do
publikacji strony WWW z zapisanych plików graficznych. Niektóre z
najważniejszych możliwości:
- obsługuje wiele formatów plików graficznych poprzez ImageMagick
- automatycznie generuje miniatury grafik
- konwertuje pliki z różnych formatów
- możliwe jest dodanie opisów do obrazków
- sposób generowania galerii w HTML-u jest wysoce konfigurowalny
- używa szablonów do generowania galerii
- pozwala na zapis oraz odczyt plików projektów aby generować
  wielokrotnie z zmienionymi bądź nie ustawieniami.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
#%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
