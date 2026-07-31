# geosite-blocked

Список популярных зарубежных доменов, независимо от того, заблокированы они в РФ или нет. Представляет собой аналог geolocation-!cn для России и предназначен для безопасной и эффективной маршрутизации на основе FakeIP.

**Обновление каждый понедельник.**

### Источники данных

- https://community.antifilter.download

- https://iplist.opencck.org (все категории)

- https://github.com/1andrevich/Re-filter-lists (community.lst + domains_all.lst с фильтрацией по TLD исключая закрепленные за странами кроме RU и базе GeoLite2-Country.mmdb через резолв оставляя RU код ответа + неудачные операции.)

- https://tranco-list.eu/ (топ 20 тыс доменов через https://pypi.org/project/tranco/ с фильтрацией по TLD исключая RU TLDs и других закрепленных за странами, RU keywords и базе GeoLite2-Country.mmdb через резолв исключая RU код ответа + неудачные операции.)

- Файл с доменами в `data/community.lst` (можно предложить свои.)


### Ссылки на последню актуальную версию для sing-box:

```
https://cdn.jsdelivr.net/gh/jinndi/geosite-blocked@main/geosite-blocked.srs
```

```
https://github.com/jinndi/geosite-blocked/raw/main/geosite-blocked.srs
```

```
https://github.com/jinndi/geosite-blocked/releases/latest/download/geosite-blocked.srs
```
