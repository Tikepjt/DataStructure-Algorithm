cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]  # 캐싱된 자료들 전송
    else:
        data = get_data_from_server(url)
        cache[url] = data  # 캐시에 처음으로 자료를 저장
        return data
