# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/commath
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-commath
Version:	0.3
Release:	9
Summary:	Mathematics typesetting support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/commath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commath.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a range of differential, partial differential and
delimiter commands, together with a \fullfunction (function,
with both domain and range, and function operation) and various
reference commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/commath/commath.sty
%doc %{_texmfdistdir}/doc/latex/commath/README
%doc %{_texmfdistdir}/doc/latex/commath/commath.pdf
%doc %{_texmfdistdir}/doc/latex/commath/commath.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 750409
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718108
- texlive-commath
- texlive-commath
- texlive-commath
- texlive-commath

