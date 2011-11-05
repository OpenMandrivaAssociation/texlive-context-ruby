# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-ruby
# catalog-date 2010-01-28 13:16:16 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-ruby
Version:	20100128
Release:	1
Summary:	Ruby annotations in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-ruby
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-ruby.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-ruby.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Conflicts:	texlive-texmf <= 20110705-3

%description
Ruby markup (aka furigana in Japan) are inline annotations
above or below a word to indicate the reading of ideographic
characters. The module implements the specification for simple
ruby described by the W3C in ConTeXt. The position and layout
of the base text and the ruby text can becontrolled by
parameters.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/ruby/t-ruby.tex
%doc %{_texmfdistdir}/doc/context/third/ruby/README
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
