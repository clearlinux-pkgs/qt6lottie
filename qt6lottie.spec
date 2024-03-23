#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : qt6lottie
Version  : 6.6.2
Release  : 14
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtlottie-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtlottie-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6lottie-lib = %{version}-%{release}
Requires: qt6lottie-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6lottie package.
Group: Development
Requires: qt6lottie-lib = %{version}-%{release}
Provides: qt6lottie-devel = %{version}-%{release}
Requires: qt6lottie = %{version}-%{release}

%description dev
dev components for the qt6lottie package.


%package lib
Summary: lib components for the qt6lottie package.
Group: Libraries
Requires: qt6lottie-license = %{version}-%{release}

%description lib
lib components for the qt6lottie package.


%package license
Summary: license components for the qt6lottie package.
Group: Default

%description license
license components for the qt6lottie package.


%prep
%setup -q -n qtlottie-everywhere-src-6.6.2
cd %{_builddir}/qtlottie-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711164342
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711164342
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6lottie
cp %{_builddir}/qtlottie-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6lottie/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtlottie-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6lottie/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtlottie-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6lottie/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/beziereasing_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmbase_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmbasictransform_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmconstants_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmellipse_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmfill_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmfilleffect_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmfreeformshape_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmgfill_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmgroup_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmimage_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmimagelayer_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmlayer_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmpathtrimmer_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmproperty_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmrect_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmrepeater_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmrepeatertransform_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmround_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmshape_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmshapelayer_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmshapetransform_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmspatialproperty_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmstroke_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/bmtrimpath_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/lottierenderer_p.h
/usr/include/QtBodymovin/6.6.2/QtBodymovin/private/trimpath_p.h
/usr/include/QtBodymovin/QtBodymovin
/usr/include/QtBodymovin/QtBodymovinDepends
/usr/include/QtBodymovin/QtBodymovinVersion
/usr/include/QtBodymovin/bmglobal.h
/usr/include/QtBodymovin/qtbodymovinversion.h
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateConfig.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateDependencies.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateTargets.cmake
/usr/lib64/cmake/Qt6BodymovinPrivate/Qt6BodymovinPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6lottieqtpluginTargets.cmake
/usr/lib64/libQt6Bodymovin.prl
/usr/lib64/libQt6Bodymovin.so
/usr/lib64/qt6/mkspecs/modules/qt_lib_bodymovin_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Bodymovin.so.6.6.2
/V3/usr/lib64/qt6/qml/Qt/labs/lottieqt/liblottieqtplugin.so
/usr/lib64/libQt6Bodymovin.so.6
/usr/lib64/libQt6Bodymovin.so.6.6.2
/usr/lib64/qt6/metatypes/qt6bodymovinprivate_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/BodymovinPrivate.json
/usr/lib64/qt6/qml/Qt/labs/lottieqt/liblottieqtplugin.so
/usr/lib64/qt6/qml/Qt/labs/lottieqt/plugins.qmltypes
/usr/lib64/qt6/qml/Qt/labs/lottieqt/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6lottie/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6lottie/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6lottie/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
