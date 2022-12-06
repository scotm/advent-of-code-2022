def chunk(this_list, chunk_size):
    for i in range(0, len(this_list), chunk_size):
        yield this_list[i:i + chunk_size]