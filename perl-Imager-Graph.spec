#
# Conditional build:
%bcond_with	tests	# perform "make test"
#			  (fails, probably because of newer Imager)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Imager
%define		pnam	Graph
Summary:	Imager::Graph - producing graphs using the Imager library
Summary(pl.UTF-8):	Imager::Graph - tworzenie wykresów przy użyciu biblioteki Imager
Name:		perl-Imager-Graph
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Imager/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5c025695893c5ef192c48f33f5aecc09
URL:		http://search.cpan.org/dist/Imager-Graph/
BuildRequires:	perl-Imager >= 0.39
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Imager >= 0.75
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imager::Graph is intended to produce good looking graphs with a
minimum effort on the part of the user. Currently only the pie graph
class, Imager::Graph::Pie, is provided.

%description -l pl.UTF-8
Imager::Graph ma służyć do tworzenia dobrze wyglądających wykresów
przy minimalnym wysiłku użytkownika. Aktualnie dostępna jest tylko
klasa do wykresów kołowych - Imager::Graph::Pie.

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
