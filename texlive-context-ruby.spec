Name:		texlive-context-ruby
Version:	47085
Release:	2
Summary:	Ruby annotations in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-ruby
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-ruby.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-ruby.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/ruby
%doc %{_texmfdistdir}/doc/context/third/ruby

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
