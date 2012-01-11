Name: give
Version: 3.0n
Release: 1
Summary: lc file transfer utility
License: LLNL Internal
Group: System Environment/Base
Source: %{name}-%{version}-%{release}.tgz                                       
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}                            
URL: https://www.git.lanl.gov/filesystems/

%description
Give and take are a set of companion utilities that allow a
secure transfer of files form one user to another without exposing
the files to third parties.

# Don't strip binaries                                                             
%define __os_install_post /usr/lib/rpm/brp-compress                                
%define debug_package %{nil} 

###############################################################################

%prep                                                                              
%setup -n %{name}-%{version}-%{release}                                            
                                                                                   
%build                                                                             
%configure --program-prefix=%{?_program_prefix:%{_program_prefix}}

make %{?_smp_mflags}                                                               

%install
rm -rf "$RPM_BUILD_ROOT"                                                        
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install src/give-assist $RPM_BUILD_ROOT%{_bindir}
install give.py $RPM_BUILD_ROOT%{_bindir}/give
ln $RPM_BUILD_ROOT%{_bindir}/give $RPM_BUILD_ROOT%{_bindir}/take
DESTDIR="$RPM_BUILD_ROOT" make install                                          

###############################################################################

%clean                                                                          
rm -rf $RPM_BUILD_ROOT

###############################################################################

%files
%defattr(-,root,root,0755)
%{_bindir}/give-assist
%{_bindir}/give
%{_bindir}/take
%{_mandir}/man1/give.1.gz
%{_mandir}/man1/take.1.gz
