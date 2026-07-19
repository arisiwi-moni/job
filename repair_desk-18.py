# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RepairDesk
class Tag:
    def __init__(self, name):
        self.name = name.lower() if name else ''

    def __repr__(self):
        return f'<Tag {self.name!r}>'


class TicketTag:
    def __init__(self, ticket_id, tag):
        self.ticket_id = int(ticket_id)
        self.tag = Tag(tag)

    def remove(self):
        return self.tag.name


def add_tag_to_ticket(db_path, ticket_id, tag_name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT id FROM tickets WHERE id=?', (int(ticket_id),))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise ValueError(f'Ticket {ticket_id} not found')
    tag_name = tag_name.strip().lower()
    if not tag_name:
        conn.close()
        return 'tag_empty'
    existing = [r[0] for r in cur.execute(
        'SELECT id FROM ticket_tags WHERE ticket_id=?', (int(ticket_id),))].fetchall()
    if any(t == tag_name for t in existing):
        conn.close()
        return f'tag_already_exists:{tag_name}'
    cur.execute('INSERT INTO ticket_tags (ticket_id, tag) VALUES (?, ?)',
                (int(ticket_id), tag_name))
    conn.commit()
    conn.close()
    return f'added:{tag_name}'


def remove_tag_from_ticket(db_path, ticket_id, tag_name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT id FROM tickets WHERE id=?', (int(ticket_id),))
    if not cur.fetchone():
        conn.close()
        raise ValueError(f'Ticket {ticket_id} not found')
    tag_name = tag_name.strip().lower()
    removed = cur.execute(
        'DELETE FROM ticket_tags WHERE ticket_id=? AND tag=?',
        (int(ticket_id), tag_name)).rowcount
    conn.commit()
    conn.close()
    return f'removed:{tag_name}' if removed else 'not_found'


def list_ticket_tags(db_path, ticket_id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT tag FROM ticket_tags WHERE ticket_id=?', (int(ticket_id),))
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return 'none' if not rows else f'{len(rows)} tags: {", ".join(rows)}'


def list_all_tags(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT tag FROM ticket_tags ORDER BY tag')
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return 'none' if not rows else f'{len(rows)} tags: {", ".join(rows)}'


def get_ticket_tag_count(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM ticket_tags')
    count = cur.fetchone()[0]
    conn.close()
    return count if count else 0
