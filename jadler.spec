Name:          jadler
Version:       1.3.0
Release:       1%{?dist}
Summary:       Jadler is a Java library for stubbing and mocking HTTP servers and resources in a declarative way. 
License:       MIT
URL:           https://github.com/jadler-mocking/jadler/wiki
Source0:       https://github.com/jadler-mocking/jadler/archive/%{name}-pom-%{version}.zip

BuildRequires: maven-local
BuildRequires: mvn(org.springframework:spring-test)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.eclipse.jetty.orbit:javax.servlet)
BuildRequires: mvn(org.eclipse.jetty:jetty-io)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-io:commons-io)

BuildArch:     noarch

%description
Jadler is a Java library for stubbing and mocking HTTP servers and resources in a declarative way. 

%package %{name}-junit
Summary:       JUnit specific Jadler extension

%description %{name}-junit
This package contains JUnit specific Jadler extension.


%package %{name}-jdk
Summary:       An alternative implementation of the stub http server component using the com.sun.net.httpserver.HttpServer

%description %{name}-jdk
This package contains an alternative implementation of the stub http server component using the com.sun.net.httpserver.HttpServer component which is bundled with major Java implementations.


%package %{name}-core
Summary:       Core of the Jadler library

%description %{name}-core
This package contains the core of the Jadler library.


%package %{name}-jetty
Summary:       An implementation of the stub http server component using Jetty

%description %{name}-jetty
This package contains an implementation of the stub http server component using Jetty.


%package %{name}-all
Summary:       All jadler sub-modules

%description %{name}-all
This package contains all jadler sub-modules. By including jadler-all to a project a complete Jadler library will be included automatically.


%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -n %{name}-%{name}-pom-%{version}
%mvn_config buildSettings/compilerSource 1.8
#%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin' ]/pom:version" 2.5.1 .
#%pom_remove_plugin -r :maven-checkstyle-plugin
#%pom_disable_module  ../core/azure-core-test azure
#%pom_change_dep -r com.sun.jersey: ::1

# org.jvnet.jaxb2.maven2:maven-jaxb2-plugin:0.9.1
#%pom_xpath_set "pom:plugin[pom:groupId = 'org.jvnet.jaxb2.maven2' ]/pom:artifactId" maven-jaxb22-plugin services/azure-servicebus

#%mvn_package ":azure-keyvault*" keyvault
#%mvn_package ":azure-mgmt-compute" resource-management
#%mvn_package ":azure-mgmt-dns" resource-management
#%mvn_package ":azure-mgmt-network" resource-management
#%mvn_package ":azure-mgmt-notificationhubs" resource-management
#%mvn_package ":azure-mgmt-resources" resource-management
#%mvn_package ":azure-mgmt-sql" resource-management
#%mvn_package ":azure-mgmt-storage" resource-management
#%mvn_package ":azure-mgmt-traffic-manager" resource-management
#%mvn_package ":azure-mgmt-utility" resource-management
#%mvn_package ":azure-mgmt-websites" resource-management
#%mvn_package ":azure-svc-*" service-management

%build
%mvn_build -s

%install
%mvn_install

%files %{name}-all -f .mfiles-%{name}-all
%doc RELEASENOTES.md
%license LICENSE

%files %{name}-core -f .mfiles-%{name}-core
%doc RELEASENOTES.md
%license LICENSE

%files %{name}-jdk -f .mfiles-%{name}-jdk
%doc RELEASENOTES.md
%license LICENSE

%files %{name}-jetty -f .mfiles-%{name}-jetty
%doc RELEASENOTES.md
%license LICENSE

%files %{name}-junit -f .mfiles-%{name}-junit
%doc RELEASENOTES.md
%license LICENSE


%changelog
* Sun Nov 6 2016 Michal Karm Babacek <karm@fedoraproject.org> 1.3.0-1
- initial rpm


