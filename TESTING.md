# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

---

## Code Validation

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.  
Validation was performed using the **raw GitHub URL** method, which ensures the deployed version is validated, not just local code.

After making fixes (line wrapping, removing excess blank lines, correcting indentation),  
`run.py` passes validation with **0 errors and 0 warnings**.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [run.py](https://github.com/colmwoods/PwdShell/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PwdShell/main/run.py) | ![screenshot](docs/img/pep8-testing.jpg) | All previous errors (E302, E501, W293) resolved. |

---

## Responsiveness

The Python terminal was provided by Code Institute, and is known to have responsiveness issues.  
However, I still tested the deployed version on multiple screen sizes using **Chrome DevTools** and an **Android phone**.  

| Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- |
| ![screenshot](docs/img/responsiveness/mobile.jpg) | ![screenshot](docs/img/responsiveness/tablet.jpg) | ![screenshot](docs/img/responsiveness/desktop.jpg) | Mobile: `overflow-x` occurs. iPhone does not accept input. Android accepts input but can stop randomly. |

---

## Browser Compatibility

I tested the deployed site on multiple browsers.  

| Chrome | Firefox | Safari | Edge | Opera | Brave | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| ![screenshot](docs/img/browser/chrome.jpg) | ![screenshot](docs/img/browser/firefox.jpg) | ![screenshot](docs/img/browser/safari.jpg) | ![screenshot](docs/img/browser/edge.jpg) | ![screenshot](docs/img/browser/opera.jpg) | ![screenshot](docs/img/browser/brave.jpg) | Chrome: works fully. Firefox: emojis cut-off. Safari: terminal input unreliable. Edge: works as expected. Opera: works as expected. Brave: works fully |

---

## Lighthouse Audit

I ran Lighthouse audits on the deployed Heroku site.  
Scores are lower on mobile due to **third-party scripts** and **Code Institute terminal environment**, which are outside my control.  
Desktop performance and accessibility scored higher.  

| Mobile | Desktop |
| --- | --- |
| ![screenshot](docs/img/lighthouse/mobile.jpg) | ![screenshot](docs/img/lighthouse/desktop.jpg) |

---

## Defensive Programming

Defensive programming was tested extensively, covering both **happy paths** and **bad inputs**.  

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Master Password Setup | Should not accept empty or mismatched passwords. | Pressed Enter with no input, and entered two different passwords. | Both rejected with clear error messages. | ![screenshot](docs/img/defensive-programming/master-password-setup.jpg) |
| Login Attempts | Only correct master password should unlock. | Tried wrong password 3 times, then correct one. | Wrong attempts rejected, correct one accepted. | ![screenshot](docs/img/defensive-programming/login-attempts.jpg) |
| Add Account | Should reject duplicates. | Added "google" twice. | First saved, second rejected. | ![screenshot](docs/img/defensive-programming/add-account.jpg) |
| Get Password | Should return correct credentials if they exist. | Retrieved "twitter" account. | Correct details displayed. | ![screenshot](docs/img/defensive-programming/get-password.jpg) |
| Delete Account | Should handle missing accounts. | Deleted "twitter" twice. | First deleted, second rejected. | ![screenshot](docs/img/defensive-programming/delete-account.jpg) |
| Empty Input | Should not accept blank values. | Tried adding account with blank username. | Input rejected with error. | ![screenshot](docs/img/defensive-programming/empty-input.jpg) |
| Exit Handling | Program should close safely. | Used Exit menu and pressed CTRL+C. | Exit menu closed cleanly, CTRL+C showed handled error. | ![screenshot](docs/img/defensive-programming/exit-handling.jpg) |
| Efficient Prompts | Users should never be asked for data already stored. | Tried creating a master password twice; tried adding duplicate account. | App reused stored master key / rejected duplicate account with error message. |

---

### Error Reporting
Errors caused by user or data actions are always reported back to the user in a clear, colour-coded way:
- **Input validation**: Blank or mismatched passwords, invalid menu choices, and duplicate entries are rejected with red error messages.  
- **Data handling**: Corrupted or missing `vault.json` files trigger an error message and the app safely resets to an empty vault.  
- **Session handling**: On wrong master password attempts, the user is notified immediately and access is blocked.  
- **Exit handling**: CTRL+C interrupts display a friendly error message instead of a crash.  

This ensures the user is always informed of what went wrong and how the program has responded.

---

## User Story Testing

All user stories from the README were manually tested.  

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I want to set and confirm a master password | so that my vault is secure. | ![screenshot](docs/img/user-story/set-master-password.jpg) |
| As a user | I want to log in with my master password | so that only I can access my vault. | ![screenshot](docs/img/user-story/log-in-master-password.jpg) |
| As a user | I want to add new accounts | so that I can securely save my credentials. | ![screenshot](docs/img/user-story/add-account.jpg) |
| As a user | I want to view stored accounts | so that I can check which ones are saved. | ![screenshot](docs/img/user-story/view-accounts.jpg) |
| As a user | I want to retrieve a password | so that I can log into accounts when needed. | ![screenshot](docs/img/user-story/get-password.jpg) |
| As a user | I want to delete accounts | so that I can keep the vault clean. | ![screenshot](docs/img/user-story/delete-account.jpg) |
| As a user | I want to exit safely at any time | so that I don’t corrupt the vault. | ![screenshot](docs/img/user-story/exit-safely.jpg) |

---

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

- Fixed `PEP8` violations (E302, E501, W293, indentation issues).  
- Fixed issue where mismatched passwords in setup caused crash → now loops until valid.  
- Fixed JSON decode error when vault.json was empty/corrupted → now defaults to empty dict.
- **Fixed Deployment Bug**: 
  - Heroku defaulted to Python 3.13, causing dependency build errors (`pillow`, `numpy`).  
  - Added `.python-version` file to pin Python to 3.12.  
  - Cleaned up `requirements.txt` to include only actual dependencies (`cryptography`, `colorama`).  
  - After these fixes, the build completed and the app deployed successfully.  
- **Fixed Input Validation Bug**:  
  - Previously, blank values for account name, username, or password were still accepted.  
  - Added if, else defensive checks to reject empty inputs inside the add_new_password function, ensuring all fields must be filled before saving.  

![screenshot](docs/img/fixed-bugs.jpg)

---

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Currently, no functional bugs remain open. Any remaining issues are environmental (see below).

---

### Known Issues

| Issue | Explanation | Screenshot |
| --- | --- | --- |
| Colors fainter on Heroku. | Due to Code Institute’s terminal emulator. | ![screenshot](docs/img/known-issues/color-heroku.jpg) |
| Emojis cut off in Firefox. | Known rendering issue with terminal fonts. | ![screenshot](docs/img/known-issues/firefox-issue.jpg) |
| Input broken in Safari/iOS. | Code Institute terminal not fully supported. | ![screenshot](docs/img/known-issues/safari-issue.jpg) |
| CTRL+C exits with error message. | Default Python behavior, partially handled with exception catch. | ![screenshot](docs/img/known-issues/ctrl-c.jpg) |

> [!NOTE]  
> Some design choices, such as storing passwords in plaintext JSON and not enforcing password strength rules, are deliberate.  
> They were made to ensure simplicity, transparency, and easy assessment by Code Institute, while still demonstrating hashing, file handling, and secure input with `getpass`.  
> These choices are appropriate for the target audience of this educational project and do not represent logic errors.


> [!IMPORTANT]  
> No remaining functional bugs are known. Environment-specific issues have been documented.  
