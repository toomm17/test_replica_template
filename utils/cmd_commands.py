

def format_url_for_curl(thread_name: str):
    domain = 'http://ctl-dev.dev.df.sbrf.ru:8080/v1/api/wf/sched/name/{}'
    return domain.format(thread_name)


def start_thread_with_curl(thread_urls: list) -> None:
    for thread_url in thread_urls:
        curl_start = f'curl -{thread_url.flag} {thread_url.method} {thread_url.url}'
        print(curl_start)
        #os.system(f'curl -X POST {thread_url}')
