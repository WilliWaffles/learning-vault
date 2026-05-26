# UI Architecture for MVP v0.1

## UI Architecture Decision

Learning Vault will use a single-window interface.

The main window will update its content depending on the current user flow instead of opening multiple windows.

## Navigation Responsibility

The application will use a single-window interface where views are shown or hidden depending on the current user flow.

`app.py` is responsible for:
- creating the main window
- initializing views
- showing and hiding views
- handling basic navigation between views

Views are responsible for:
- displaying UI content
- capturing user interaction
- notifying `app.py` when navigation is needed

Views should not:
- create other views directly
- manage SQLite logic
- handle full business logic

## Views

### LanguageSelectionView

#### Shows
- Tiles with the available programming languages

#### Handles
- Language selection

#### Should not
- Allow users to add new languages
- Handle authentication or login
- Load database logic directly

---

### CategoryBrowserView

#### Shows
- Left side: category list
- Right side: placeholder message when no category is selected
- Right side: topic cards/list when a category is selected

#### Handles
- Category selection
- Topic selection requests
- Back navigation to LanguageSelectionView

#### Should not
- Add, edit, or delete categories
- Show full topic content
- Modify learning data

---

### TopicDetailView

#### Shows
- Topic details
- Theory sections
- Questions
- Exercises

#### Handles
- Back navigation to CategoryBrowserView

#### Future Responsibilities
- Question attempts
- Exercise progress tracking

#### Should not
- Modify topic, theory, question, or exercise content
- Manage database logic directly