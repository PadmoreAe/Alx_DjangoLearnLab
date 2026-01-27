# Project Instructions

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git


# Permissions and Groups Setup

### Custom Permissions
Custom permissions defined in the `Book` model:
- `can_view`: Allows users to view the book list and details.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify existing books.
- `can_delete`: Allows users to remove books from the database.

### Groups
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Full permissions (view, create, edit, delete).