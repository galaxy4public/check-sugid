Name:		check-sugid
Version:	0.0.1
Release:	1
License:	GPLv3+
Group:		System Environment/Base/Security
Summary:	A tool to perform a quick scan for binaries with extensive privileges
Url:		https://github.com/galaxy4public/check-sugid

Source0:	%name.script

Requires:	attr, coreutils, findutils, grep, libcap, sed

BuildArch:	noarch

%description
The check-sugid script scans the system for any binaries with extensive
privileges and prints the list out in a format compatible with the
post-transaction-actions Yum plugin, so it would be possible to define
rules for the detected binaries and these rules will be enforced on
package installations/updates.

The script could be used as a standalone tool, but the recomended way
is to call from the at-exit Yum plugin, so the check is performed each
time there is a change to the package set.

%install
rm -rf -- '%buildroot'
mkdir -p -m755 '%buildroot%_sbindir'
install -m700 -p '%_sourcedir/%name.script' '%buildroot%_sbindir/%name'

%files
%defattr(0600,root,root,0700)
%attr(0700,root,root) %_sbindir/%name

%changelog
* Sun Apr 03 2016 (GalaxyMaster) <galaxy-at-openwall.com> - 0.0.1-1
- Initial release to the public.
