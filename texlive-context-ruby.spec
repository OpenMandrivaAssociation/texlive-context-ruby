# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-ruby
# catalog-date 2010-01-28 13:16:16 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-ruby
Version:	20100128
Release:	2
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
characters. The module implements the specification for simple
ruby described by the W3C in ConTeXt. The position and layout
of the base text and the ruby text can becontrolled by
parameters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/ruby/t-ruby.tex
%doc %{_texmfdistdir}/doc/context/third/ruby/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100128-2
+ Revision: 750506
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100128-1
+ Revision: 718141
- texlive-context-ruby
- texlive-context-ruby
- texlive-context-ruby
- texlive-context-ruby

