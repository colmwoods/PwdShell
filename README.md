# [PwdShell](https://pwdshell-6bf799458b95.herokuapp.com)

Developer: Colm Woods ([colmwoods](https://www.github.com/colmwoods))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/colmwoods/PwdShell)](https://www.github.com/colmwoods/PwdShell/commits/main)  
[![GitHub last commit](https://img.shields.io/github/last-commit/colmwoods/PwdShell)](https://www.github.com/colmwoods/PwdShell/commits/main)  
[![GitHub repo size](https://img.shields.io/github/repo-size/colmwoods/PwdShell)](https://www.github.com/colmwoods/PwdShell)  
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://pwdshell-6bf799458b95.herokuapp.com)

---
![Mockups](docs/img/mockup.jpg)  

Source: [Techsini Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/?url=https://pwdshell-6bf799458b95.herokuapp.com/)  


## Project Introduction and Rationale

PwdShell is a **terminal-based password manager**.  
It allows users to set a **master password** and then store, retrieve, and manage their account credentials securely in a local vault (`vault.json`).

A key design choice was to handle master password storage differently depending on the environment:

#### 🔹 Heroku Deployment
- The master password is **session-only**.  
- It resets each time the dyno restarts or the “Run Program” button is pressed.  
- This ensures every user, including Code Institute assessors, can set their own password without needing the developer’s.  
- **No permanent files** (`master.key` or `vault.json`) are written in the deployed version.  

#### 🔹 Local Environment
- The master password is **persisted** in a `master.key` file, hashed with **SHA-256**.  
- Vault data is stored in `vault.json` and is available across runs.  
- This allows users to manage and retain their passwords securely between sessions.  

> Apart from this difference in password persistence, both versions function identically.
The project is designed for users who:  
- Want a **lightweight password manager** that doesn’t require browser plugins.  
- Prefer to keep their data **local** instead of relying on third-party services.  
- Need a **simple menu-driven tool** for basic password management.  

I chose this project because:  
- Password management is a **real-world problem** that everyone faces.  
- It gave me a chance to explore **hashing, encryption, JSON storage, and Python file handling**.  
- It’s a project I can personally use to manage my own credentials.  

---

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide users with a secure vault for account credentials.  
- Protect access to sensitive data with a master password.  

**Primary User Needs**
- Add new account credentials quickly.  
- Retrieve stored account details.  
- View all accounts in the vault.  
- Delete accounts no longer needed.  

**Business Goals**
- Deliver a simple, functional password manager.  
- Encourage safe password practices by making management easy.  

#### 2. Scope

**Features**
- Master password setup and verification.  
- Add account with username + password.  
- Retrieve account details.  
- View all accounts.  
- Delete accounts.  

#### 3. Structure

**Information Architecture**
- App opens with master password check.  
- Menu-driven interface for all actions.  

**User Flow**
1. User runs app → sets/verifies master password.  
2. Main menu appears.  
3. User chooses to add, view, retrieve, or delete accounts.  
4. Vault updates automatically.  

#### 4. Skeleton

Screenshot of the terminal menu structure that users interact with after logging in, no wireframes only text menu.  
![Skeleton](docs/img/terminal.jpg)  

#### 5. Surface

**Visual Design Elements**
- Minimal text UI.  
- Symbols and dividers used for readability.  

**Colours**
- The terminal app relies on the system terminal’s default colour scheme.  
- In future, the app could use [Colorama](https://pypi.org/project/colorama/) to add colour-coded menus and alerts.  

**Typography**
- The app uses the system’s default **monospaced font** (e.g., Consolas, Courier New, or Menlo depending on OS).  
- This ensures consistent character alignment in the terminal.

---

## Wireframes

“Instead of GUI wireframes, the terminal menu structure acts as the skeleton design. See screenshot below.”
![Wireframes](docs/img/terminal.jpg)

---

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a user | I want to set a master password | so that my vault is secure. |
| As a user | I want to add account details | so I can store them safely. |
| As a user | I want to view a list of accounts | so I know what I have stored. |
| As a user | I want to retrieve login details | so I can log in to accounts. |
| As a user | I want to delete accounts | so I can remove ones I no longer use. |

---

## Features

### Existing Features

> [!NOTE]
> You cannot see the **password** on the screen as i'm using the getpass method whichs hides the password from being seen

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Master Password | Vault is protected with a SHA256 hash of the master password. |![Master Password](docs/img/features/master-password.jpg)    |
| Add Account | Add username + password securely to JSON vault. | ![Add Account](docs/img/features/add-account.jpg) |
| Get Account | View stored login details by account name. | ![Get Account](docs/img/features/get-password.jpg) |
| View Accounts | List all stored accounts. | ![View Accounts](docs/img/features/view-accounts.jpg) |
| Delete Account | Remove account from the vault. | ![Delete Account](docs/img/features/delete-account.jpg) |

### Future Features
- Password generator for creating secure passwords.  
- Encrypt vault contents (AES/Fernet).  
- Export/import vault.  
- Desktop GUI.  
- Mobile app.  

---

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Lucidchart-grey?logo=lucid&logoColor=F97B2C)](https://www.lucidchart.com) | Flow diagrams for mapping the app's logic. |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |


---

## Database Design

### Data Model

Vault data is stored in a JSON file (`vault.json`) with the following structure:

```json
{
  "google": { "username": "user123", "password": "mypassword" },
  "twitter": { "username": "birduser", "password": "securepass" }
}
```

---

### Flowchart

To follow best practice, a flowchart was created to illustrate the logic of **PwdShell**.  
It shows the cycle of setting/verifying a master password and the main menu actions.  

![flowchart](docs/img/flowchart.jpg)
> Below is the interactive Mermaid flowchart equivalent of the program logic:

```
mermaid
flowchart TD
    A([Start]) --> B{Master Password Exists?}
    B -- No --> C[Create Master Password]
    C --> D[Save]
    D --> E[Password Correct?]
    B -- Yes --> E

    E -- No --> F([Exit])
    E -- Yes --> G{Show Menu}

    G --> H[Add an Account]
    G --> I[Get Saved Password]
    G --> J[View Accounts]
    G --> K[Delete Account]
    G --> L([Exit])

    H --> G
    I --> G
    J --> G
    K --> G
    L --> M([Exit])
```


---

### Imports

PwdShell uses the following Python libraries:

- `getpass` – securely handle hidden password input.  
- `os` – check environment variables and clear the terminal.  
- `json` – store and retrieve account data from `vault.json`.  
- `cryptography.fernet.Fernet` – generate and manage an encryption key.  
- `hashlib` – hash the master password using SHA-256.  

---

### Functions

The main functions in **PwdShell** are:

- `clear()`  
  Clears the terminal screen for readability (cross-platform).  

- `set_master_password(user_id="default_user")`  
  Prompts the user to set a master password.  
  - On **Heroku**, the password is stored in memory (`user_sessions`) for the session.  
  - On **local**, it hashes the password with SHA-256 and saves it to `master.key`.  

- `master_password(user_id="default_user")`  
  Verifies the master password entered by the user against either session memory (Heroku) or the stored hash (local).  

- `load_key()`  
  Loads an encryption key from `key.key`. If the file doesn’t exist, a new key is generated and saved.  

- `load_vault()`  
  Loads the password vault from `vault.json`. If the file doesn’t exist or is invalid, it returns an empty dictionary.  

- `save_vault(vault)`  
  Saves the current state of the vault back into `vault.json`.  

- `add_new_password(vault)`  
  Adds a new account (account name, username, password) to the vault.  

- `get_password(vault)`  
  Retrieves and prints the username and password for a given account.  

- `view_accounts(vault)`  
  Lists all stored account names in the vault.  

- `delete_account(vault)`  
  Deletes an account from the vault and updates the file.  

- `main()`  
  Runs the application. Handles master password setup/verification, loads the vault, and provides the main menu loop.  

---

### Program Flow

1. User sets or verifies the master password.  
2. The vault is loaded from `vault.json`.  
3. The main menu is displayed.  
4. User can choose to:  
   - Add a new password  
   - Get a password  
   - View all accounts  
   - Delete an account  
   - Exit the program  
5. Vault changes are saved automatically.  

---

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/colmwoods/PwdShell/projects) served as the Agile tool for this project.  
Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban board.  

![Kanban Board](docs/img/kanban.jpg)

---

### GitHub Issues

[GitHub Issues](https://www.github.com/colmwoods/PwdShell/issues) served as another Agile tool.  
Here I managed User Stories, Milestones, and tracked any bugs that were raised.  

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![Open Issues](docs/img/open-issue.jpg) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![Closed Issues](docs/img/closed-issue.jpg) |

---

### MoSCoW Prioritization

I decomposed EPICs into User Stories and applied **MoSCoW prioritization** using labels in GitHub Issues:  

- **Must Have**: guaranteed to be delivered – required to pass the project (*max ~60% of stories*).  
- **Should Have**: adds significant value, but not vital (*~20% of stories*).  
- **Could Have**: has small impact if left out (*~20% of stories*).  
- **Won't Have**: not a priority for this iteration – future features.  



---

## Testing

Manual testing was carried out to ensure the reliability of **PwdShell**.  
Key areas tested included:  

- **Master Password Handling**  
  - Verified correct setup and storage of master password (local hash and Heroku session).  
  - Tested incorrect, empty, and mismatched inputs.  

- **Vault Operations (CRUD)**  
  - Adding accounts: prevented duplicates, validated empty input.  
  - Retrieving accounts: checked correct details returned, handled missing accounts gracefully.  
  - Viewing accounts: confirmed correct list output when vault had entries and when empty.  
  - Deleting accounts: verified successful deletion and appropriate error message if not found.  

- **General Validation**  
  - Menu input tested with valid/invalid choices.  
  - Confirmed program exited cleanly with `Exit` option or `CTRL+C`.  

Full details of all test cases and results can be found in [TESTING.md](TESTING.md).


---

## Deployment

### Heroku Deployment

Deployed on Heroku using the [Code Institute Python template](https://github.com/Code-Institute-Org/python-essentials-template).  

- Live app: [PwdShell on Heroku](https://pwdshell-6bf799458b95.herokuapp.com)  

> [!NOTE]  
> On the **Heroku deployed version** of PwdShell, the master password is stored **session-only**.  
> - When you first visit the app, you will be prompted to create your own master password.  
> - After you press the run program button again, you will be prompted to set a new master password.  
>
> This behavior is intentional, so that each user (including assessors) can create their own password without needing the developer’s local credentials.

Deployment steps:  
- Create a new Heroku app.  
- Add buildpacks (`Python`, `Node.js`).  
- Add files (`requirements.txt`, `Procfile`, `.python-version`).  
- Connect GitHub repo and enable auto-deploy.  

---

### Local Development

> [!NOTE]  
> On the **local version** of PwdShell, the master password is stored in a `master.key` file on your machine once you set it.  
> - The first time you run the program, you will be prompted to create a master password.  
> - The password is hashed using **SHA-256** and saved to `master.key`.  
> - On subsequent runs, you will be prompted to **enter your existing master password** for verification.  
>
> Unlike the Heroku version, the local master password is **persistent** and will remain the same until the `master.key` file is deleted or replaced.  

Clone this repo:

```
bash
git clone https://www.github.com/colmwoods/PwdShell.git
cd PwdShell
python3 run.py
```

---

### Local vs Deployment

- **Heroku version**:  
  - The master password is stored **session-only** (reset each time the “Run Program” button is pressed or the dyno restarts).  
  - This ensures every user, including assessors, can create their own master password without needing the developer’s.  

- **Local version**:  
  - The master password is saved in a `master.key` file after setup.  
  - It is **hashed with SHA-256** and persists across runs until the file is deleted or replaced.  

Apart from this difference in password handling, both versions function identically.  


## Credits

### Content
- [Python hashlib docs](https://docs.python.org/3/library/hashlib.html)  
- [Cryptography docs](https://cryptography.io/en/latest/)  
- [StackOverflow](https://stackoverflow.com) – troubleshooting help  
- [ChatGPT](https://chat.openai.com) – debugging and explanations  
- [Markdown Builder](https://markdown.2bn.dev) – helped generate Markdown structure  
- [Chris Beams – How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit)  
- [Code Institute – Love Sandwiches project](https://codeinstitute.net) – inspiration for layout  
- [Python Tutor](https://pythontutor.com) – extra Python debugging help  
- [Colorama Tutorial](https://www.youtube.com/watch?v=u51Zjlnui4Y) – for adding color in Python  
- [StackOverflow Clear Screen](https://stackoverflow.com/a/50921841) – clear screen function  

### Media
- [ASCII Art Archive](https://www.asciiart.eu) – terminal ASCII art inspiration  
- [Patorjk](https://patorjk.com/software/taag) – text-to-ASCII generator  

### Acknowledgements
- Thanks to my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN), for support.  
- Thanks to the [Code Institute Tutor Team](https://codeinstitute.net) for assistance with debugging.  
- Thanks to the [Code Institute Slack community](https://code-institute-room.slack.com) for encouragement.  
- Thanks to my partner, for believing in me and supporting this career change.  
- Thanks to my employer, for supporting me in my career development.  
- Thanks to friends and family for motivation during the project.  
