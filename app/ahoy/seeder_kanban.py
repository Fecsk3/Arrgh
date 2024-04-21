import sqlite3

def seed_boards(cursor, board_name):
    try:
        cursor.execute("SELECT id FROM kanban_board WHERE board_name=?", (board_name,))
        board = cursor.fetchone()
        if not board:
            cursor.execute("INSERT INTO kanban_board (board_name) VALUES (?)", (board_name,))
            print(f"Board '{board_name}' seeded successfully.")
            return cursor.lastrowid
        else:
            print(f"Board '{board_name}' already exists.")
            return board[0]
    except sqlite3.Error as e:
        print(f'Error occurred while seeding board: {e}')
        return None

def seed_titles(cursor, board_id, title_data):
    try:
        for title_info in title_data:
            title_name = title_info['title_name']
            cursor.execute("SELECT id FROM kanban_title WHERE title_name=? AND board_id=?", (title_name, board_id))
            title = cursor.fetchone()
            if not title:
                cursor.execute("INSERT INTO kanban_title (title_name, board_id) VALUES (?, ?)", (title_name, board_id))
                print(f"Title '{title_name}' seeded successfully under Board ID '{board_id}'.")
                title_id = cursor.lastrowid
                seed_tasks(cursor, title_id, title_info.get('tasks', []))
            else:
                print(f"Title '{title_name}' already exists under Board ID '{board_id}'.")
    except sqlite3.Error as e:
        print(f'Error occurred while seeding titles: {e}')

def seed_tasks(cursor, title_id, task_data):
    try:
        for task_info in task_data:
            task_name = task_info['task_name']
            description = task_info['description']
            cursor.execute("SELECT id FROM kanban_task WHERE task_name=? AND title_id=?", (task_name, title_id))
            task = cursor.fetchone()
            if not task:
                cursor.execute("INSERT INTO kanban_task (task_name, description, title_id) VALUES (?, ?, ?)", (task_name, description, title_id))
                print(f"Task '{task_name}' seeded successfully under Title ID '{title_id}'.")
            else:
                print(f"Task '{task_name}' already exists under Title ID '{title_id}'.")
    except sqlite3.Error as e:
        print(f'Error occurred while seeding tasks: {e}')

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

board_data = {
    'board_name': 'Kanban',
    'titles': [
        {
            'title_name': 'Teendő',
            'tasks': [
                {'task_name': 'Task 1.1', 'description': 'Description for Task 1.1'},
                {'task_name': 'Task 1.2', 'description': 'Description for Task 1.2'},
                {'task_name': 'Task 1.3', 'description': 'Description for Task 1.3'},
            ]
        },
        {
            'title_name': 'Folyamatban',
            'tasks': [
                {'task_name': 'Task 2.2', 'description': 'Description for Task 2.2'},
                {'task_name': 'Task 2.3', 'description': 'Description for Task 2.3'},
                {'task_name': 'Task 2.1', 'description': 'Description for Task 2.1'},
            ]
        },
        {
            'title_name': 'Ellenőrzés',
            'tasks': [
                {'task_name': 'Task 3.1', 'description': 'Description for Task 3.1'},
                {'task_name': 'Task 3.2', 'description': 'Description for Task 3.2'},
                {'task_name': 'Task 3.3', 'description': 'Description for Task 3.3'},
            ]
        },
        {
            'title_name': 'Teszt',
            'tasks': [
                {'task_name': 'Task 4.1', 'description': 'Description for Task 4.1'},
                {'task_name': 'Task 4.2', 'description': 'Description for Task 4.2'},
                {'task_name': 'Task 4.3', 'description': 'Description for Task 4.3'},
            ]
        },
        {
            'title_name': 'Kész',
            'tasks': [
                {'task_name': 'Task 5.1', 'description': 'Description for Task 5.1'},
                {'task_name': 'Task 5.2', 'description': 'Description for Task 5.2'},
                {'task_name': 'Task 5.3', 'description': 'Description for Task 5.3'},
            ]
        }
    ]
}

try:
    # Seed boards
    board_id = seed_boards(cursor, board_data['board_name'])

    # Seed titles and tasks
    seed_titles(cursor, board_id, board_data['titles'])

    # Commit the transaction
    conn.commit()
    print('Data seeding completed successfully.')

except sqlite3.Error as e:
    print(f'Error occurred during data seeding: {e}')
    conn.rollback()

finally:
    # Close the connection
    conn.close()
