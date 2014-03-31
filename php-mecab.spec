Summary: The PHP bindings of the MeCab.
Name: php-pecl-mecab
Version: 0.5.0
Release: 1
License: MIT
Group: Development/Languages
Source0: php-mecab-%{version}.tar.gz
Source1: mecab.ini
URL: https://github.com/rsky/php-mecab

BuildRequires: mecab-devel
BuildRequires: php-devel

Requires: mecab
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}

BuildRoot: %{_tmppath}/%{name}-root

%description
This is a standalone PHP extension created using CodeGen_PECL 1.0.0

%prep
%setup -q -c

%build
cd php-mecab-%{version}/mecab/
%{_bindir}/phpize
%configure \
    --with-mecab=%{_bindir}/mecab-config \
    --with-php-config=%{_bindir}/php-config
make

%install
rm -rf %{buildroot}
cd php-mecab-%{version}/mecab/
make install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/mecab.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{php_extdir}/mecab.so
%config(noreplace) %{_sysconfdir}/php.d/mecab.ini

%changelog
* Mon Mar 31 2014 Yoshihiko Nishida <nishida@ngc224.org> - 6-5.el6.centos
- Build for CentOS-6.5
