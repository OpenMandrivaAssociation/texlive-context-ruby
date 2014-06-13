# revision 28434
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-ruby
# catalog-date 2012-11-30 11:03:17 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-ruby
Version:	20121130
Release:	6
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

%description
Ruby markup (aka furigana in Japan) are inline annotations
above or below a word to indicate the reading of ideographic
characters. The module implements the W3C specification for
simple ruby in ConTeXt. The position and layout of the base
text and the ruby text can becontrolled by parameters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/ruby/t-ruby.mkii
%{_texmfdistdir}/tex/context/third/ruby/t-ruby.mkiv
%{_texmfdistdir}/tex/context/third/ruby/t-ruby.mkvi
%doc %{_texmfdistdir}/doc/context/third/ruby/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
