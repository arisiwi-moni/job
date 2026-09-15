# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RepairDesk
def paginate(items, page_size=10):
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages

def get_page(pages, page_num):
    if 1 <= page_num <= len(pages):
        return pages[page_num - 1]
    return []

def get_page_count(pages):
    return len(pages) if pages else 0
