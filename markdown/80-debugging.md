<!-- .slide: data-state="normal" id="debugging-1" data-timing="20s" data-menu-title="Standard text slide" -->

## ceph orch ls

<div class="breadcrumbs">Debugging</div>

```bash
➜  ~ ceph orch ls
NAME           RUNNING  REFRESHED  AGE  PLACEMENT  IMAGE NAME                                                                                          IMAGE ID
alertmanager       1/1  26s ago    39s  count:1    docker.io/prom/alertmanager:v0.20.0                                                                 0881eb8f169f
crash              1/1  26s ago    4m   *          docker.io/ceph/daemon-base@sha256:07ef69780ba84b248a0a500a919008b599d4176a820debdc9afe714fb51a3545  57df290c0cce
grafana            1/1  26s ago    2m   count:1    docker.io/ceph/ceph-grafana:6.6.2                                                                   a0dce381714a
node-exporter      1/1  26s ago    2m   *          docker.io/prom/node-exporter:v0.18.1                                                                e5a616e4b9cf
prometheus         1/1  26s ago    2m   count:1    docker.io/prom/prometheus:v2.18.1                                                                   de242295e225
➜  ~
```

--

<!-- .slide: data-state="normal" id="debugging-2" data-timing="20s" data-menu-title="Standard text slide" -->

## Logs

<div class="breadcrumbs">Debugging</div>

### Usage

```bash
cephadm logs --fsid <fsid> --name <name-of-daemon>
```

### Example

```bash
➜  ~ sudo cephadm logs --fsid $(ceph fsid) --name node-exporter.home | head
-- Logs begin at Sat 2020-09-05 19:41:07 CEST, end at Mon 2020-09-14 15:50:24 CEST. --
Sep 14 14:41:06 home systemd[1]: Starting Ceph node-exporter.home for 836f9c83-b8f6-4bc7-9d0c-2a59eefeff41...
Sep 14 14:41:06 home podman[1356353]: Error: no container with name or ID ceph-836f9c83-b8f6-4bc7-9d0c-2a59eefeff41-node-exporter.home found: no such container
Sep 14 14:41:06 home bash[1356397]: Error: Failed to evict container: "": Failed to find container "ceph-836f9c83-b8f6-4bc7-9d0c-2a59eefeff41-node-exporter.home" in state: no container with name or ID ceph-836f9c83-b8f6-4bc7-9d0c-2a59eefeff41-node-exporter.home found: no such container
Sep 14 14:41:06 home bash[1356437]: Error: no container with ID or name "ceph-836f9c83-b8f6-4bc7-9d0c-2a59eefeff41-node-exporter.home" found: no such container
Sep 14 14:41:06 home bash[1356478]: Trying to pull docker.io/prom/node-exporter:v0.18.1...
Sep 14 14:41:09 home bash[1356478]: Getting image source signatures
Sep 14 14:41:09 home bash[1356478]: Copying blob sha256:49a2d53aa1af115e87f7e23a7fe4b7a3e12304d37982fb6528b035d0f68a3b56
Sep 14 14:41:09 home bash[1356478]: Copying blob sha256:190160031744b0810999dd6f293478be0b41524654c70782cf09437095430f2f
Sep 14 14:41:09 home bash[1356478]: Copying blob sha256:3589a6efd9ce96b2f2218a80bacb84f60d5e584d024023617b0f56b87fe798c3
➜  ~
```
