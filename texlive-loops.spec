%global tl_name loops
%global tl_revision 30704

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	General looping macros for use with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/loops
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/loops.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/loops.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides efficient looping macros for processing both csv
(separated-values) and nsv/tsv (non-separated values) lists. CSV lists
which have associated parsers may be processed with the tools of the
package.

