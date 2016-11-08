#%%global _internal_version  c147867

Name:           mate-icon-theme-faenza
Version:        1.16.0
Release:        2%{?dist}
#Release:        0.1.git%{_internal_version}%{?dist}
Summary:        Extra set of icon themes for MATE Desktop
License:        GPLv2+
URL:            http://mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz
#Source0: http://raveit65.fedorapeople.org/Mate/git-upstream/%{name}-%{version}.git%{_internal_version}.tar.xz

Source0:        http://pub.mate-desktop.org/releases/1.16/%{name}-%{version}.tar.xz

BuildRequires: hardlink
BuildRequires: mate-common

BuildArch: noarch

%description
Provides a complimentary set of icon themes for MATE Desktop


%prep
%setup -q
#%setup -q -n %{name}-%{_internal_version}

# nedded for git snapshots
NOCONFIGURE=1 ./autogen.sh

%build
%configure
make %{?_smp_mflags} V=1

%install
%{make_install}

# save space by linking identical images
hardlink -c -v %{buildroot}%{_datadir}/icons


%post
/bin/touch --no-create %{_datadir}/icons/matefaenza &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzagray &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzadark &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/matefaenza &> /dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenza &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons//matefaenzadark &> /dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenzadark &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons//matefaenzagray &> /dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenzagray &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenza &> /dev/null || :
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenzadark &> /dev/null || :
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/matefaenzagray &> /dev/null || :


%files
%{_datadir}/icons/matefaenzagray
%{_datadir}/icons/matefaenzadark
%{_datadir}/icons/matefaenza
%doc AUTHORS COPYING README NEWS


%changelog
* Tue Nov 08 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.16.0-2
- Fix Source0 D/L link

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Wed Jun 15 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0.1
- update to 1.10.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Mon Jan 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.7.0-1
- update to 1.7.0 release
- use modern 'make install' macro

* Thu Sep 12 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-0.1.gitc147867
- update latest git snapshot
- fix mate-icon-theme-faenza included Trademark and non-free logo, rhbz (#1005464)

* Wed Jul 31 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Initial build
