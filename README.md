# kalliope-NordVpn

A simple neuron for Kalliope to use NordVpn


## Synopsis

Make kalliope connect, disconnect and view status for NordVpn  
Nordvpn must be installed on your system [Nordvpn on linux](https://nordvpn.com/fr/download/linux/)

## Installation

  ```
  kalliope install --git-url https://github.com/raspidev/kalliope-nordvpn.git
  ```


## Options

| parameter                  | required | default | choices     | comment                                        |
|----------------------------|----------|---------|-------------|------------------------------------------------|
| param                      | yes      |         |d, c, status | For the action deconnect, connect and status   |


## Synapses example

This synapse will connect, disconnect and viewing the status of NordVpn
```
---

  - name: "nordvpn-connect"
    signals:
      - order: "vpn connect"
    neurons:
      - nordvpn:
          param: "c"
      - say:
          message: "Vous êtes connecté"

  - name: "nordvpn-disconnect"
    signals:
      - order: "vpn déco"
    neurons:
      - nordvpn:
          param: "d"
      - say:
          message: "Vous êtes déconnecté"

  - name: "nordvpn-status"
    signals:
      - order: "vpn status"
    neurons:
      - nordvpn:
          param: "status"


```

* [project on github](https://github.com/raspidev/kalliope-nordvpn)


