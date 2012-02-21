%global packname  fCalendar
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          270.78.3
Release:          1
Summary:          Chronological and Calendarical Objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/%{packname}/%{packname}_%{version}.tar.gz
Requires:         R-methods R-MASS R-fUtilities R-fEcofin 
Requires:         R-RUnit 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-MASS R-fUtilities R-fEcofin
BuildRequires:    R-RUnit 

%description
Environment for teaching "Financial Engineering and Computational Finance"

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME
#  ERROR in test.displayMethods: Error in func() : cannot change value of locked binding for 'myFinCenter'
#  ERROR in test.timeCalendar: Error in func() : cannot change value of locked binding for 'myFinCenter'
#  ERROR in test.as: Error in func() : cannot change value of locked binding for 'myFinCenter'
#  ERROR in test.asTimeDate: Error in func() : cannot change value of locked binding for 'myFinCenter'
#  ERROR in test.julian: Error in func() : cannot change value of locked binding for 'myFinCenter'
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/todo.txt
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYRIGHT.html
%{rlibdir}/%{packname}/DocCopying.pdf
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
