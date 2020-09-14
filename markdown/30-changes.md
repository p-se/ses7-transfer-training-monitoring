<!-- .slide: data-state="normal" id="containers-1" data-timing="20s" data-menu-title="Standard text slide" -->

## Every component is containerized

<div class="breadcrumbs">Containers</div>

<table style="margin: 0">
<tr>
    <td style="border-bottom-width: 0; padding-right: 100px">
        <ul style="font-size: 32px">
            <li>Prometheus</li>
            <li>Prometheus Node Exporter</li>
            <li>Alertmanager</li>
        </ul>
    </td>
    <td style="border-bottom-width: 0">
    <img src="../images/icons/prometheus.png" height="150px" style="margin: 0">
    </td>
</tr>
<tr>
    <td style="border-bottom-width: 0">
        <ul style="font-size: 32px">
            <li>Grafana</li>
        </ul>
    </td>
    <td style="border-bottom-width: 0"><img src="../images/icons/grafana.png" height="150px" style="margin: 0"></td>
</tr>
<tr class="fragment">
    <td style="border-bottom-width: 0; padding-right: 100px">
        <ul style="font-size: 32px">
            <li>SNMP Trap Receiver (WIP)</li>
        </ul>
    </td>
    <td style="border-bottom-width: 0"><img src="../images/icons/suse.svg" height="150px" style="margin: 0; margin-left: -30px"></td>
</tr>
<tr class="fragment">
    <td style="border-bottom-width: 0; padding-right: 100px">
        <ul style="font-size: 32px">
            <li>Rasdaemon Exporter (SES-7 maintenance upgrade)</li>
        </ul>
    </td>
    <td style="border-bottom-width: 0"><img src="../images/icons/question.svg" height="150px" style="margin: 0; margin-left: 0"></td>
</tr>
</table>

--

<!-- .slide: data-state="normal" id="containers-2" data-timing="20s" data-menu-title="Standard text slide" -->

## Port Allocations

<div class="breadcrumbs">Containers</div>

- Prometheus: **9095** (before: 9090)
- Node-Exporter: 9100
- Alert Manager: 9093 9094
- Grafana: 3000
- Prometheus Manager Module: 9283
