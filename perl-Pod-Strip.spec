#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Strip
Summary:	Pod::Strip - Remove POD from Perl code
#Summary(pl):	
Name:		perl-Pod-Strip
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DO/DOMM/Pod-Strip-1.02.tar.gz
# Source0-md5:	b5ac7b0e68d8d44bd737f1ba71aaee3f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Pod::Simple) >= 3.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.



# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Pod/*.pm
#%%{perl_vendorlib}/Pod/Strip
%{_mandir}/man3/*
