Name:		texlive-jumplines
Version:	37553
Release:	1
Summary:	Articles with teasers and continuation later on
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jumplines
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jumplines.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jumplines.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Jumplines is a package for typesetting (newspaper) articles
that show a teaser (some few lines of text/content) and are
continued at a later place, with optional hyperlinking and a
list of articles. It requires lualatex for colour support in
split boxes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jumplines
%doc %{_texmfdistdir}/doc/latex/jumplines

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
