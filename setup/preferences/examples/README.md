# Personal Preferences

The examples in this folder are for you to copy and edit to your satisfaction. They will not affect
the code in its official GitHub repository: those are controlled by _pyproject.toml_.

The idea is that the code you are working on is readable and editable by _you_. When pushing, the
git hooks will ensure the code is standardized to the _team_ requirements ... and readable to most
developers when running a code review.

## Visual Studio Code Extensions

### Recommended Extensions

- autoDocstring (Nils Werner)
- Black Formatter (Microsoft)
- Canadian English - Code Spell Checker (Street Side Software)
- Container Tools (Microsoft)
- Dev Containers (Microsoft)
- Docker DX (Docker)
- Git History (Don Jayamanne)
- isort (Microsoft)
- Markdown All in One (Yu Zhang)
- markdownlint (David Anson)
- Pylance (Microsoft)
- Pylint (Microsoft)
- Python (Microsoft)
- Python Debugger (Microsoft)
- Python Environments(Microsoft)
- Remote - SSH (Microsoft)
- Remote Explorer (Microsoft)
- Rewrap (stkb)

### Optional Packages

- Vim (vscodevim)

## Visual Studio Code Workspace

Copy _code.code-workspace_ to the root of this repository and edit it to your requirements. Note
that they will not be saved with this repository.

### Spell-Checking

Keep the Code Spelling plugin and the settings in the example _code.code-workspace_.

If you click on _View_ -> _Problems_, you will see linting and spelling problems.

## User Settings

Depending on your platform, your user settings file is located in:

|OS     |Path                                                      |
|-------|----------------------------------------------------------|
|Windows|%APPDATA%\Code\User\settings.json                         |
|macOS  |$HOME/Library/Application\ Support/Code/User/settings.json|
|Linux  |$HOME/.config/Code/User/settings.json                     |

Your settings file has no bearing on the code. You may look at the examples _settings.json_ file
in this directory for inspiration.

## Pylint

My standards for linting are set in _pyproject.toml_. If you wish to override them in Visual Studio
Code:

1. Copy _pylintrc_ into _setup/preferences_ and edit them.
2. Adjust your personal _settings.json_
   1. Hit CMD-Shift-p (on Mac) and select _Preferences: Open User Settings (JSON).
   2. Insert and save:
      ```json
      "pylint.args": ["--rcfile=developer_setup/personal_preferences/pylintrc"]
      ```

The linter will adjust immediately. Nothing under _personal preferences_ other than the examples
will be preserved in the GitHub repository.

## Black

Black is a formatter that performs an AST-safe[^1] formatting to team standards. As with Pylint,
Black uses the _pyproject.toml_ as its configuration. It can be overridden in VS Code and in the
terminal by first copying _developer_setup/personal_preferences/examples/black_ to
_developer_setup/personal_preferences_.

Adjust your personal settings (see [User Settings](#user-settings) above):
```json
{
   ...
   "black-formatter.path": "developer_setup/personal_preferences/black"
   ...
}
```

## Team Standards vs Personal Standards

The pre-commit and pre-push git commands that you inserted when you executed `make setup` will
use _pylint_ to check your work, then _black_ to format it to team standards.

Black will change the code readability, possibly not to your liking. As the team does not have much
interest in your personal workstation, you may readjust the formatting at need. Once you have
pushed your changes, or once you have pulled someone else's changes, just go into Visual Studio
Code, and in the file you wish to edit, hit:

|OS     |Key Combination               |
|-------|------------------------------|
|Windows|SHIFT+Alt+F                   |
|MacOS  |SHIFT+OPTION+F                |
|Linux  |CTRL+SHIFT+I  (I as in India) |

[^1]: Abstract Syntax Tree
