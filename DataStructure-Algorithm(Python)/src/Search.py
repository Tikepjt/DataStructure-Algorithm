def search(name):
    search_queue = deque()
    search_queue + graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
