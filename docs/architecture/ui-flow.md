# UI Flow for MVP v0.1
1. App opens
2. Shows language tiles
3. User clicks Python
4. App shows a two-column layout:
   - left: categories
   - right: placeholder message
5. User clicks category
6. Right side shows topic cards for that category
   - title
   - short description
   - theory sections count
   - questions count
   - exercises count
7. User clicks topic
8. Right side shows topic detail
   - description
   - theory sections
   - questions
   - exercises

Example:
[ Loops ]
Repeat actions using for and while loops.
Theory: 4 | Questions: 6 | Exercises: 3

# UI Architecture Decision

Learning Vault will use a single-window interface.

The main window will update its content depending on the current user flow instead of opening multiple windows.

```text
Main Window
 └── Main Content Area
      ├── Language Selection View
      ├── Category Browser View
      ├── Topic Detail View
      └── Future views
```

# Future Improvements

- animated transitions
- slide menu
- category icons
- progress indicators
- locked/soon tiles
- prettier dashboard

