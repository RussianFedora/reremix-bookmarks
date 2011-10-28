Name:           reremix-bookmarks
Version:        6
Release:        2.R
Summary:        Scientific Linux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.scientificlinux.org/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Scientific Linux

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Fri Oct 28 2011 Arkady L. Shane <ashejn@russianfedora.ru> 6-2.R
- update for RERemix Linux

* Fri Nov 12 2010 Troy Dawson <dawson@fnal.gov> 6-1.sl6
- Updated to final SL 6 release

* Wed Jul 14 2010 Troy Dawson <dawson@fnal.gov> 6-0.sl6
- Changed the bookmarks to be SL's bookmarks

* Fri Jan 29 2010 Christopher Aillon <caillon@redhat.com> 6-0
- Initial SRPM

