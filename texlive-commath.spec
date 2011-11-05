# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/commath
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-commath
Version:	0.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a range of differential, partial differential and
delimiter commands, together with a \fullfunction (function,
with both domain and range, and function operation) and various
reference commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/commath/commath.sty
%doc %{_texmfdistdir}/doc/latex/commath/README
%doc %{_texmfdistdir}/doc/latex/commath/commath.pdf
%doc %{_texmfdistdir}/doc/latex/commath/commath.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
