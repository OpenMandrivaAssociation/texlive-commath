Name:		texlive-commath
Version:	15878
Release:	2
Summary:	Mathematics typesetting support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/commath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commath.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
