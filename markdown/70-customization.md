<!-- .slide: data-state="normal" id="customization-1" data-timing="20s" data-menu-title="Standard text slide" -->

## Image Sources

<div class="breadcrumbs">Customization</div>

- Registry: registry.suse.com
- Prometheus & related images from CaaSP
- Eventually we'll be using images from ecosystem team (CAPS)
- Grafana image is maintained by SES team

--

<!-- .slide: data-state="normal" id="customization-2" data-timing="20s" data-menu-title="Standard text slide" -->

## Custom images

<div class="breadcrumbs">Customization</div>

### Options

- container_image_prometheus
- container_image_grafana
- container_image_alertmanager
- container_image_node_exporter

### Usage

```bash
ceph config set mgr mgr/cephadm/<option_name> <value>
```

### Example

```bash
ceph config set mgr mgr/cephadm/container_image_prometheus prom/prometheus:v1.4.1
```

--

<!-- .slide: data-state="normal" id="customization-3" data-timing="20s" data-menu-title="Standard text slide" -->

## Custom Grafana TLS certificate

<div class="breadcrumbs">Customization</div>

### Example

```bash
ceph config-key set mgr/cephadm/grafana_key -i $PWD/key.pem

ceph config-key set mgr/cephadm/grafana_crt -i $PWD/certificate.pem
```

### Update Configuration

```bash
ceph orch redeploy grafana

# `ceph orch reconfig grafana` might eventually work as well
```

--

<!-- .slide: data-state="normal" id="customization-4" data-timing="20s" data-menu-title="Standard text slide" -->

## Prometheus Manager Enhancements

<div class="breadcrumbs">Customization</div>

### Improved cache

- Completely prevents accumulation of requests
- Resolves an issue with the Prometheus MGR

### Performance Logs

- Additional logs about performance

### Performancse Metrics

- Exporting performance metrics of collection time (WIP)

--

<!-- .slide: data-state="normal" id="customization-5" data-timing="20s" data-menu-title="Standard text slide" -->

## Prometheus Manager Module Configuration

<div class="breadcrumbs">Customization</div>

### Server Listening Address and Port

```bash
ceph config set mgr mgr/prometheus/server_addr 0.0.0.0

ceph config set mgr mgr/prometheus/server_port 9283
```

### Scrape Interval

```bash
ceph config set mgr mgr/prometheus/scrape_interval 10
```

--

<!-- .slide: data-state="normal" id="customization-6" data-timing="20s" data-menu-title="Standard text slide" -->

## Prometheus Manager Module Configuration

### Cache Configuration

<div class="breadcrumbs">Customization</div>

```bash
ceph config set mgr mgr/prometheus/stale_cache_strategy <return|fail>
```

<div class="fragment">It will be possible to disable the cache as well.</fragment>

--

<!-- .slide: data-state="normal" id="customization-7" data-timing="20s" data-menu-title="Standard text slide" -->

## Outlook

### Configuration Templates

<div class="breadcrumbs">Customization</div>

- Currently, only certain options for configuration exist
- Templates will enable **any** configuration adaptation
  - Migration of configuration files will work the same way
  - Jinja template engine will be used

--

<!-- .slide: data-state="normal" id="customization-8" data-timing="20s" data-menu-title="Standard text slide" -->

## Ninja Template Example - prometheus.yml.j2 #1

<div class="breadcrumbs">Customization</div>

```jinja
# {{ cephadm_managed }}
global:
  scrape_interval: 10s
  evaluation_interval: 10s
rule_files:
  - /etc/prometheus/alerting/*
# Removed Alertmanager configuration from here
scrape_configs:
  - job_name: 'ceph'
    static_configs:
    - targets:
```

--

<!-- .slide: data-state="normal" id="customization-9" data-timing="20s" data-menu-title="Standard text slide" -->

## Ninja Template Example - prometheus.yml.j2 #2

<div class="breadcrumbs">Customization</div>

```jinja
{% for mgr in mgr_scrape_list %}
      - '{{ mgr }}'
{% endfor %}
      labels:
        instance: 'ceph_cluster'
{% if nodes %}
  - job_name: 'node'
    static_configs:
{% for node in nodes %}
    - targets: ['{{ node.url }}']
      labels:
        instance: '{{ node.hostname }}'
{% endfor %}
{% endif %}
```
