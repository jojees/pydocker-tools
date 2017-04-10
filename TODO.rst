Reqs:
1. with v2 registry
2. wiyh logging into hub.docker with credentials both v1 and v2
3. argument groups for authentication
4. Need https://pyup.io/ for dependency management
5. Travis CI for linux Build
6. CookieCutter
7. Appveyor for windows build
8. Code Coverage: https://coveralls.io/r/jeffknupp/sandman?branch=develop
9. WIKI Page in Github
10. https://sonarqube.com/profiles/?language=py



MAIL IDs:
Danny Philayvanh
Benjamin Weinberger
Michael Boyd


Management Commands:
1. orchestrator
2. Registry
3. launcher 
4. identity
6. aggregator

1 orchestrator
1.1 Helios https://github.com/spotify/helios
1.2 shipper https://github.com/mailgun/shipper
1.3 Consul https://github.com/hashicorp/consul
1.4 coreOS/fleet https://github.com/coreos/fleet
1.5 redHat/geard https://github.com/openshift/geard https://www.openshift.com/blogs/geard-the-intersection-of-paas-docker-and-project-atomic
1.6 Centurion https://github.com/newrelic/centurion
1.7 multi-host Fig http://www.fig.sh/
1.8 adapters Mesos https://github.com/mesosphere/deimos https://issues.apache.org/jira/browse/MESOS-816
1.9 service scheduler apache aurora http://aurora.incubator.apache.org/
1.10 centralized server configuration apache zookeeper http://zookeeper.apache.org/
1.11 QA - Test Kichen https://github.com/portertech/kitchen-docker
2 registry
2.1 docker hub https://hub.docker.com/
2.2 quay.io https://quay.io/
2.3 private repository https://github.com/docker/docker-registry
3 launcher
3.1 docker https://github.com/docker/docker
3.1.1 libcontainer https://github.com/docker/libcontainer
3.1.2 libswarm https://github.com/docker/libswarm
3.1.3 libchan https://github.com/docker/libchan
3.2 distros
3.2.1 CoreOS
3.2.2 Project Atomic / RedHat http://www.projectatomic.io/
3.2.3 boot2docker.iso
3.3 cloud
3.3.1 AWS
3.3.1.1 EC2 http://awstaiwan.blogspot.tw/2014/07/how-to-install-docker-on-aws-ec2-centos.html
3.3.1.2 Elastic Beanstalk http://aws.amazon.com/about-aws/whats-new/2014/04/23/aws-elastic-beanstalk-adds-docker-support/
3.3.2 Google - GCE http://docs.docker.com/installation/google/
3.3.3 Rackspace http://docs.docker.com/installation/rackspace/
3.3.4 Mesosphere
3.3.4.1 http://mesosphere.io/docs/getting-started/data-center-install/
3.3.4.2 http://mesosphere.io/docs/getting-started/cloud-install/
3.3.4.3 http://mesosphere.io/docs/getting-started/playa-install/
3.3.5 Openstack https://github.com/stackforge/nova-docker
4 GUI
4.1 web UI
4.1.1 kdocker-web
4.1.1.1 https://github.com/tsaikd/kdocker-web
4.1.2 Dockland
4.1.2.1 https://github.com/dynport/dockland
4.1.3 Shipyard
4.1.3.1 https://github.com/shipyard/shipyard
4.1.3.1.1 http://shipyard-project.com/
4.1.4 DockerUI
4.1.4.1 https://github.com/crosbymichael/dockerui
4.2 visual builder
4.2.1 gaudi.io
4.2.1.1 http://gaudi.io/builder.html
4.3 cluster manager
4.3.1 cockpit
4.3.1.1 http://www.projectatomic.io/docs/cockpit/
4.3.2 Mesos UI
4.3.3 Marathon UI
5 identity
6 aggregator
7 core technology
7.1 boot
7.1.1 systemd
7.1.1.1 http://developerblog.redhat.com/2014/05/05/running-systemd-within-docker-container/
7.1.1.2 https://coreos.com/docs/launching-containers/launching/getting-started-with-systemd/
7.2 container
7.2.1 lxc
7.2.1.1 https://linuxcontainers.org/
7.2.1.2 https://help.ubuntu.com/lts/serverguide/lxc.html
7.3 file system
7.3.1 aufs
7.3.1.1 http://www.thegeekstuff.com/2013/05/linux-aufs/
7.4 cluster
7.4.1 etcd
7.4.1.1 https://github.com/coreos/etcd
7.4.1.2 intra-cluster/kraft
7.4.2 kubernetes
7.4.2.1 https://github.com/GoogleCloudPlatform/kubernetes
7.5 I/O virtualization
7.5.1 virtio
7.5.1.1 http://www.ibm.com/developerworks/library/l-virtio/
7.6 software-define networking
7.6.1 pipework
7.6.1.1 https://github.com/jpetazzo/pipework
7.7 virtualization API
7.7.1 libvirt
7.7.1.1 http://libvirt.org/
7.8 security seperation
7.8.1 SELinux
7.8.1.1 http://www.projectatomic.io/docs/docker-and-selinux/
7.9 git for OS binaries
7.9.1 OSTree
7.9.1.1 https://wiki.gnome.org/Projects/OSTree
8 docker VM manager
8.1 boot2docker
8.1.1 http://boot2docker.io/
8.2 docker-osx
8.2.1 https://github.com/noplay/docker-osx
9 automation
9.1 testing
9.1.1 kitchen
9.1.1.1 https://github.com/portertech/kitchen-docker
9.1.1.1.1 http://rubygems.org/gems/kitchen-docker
9.2 Ansible
9.2.1 http://www.ansible.com/docker
9.3 Chef
9.3.1 http://www.getchef.com/solutions/docker/
9.3.2 https://github.com/bflad/chef-docker
9.3.3 http://tech.paulcz.net/2013/09/creating-immutable-servers-with-chef-and-docker-dot-io.html
9.3.4 https://docs.docker.com/articles/chef/
9.3.5 cookbook
9.3.5.1 https://github.com/thoward/docker-cookbook
9.4 Puppet
9.4.1 http://puppetlabs.com/blog/building-puppet-based-applications-inside-docker
9.4.2 https://docs.docker.com/articles/puppet/
9.4.3 http://puppetlabs.com/blog/docker-and-puppet-for-application-management
9.4.4 https://forge.puppetlabs.com/garethr/docker
9.5 Vagrant
9.5.1 https://docs.vagrantup.com/v2/docker/basics.html
10 mini-PaaS
10.1 paramax
10.1.1 https://github.com/CenturyLinkLabs/panamax-ui/wiki
10.1.1.1 http://panamax.io/
10.2 dotCloud / cloudControl
10.2.1 https://www.dotcloud.com/
10.3 Orchard
10.3.1 https://www.orchardup.com/
10.4 Tutum
10.4.1 https://www.tutum.co/
10.5 Dies
10.5.1 https://github.com/deis/deis/
10.5.1.1 http://deis.io/
10.6 Flynn
10.6.1 https://github.com/flynn/flynn
10.6.1.1 https://flynn.io/
10.7 Dokku
10.7.1 https://github.com/progrium/dokku
10.8 Tsuru
10.8.1 http://www.tsuru.io/
10.8.1.1 https://github.com/tsuru/tsuru
10.9 Dawn
10.9.1 https://github.com/dawn/dawn
10.10 Octohost
10.10.1 https://github.com/octohost
10.10.1.1 http://html.octohost.io/
10.10.1.1.1 http://www.octohost.io/