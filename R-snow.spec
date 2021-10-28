#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-snow
Version  : 0.4.4
Release  : 35
URL      : https://cran.r-project.org/src/contrib/snow_0.4-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/snow_0.4-4.tar.gz
Summary  : Simple Network of Workstations
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-Rmpi
BuildRequires : buildreq-R

%description
SNOW: Simple Network of Workstations
The snow package provides support for simple parallel computing on a
network of workstations using R.  A master R process calls makeCluster
to start a cluster of worker processes; the master process then uses
functions such as clusterCall and clusterApply to execute R code on
the worker processes and collect and return the results on the master.
This framework supports many forms of "embarrassingly parallel"
computations.

%prep
%setup -q -c -n snow
cd %{_builddir}/snow

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635379921

%install
export SOURCE_DATE_EPOCH=1635379921
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snow
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snow
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snow
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc snow || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/snow/DESCRIPTION
/usr/lib64/R/library/snow/INDEX
/usr/lib64/R/library/snow/Meta/Rd.rds
/usr/lib64/R/library/snow/Meta/features.rds
/usr/lib64/R/library/snow/Meta/hsearch.rds
/usr/lib64/R/library/snow/Meta/links.rds
/usr/lib64/R/library/snow/Meta/nsInfo.rds
/usr/lib64/R/library/snow/Meta/package.rds
/usr/lib64/R/library/snow/NAMESPACE
/usr/lib64/R/library/snow/R/snow
/usr/lib64/R/library/snow/R/snow.rdb
/usr/lib64/R/library/snow/R/snow.rdx
/usr/lib64/R/library/snow/RMPISNOW
/usr/lib64/R/library/snow/RMPISNOWprofile
/usr/lib64/R/library/snow/RMPInode.R
/usr/lib64/R/library/snow/RMPInode.sh
/usr/lib64/R/library/snow/RSOCKnode.R
/usr/lib64/R/library/snow/RSOCKnode.sh
/usr/lib64/R/library/snow/RunSnowNode
/usr/lib64/R/library/snow/RunSnowWorker
/usr/lib64/R/library/snow/RunSnowWorker.bat
/usr/lib64/R/library/snow/help/AnIndex
/usr/lib64/R/library/snow/help/aliases.rds
/usr/lib64/R/library/snow/help/paths.rds
/usr/lib64/R/library/snow/help/snow.rdb
/usr/lib64/R/library/snow/help/snow.rdx
/usr/lib64/R/library/snow/html/00Index.html
/usr/lib64/R/library/snow/html/R.css
