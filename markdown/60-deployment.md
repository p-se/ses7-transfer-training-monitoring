<!-- .slide: data-state="normal" id="deployment-1" data-timing="20s" data-menu-title="Standard text slide" -->

## Prerequisites

<div class="breadcrumbs">Deployment</div>

`ceph-salt` Cluster:

- 1x MON instance
- 1x MGR instance

--

<!-- .slide: data-state="normal" id="deployment-2" data-timing="20s" data-menu-title="Standard text slide" -->

## Specification Example

<div class="breadcrumbs">Deployment</div>

`monitoring.yml` example specification:

```yaml
service_type: prometheus
placement:
  hosts:
    - ses-min2
---
service_type: node-exporter
---
service_type: alertmanager
placement:
  hosts:
    - ses-min4
---
service_type: grafana
placement:
  hosts:
    - ses-min3
```

--

## Applying Specification

<!-- .slide: data-state="normal" id="deployment-3" data-timing="20s" data-menu-title="Standard text slide" -->

<div class="breadcrumbs">Deployment</div>

```bash
ceph orch apply -i monitoring.yml
```

<div class="fragment">

## Applying with CLI

```bash
ceph orch apply prometheus ses-min2

ceph orch apply node-exporter

ceph orch apply alertmanager ses-min4

ceph orch apply grafana ses-min3
```

</div>
