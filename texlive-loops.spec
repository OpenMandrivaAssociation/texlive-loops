# revision 30704
# category Package
# catalog-ctan /macros/latex/contrib/loops
# catalog-date 2013-05-16 16:49:13 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-loops
Version:	1.3
Release:	11
Summary:	General looping macros for use with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/loops
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/loops.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/loops.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides efficient looping macros for processing
both csv (separated-values) and nsv/tsv (non-separated values)
lists. CSV lists which have associated parsers may be processed
with the tools of the package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/loops/loops.sty
%doc %{_texmfdistdir}/doc/latex/loops/README
%doc %{_texmfdistdir}/doc/latex/loops/loops-pokayoke1.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
