# TODO: fix pl
# TODO: fix applnk/Applications/kallery.desktop hack
######		Unknown group!
Summary:	Image gallery generator program for KDE
Summary(pl):	Generator galerii plikow graficznych dla KDE
Name:		kallery
Version:	1.0.7a
Release:	1
License:	GPL
Group:		Graphics
Source0:	http://kallery.kdewebdev.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7378740aaeac45062b35e33c07e329b1
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

%description -l pl
Kallery jest �atwym w u�yciu generatorem galerii grafik z podobnym do
czarodziei interfjesem. Mo�na nim robi� �adnie wygladaj�ce gotowe do
publikacji strony www z zapisanych plik�w graficznych. Niekt�re z
najwa�niejszych mo�liwosci:
- obs�uguje wiele formatow plik�w graficznych poprzez ImageMagick
- automatycznie generuje miniatury grafik
- konwertuje pliki z r�nych formatow
- mo�liwe jest dodanie opisow do obrazkow
- spos�b generacji galerii w HTML jest wysoce konfigurowalny
- u�ywa szablon�w do genrowania galleri
- pozwala na zapis oraz odczyt plik�w projekt�w aby generowac
  wielokrotnie z zmienionymi bad� nie ustawieniami.

%prep
#setup -q -n %{name}
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

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kallery.desktop $RPM_BUILD_ROOT/%{_desktopdir}
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
#%{_pixmapsdir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
#%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
