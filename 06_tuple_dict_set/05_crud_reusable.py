def generate_id(items):
    return max(item["id"] for item in items) + 1


def find_item(item_id, items):
    for item in items:
        if item_id == item["id"]:
            return item


def update_item(item_id, payload, items):
    item = find_item(item_id, items)
    if item:
        item.update(payload)
        return item


def create_item(payload, items):
    items.append({"id": generate_id(), **payload})
    return items[-1]


def remove_item(item_id, items):
    item = find_item(item_id, items)
    items.remove(item)
