#
# Conditional build:
%bcond_with	tests	# perform "make test"
#			  (fails, probably because of newer Imager)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Imager
%define		pnam	Graph
Summary:	Imager::Graph - producing graphs using the Imager library
Summary(pl):	Imager::Graph - tworzenie wykresów przy u¿yciu biblioteki Imager
Name:		perl-Imager-Graph
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec53f2eb28a8ac4269d3edf14bd631d5
BuildRequires:	perl-Imager >= 0.39
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Imager >= 0.39
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imager::Graph is intended to produce good looking graphs with a
minimum effort on the part of the user. Currently only the pie graph
class, Imager::Graph::Pie, is provided.

%description -l pl
Imager::Graph ma s³u¿yæ do tworzenia dobrze wygl±daj±cych wykresów
przy minimalnym wysi³ku u¿ytkownika. Aktualnie dostêpna jest tylko
klasa do wykresów ko³owych - Imager::Graph::Pie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Imager/Graph.pm
%{perl_vendorlib}/Imager/Graph
%{_mandir}/man3/*
