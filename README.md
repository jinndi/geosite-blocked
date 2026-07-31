# geosite-blocked

Список популярных зарубежных доменов, независимо от того, заблокированы они в РФ или нет. Представляет собой аналог geolocation-!cn для России и предназначен для безопасной и эффективной маршрутизации на основе FakeIP.

**Обновление каждый понедельник.**

### Источники данных

- https://community.antifilter.download

- https://iplist.opencck.org (все категории)

- https://github.com/1andrevich/Re-filter-lists (community.lst и domains_all.lst **с фильтрацией**.)

* **Логика фильтрации:**
  * **Фильтрация по TLD:** Исключаются национальные доменные зоны (ccTLD), закрепленные за другими странами, **кроме зоны RU** (`.ru`, `.su`, `.рф` и т.д.).
  * **Проверка через DNS & GeoIP (`GeoLite2-Country.mmdb`):**
    * **Исключаем:** домены, которые не резолвятся (ошибки DNS, `NXDOMAIN`, таймауты).
    * **Оставляем:** домены, которые резолвятся в IP-адреса с кодом страны **`RU`**, а также случаи, когда GeoIP не смог определить код страны.
    * **Исключаем:** домены, резолв которых явно вернул код страны, отличный от `RU`.

- https://tranco-list.eu/ (топ 50 тыс доменов через https://pypi.org/project/tranco/ **с фильтрацией**)

* **Логика фильтрации:**
  * **Фильтрация по TLD:** Исключаются доменные зоны RU (`.ru`, `.su`, `.рф` и т.д.) и все остальные национальные доменные зоны (ccTLD).
  * **Фильтрация по ключевым словам:** Исключаются российские сервисы и ключевые слова (*yandex, vkontakte, sber, ozon, avito* и др.).
  * **Проверка через DNS & GeoIP (`GeoLite2-Country.mmdb`):**
    * **Исключаем:** домены, резолв которых вернул IP-адрес с кодом страны **`RU`**.
    * **Оставляем:** домены с неудачными операциями (ошибки DNS, `NXDOMAIN`, таймауты).

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
