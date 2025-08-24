#
# Conditional build:
%bcond_with	jack1	# JACK 1 (0.126+) instead of JACK 2
%bcond_without	zalsa	# zita-a2j/j2a client

Summary:	JACK example tools
Summary(pl.UTF-8):	Przykładowe narzędzia do JACK-a
Name:		jack-example-tools
Version:	4
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/jackaudio/jack-example-tools/releases
Source0:	https://github.com/jackaudio/jack-example-tools/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	282f4c913489b32edc9926c8f84a73ae
URL:		https://github.com/jackaudio/jack-example-tools
BuildRequires:	alsa-lib-devel >= 1.0.18
# also pipewire jack >= 0.3.44 possible
%if %{with jack1}
BuildRequires:	jack-audio-connection-kit-devel >= 0.126.0
%else
BuildRequires:	jack-audio-connection-kit-devel >= 1.9.20
%endif
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	opus-devel >= 0.9.0
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 2.042
%if %{with zalsa}
BuildRequires:	zita-alsa-pcmi-devel
BuildRequires:	zita-resampler-devel
%endif
Requires:	alsa-lib >= 1.0.18
%if %{with jack1}
Requires:	jack-audio-connection-kit >= 0.126.0
%else
Requires:	jack-audio-connection-kit >= 1.9.20
%endif
Requires:	opus-devel >= 0.9.0
Conflicts:	jack-audio-connection-kit-example-clients < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The official JACK example clients and tools.

%description -l pl.UTF-8
Oficjalne przykładowe narzędzia i programy klienckie do systemu
dźwięku JACK.

%package -n jack-example-clients
Summary:	Example clients that use JACK
Summary(pl.UTF-8):	Przykładowe programy klienckie używające JACK-a
License:	GPL v2+
Group:		Applications/Sound
%if %{with jack1}
Requires:	jack-audio-connection-kit >= 0.126.0
%else
Requires:	jack-audio-connection-kit >= 1.9.20
%endif
Requires:	libsndfile >= 1.0.0
Obsoletes:	jack-audio-connection-kit-example-clients < 2
Obsoletes:	jack-audio-connection-kit-example-jackrec < 2

%description -n jack-example-clients
Small example clients that use the JACK Audio Connection Kit.

%description -n jack-example-clients -l pl.UTF-8
Małe, przykładowe programy klienckie, które używają zestawu do
połączeń audio JACK.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	%{!?with_zalsa:-Dzalsa=disable}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/alsa_in
%attr(755,root,root) %{_bindir}/alsa_out
%attr(755,root,root) %{_bindir}/jack_alias
%attr(755,root,root) %{_bindir}/jack_bufsize
%attr(755,root,root) %{_bindir}/jack_connect
%attr(755,root,root) %{_bindir}/jack_disconnect
%attr(755,root,root) %{_bindir}/jack_evmon
%attr(755,root,root) %{_bindir}/jack_freewheel
%attr(755,root,root) %{_bindir}/jack_iodelay
%attr(755,root,root) %{_bindir}/jack_load
%attr(755,root,root) %{_bindir}/jack_load_test
%attr(755,root,root) %{_bindir}/jack_lsp
%attr(755,root,root) %{_bindir}/jack_midi_dump
%attr(755,root,root) %{_bindir}/jack_monitor_client
%attr(755,root,root) %{_bindir}/jack_netsource
%attr(755,root,root) %{_bindir}/jack_property
%attr(755,root,root) %{_bindir}/jack_samplerate
%attr(755,root,root) %{_bindir}/jack_transport
%attr(755,root,root) %{_bindir}/jack_tw
%attr(755,root,root) %{_bindir}/jack_unload
%attr(755,root,root) %{_bindir}/jack_wait
%if %{with zalsa}
%attr(755,root,root) %{_libdir}/jack/zalsa_in.so
%attr(755,root,root) %{_libdir}/jack/zalsa_out.so
%endif
%{_mandir}/man1/alsa_in.1*
%{_mandir}/man1/alsa_out.1*
%{_mandir}/man1/jack_bufsize.1*
%{_mandir}/man1/jack_connect.1*
%{_mandir}/man1/jack_disconnect.1*
%{_mandir}/man1/jack_freewheel.1*
%{_mandir}/man1/jack_iodelay.1*
%{_mandir}/man1/jack_load.1*
%{_mandir}/man1/jack_lsp.1*
%{_mandir}/man1/jack_monitor_client.1*
%{_mandir}/man1/jack_netsource.1*
%{_mandir}/man1/jack_property.1*
%{_mandir}/man1/jack_samplerate.1*
%{_mandir}/man1/jack_transport.1*
%{_mandir}/man1/jack_unload.1*
%{_mandir}/man1/jack_wait.1*

%files -n jack-example-clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack_control_client
%attr(755,root,root) %{_bindir}/jack_cpu_load
%attr(755,root,root) %{_bindir}/jack_impulse_grabber
%attr(755,root,root) %{_bindir}/jack_latent_client
%attr(755,root,root) %{_bindir}/jack_metro
%attr(755,root,root) %{_bindir}/jack_midi_latency_test
%attr(755,root,root) %{_bindir}/jack_midiseq
%attr(755,root,root) %{_bindir}/jack_midisine
%attr(755,root,root) %{_bindir}/jack_net_master
%attr(755,root,root) %{_bindir}/jack_net_slave
%attr(755,root,root) %{_bindir}/jack_rec
%attr(755,root,root) %{_bindir}/jack_server_control
%attr(755,root,root) %{_bindir}/jack_showtime
%attr(755,root,root) %{_bindir}/jack_simdtests
%attr(755,root,root) %{_bindir}/jack_simple_client
%attr(755,root,root) %{_bindir}/jack_thru_client
%attr(755,root,root) %{_bindir}/jack_transport_client
%attr(755,root,root) %{_bindir}/jack_zombie
%attr(755,root,root) %{_libdir}/jack/jack_inprocess.so
%attr(755,root,root) %{_libdir}/jack/jack_internal_metro.so
%attr(755,root,root) %{_libdir}/jack/jack_intime.so
%{_mandir}/man1/jack_impulse_grabber.1*
%{_mandir}/man1/jack_metro.1*
%{_mandir}/man1/jack_rec.1*
%{_mandir}/man1/jack_showtime.1*
%{_mandir}/man1/jack_simple_client.1*
