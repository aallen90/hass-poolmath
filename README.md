# Pool Math for Home Assistant

![release_badge](https://img.shields.io/github/release/rsnodgrass/hass-poolmath.svg)
![release_date](https://img.shields.io/github/release-date/rsnodgrass/hass-poolmath.svg)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Buy Me A Coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg)](https://buymeacoffee.com/DYks67r)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=WREP29UDAMB6G)
[![Support on Patreon][patreon-shield]][patreon]

[![Community Forum][forum-shield]][forum]

Creates sensors for pools being managed with Trouble Free Pools's [Pool Math](https://www.troublefreepool.com/blog/poolmath/) apps ([iOS](https://apps.apple.com/us/app/pool-math-by-troublefreepool/id1228819359)/[Android](https://play.google.com/store/apps/details?id=com.troublefreepool.poolmath&hl=en_US)/[Fire](https://www.amazon.com/gp/product/B07F87V4SX/ref=mas_pm_Pool_Math)). Use a device like [Pool Exact EZ Pool Water Tester](https://amzn.to/4kqjHxI) to measure exact values and enter the data into Pool Math, and your pool, spa, or hot tub data will automatically appear in Home Assistant.

[Pool Math](https://www.troublefreepool.com/blog/poolmath/) makes swimming pool care, maintenance and management easy by tracking chlorine, pH, alkalinity and other levels to help calculate how much salt, bleach and other chemicals to add. Note: this **requires a [Trouble Free Pool](https://www.troublefreepool.com/) Pool Math Premium subscription** to access your pool or spa's data from the Pool Math service.

#### Supported Pool Math Values

* pH
* Free Chlorine (FC)
* Combined Chlorine (CC)
* Total Chlorine (TC)
* Total Alkalinity (TA)
* Calcium Hardness (CH)
* Cyanuric Acid (CYA)
* Salt
* Borates
* Calcite Saturation Index (CSI)
* Temperature
* Pressure
* Flow Rate
* SWG Cell Percentage



## Support

### Community Support

* **For support, use the [official Home Assistant Pool Math discussion thread](https://community.home-assistant.io/t/custom-component-pool-math-sensors-for-pool-chemicals-and-operations/435126). The developers are just volunteers from the community and do not provide any support, so it is best to ask the entire community for help or questions. There is no support or dedicated development for this integration, thus GitHub issue tracking has been turned off. Please submit Pull Requests with bug fixes!**

* [How to use the Pool Math app?](https://www.troublefreepool.com/threads/how-to-use-the-pool-math-app.179282/)

* For issues with the Pool Math apps, see forums or contact [poolmath@troublefreepool.com](mailto:poolmath@troublefreepool.com)

## Installation

Make sure [Home Assistant Community Store (HACS)](https://github.com/custom-components/hacs) is installed, then add the repository: `rsnodgrass/hass-poolmath`

### Configuration

1. Under Settings in the Pool Math app (iOS/Android/Fire), find the Sharing section: turn this on and **save changes**. Your pool's share URL will be displayed, which you'll need for setting up this integration. Anyone with the share URL will be able to view data about your pool.

2. Configure the `Pool Math (Trouble Free Pool)` integration via Home Assistant integrations page, or press the blue button below:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=poolmath)

3. Enter your pool's share URL when asked during the configuration of the Pool Math integration. Multiple pools and hot tubs can be configured by adding additional integrations.

NOTE: To protect the PoolMath service this integration only updates values **every 8 minutes** since PoolMath's cloud service caches data for 10 minutes AND rate limits to no more than once per minute.

### Example Lovelace UI

```yaml
entities:
  - entity: sensor.pool_fc
    name: Free Chlorine
  - entity: sensor.pool_ph
    name: pH
  - entity: sensor.pool_ta
    name: Total Alkalinity
  - entity: sensor.pool_cya
    name: CYA
  - entity: sensor.pool_ch
    name: Hardness
type: entities
title: Pool
show_header_toggle: false
```

![Lovelace Example](https://github.com/rsnodgrass/hass-poolmath/blob/master/img/example.png?raw=true)

Another single line Lovelace example using multiple-entity-row:

```yaml
entities:
  - entity: sensor.pool_ph
    type: 'custom:multiple-entity-row'
    name: Pool
    state_header: pH
    secondary_info: last-changed
    entities:
      - entity: sensor.pool_fc
        name: FC
      - entity: sensor.pool_cc
        name: CC
      - entity: sensor.pool_ta
        name: TA
  - entity: sensor.hot_tub_ph
    type: 'custom:multiple-entity-row'
    name: Hot Tub
    state_header: pH
    secondary_info: last-changed
    entities:
      - entity: sensor.hot_tub_fc
        name: FC
      - entity: sensor.hot_tub_cc
        name: CC
      - entity: sensor.hot_tub_ta
        name: TA
type: entities
```

![Lovelace Example](https://github.com/rsnodgrass/hass-poolmath/blob/master/img/example-multiple.png?raw=true)


## Future Plans

### Feature Requests

* move all communication/interfaces to Pool Math into separate `pypoolmath` package that can be maintained separately
* add [@berniedp's calculation to suggest SWG % setting](https://community.home-assistant.io/t/custom-component-pool-math-sensors-for-pool-chemicals-and-operations/435126/12?u=ryans) See [https://community.home-assistant.io/t/custom-component-pool-math-sensors-for-pool-chemicals-and-operations/435126/17](calculations here).

### Developer Testing

Quick cheat sheet for developers testing changes on their own instance of Home Assistant:

```console
scp -r custom_components/poolmath homeassistant.local:/config/custom_components
ssh homeassistant.local "rm /config/*.log ; ha core restart"
```

## See Also

* [Trouble Free Pool Pool Math online calculator](https://www.troublefreepool.com/calc.html)
* [Pool Math apps](https://www.troublefreepool.com/blog/poolmath/) ([iOS](https://apps.apple.com/us/app/pool-math-by-troublefreepool/id1228819359), [Android](https://play.google.com/store/apps/details?id=com.troublefreepool.poolmath&hl=en_US))
* [ABC's of Pool Water Chemistry by Trouble Free Pool](https://www.troublefreepool.com/blog/2018/12/12/abcs-of-pool-water-chemistry/)
* [PookMath calculator](https://www.troublefreepool.com/calc.html)

### Pool Monitoring Tools

* [Pool Exact EZ Photometer Entry Digital Pool Water Test Ki](https://amzn.to/4kqjHxI)
* [Pentair EC-523317 IntelliConnect Pool Control and Monitoring System](https://amzn.to/3S9GJN5)
* [Sutro Pool & Spa Water Smart Monitoring Device](https://amzn.to/4kovpss)
* [PoolLab 1.0 Pool Chemical Tester with Bluetooth](https://amzn.to/4mmr6jg)


[forum]: https://community.home-assistant.io/t/custom-component-pool-math-sensors-for-pool-chemicals-and-operations/435126
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[patreon]: https://www.patreon.com/rsnodgrass
[patreon-shield]: https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
