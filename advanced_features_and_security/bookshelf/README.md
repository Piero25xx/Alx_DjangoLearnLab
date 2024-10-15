## Django Groups and Permissions Setup

### Custom Permissions
The following custom permissions have been added to the `Book` model in `bookshelf/models.py`:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

### Groups Setup
The following groups have been created in the Django admin:
- **Viewers**: Can view books.
- **Editors**: Can create and edit books.
- **Admins**: Can view, create, edit, and delete books.

### Enforcing Permissions
Views in `bookshelf/views.py` are protected using the `@permission_required` decorator to ensure that only users with the appropriate permissions can access specific actions.

### Testing
To test the permissions, create test users, assign them to different groups, and verify access to different parts of the application.
