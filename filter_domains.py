import socket
import concurrent.futures
import pandas as pd
import geoip2.database

input_csv = 'top_5000.csv'   # Входящая таблица
output_lst = 'data/top_5000.lst'  # Итоговый файл .lst
geoip_db = 'GeoLite2-Country.mmdb'

ru_tlds = ('.ru', '.рф', '.su', 'by', '.xn--p1ai')

# Инициализируем GeoIP ридер
try:
    reader = geoip2.database.Reader(geoip_db)
except Exception as e:
    print(f"Ошибка загрузки базы GeoIP: {e}")
    reader = None

def is_russian(domain):
    domain = str(domain).strip().lower()
    
    # 1. Проверка по доменной зоне
    if domain.endswith(ru_tlds):
        return True
    
    # 2. Проверка по IP (GeoIP)
    if reader:
        try:
            ip = socket.gethostbyname(domain)
            response = reader.country(ip)
            if response.country.iso_code == 'RU':
                return True
        except Exception:
            pass

    return False

def main():
    # Загрузка CSV
    df = pd.read_csv(input_csv)
    domains = df[df.columns[0]].tolist()
    
    print(f"Начало обработки {len(domains)} доменов...")
    
    # Резолвинг в 50 параллельных потоков
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(lambda d: (d, is_russian(d)), domains))
    
    # Формируем итоговый список
    non_ru_domains = [domain for domain, is_ru in results if not is_ru]
    
    # Сохраняем результат в .lst
    with open(output_lst, 'w', encoding='utf-8') as f:
        for d in non_ru_domains:
            f.write(f"{d}\n")
            
    print(f"Готово! Осталось доменов: {len(non_ru_domains)}")

if __name__ == '__main__':
    main()