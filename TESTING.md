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
|  | [run.py](https://github.com/colmwoods/PwdShell/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/PwdShell/main/run.py) | ![screenshot](documentation/validation/py--run.png) | All previous errors (E302, E501, W293) resolved. |

---

## Responsiveness

The Python terminal was provided by Code Institute, and is known to have responsiveness issues.  
However, I still tested the deployed version on multiple screen sizes using **Chrome DevTools** and an **Android phone**.  

| Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- |
| ![screenshot](documentation/responsiveness/mobile-terminal.png) | ![screenshot](documentation/responsiveness/tablet-terminal.png) | ![screenshot](documentation/responsiveness/desktop-terminal.png) | Mobile: `overflow-x` occurs. iPhone does not accept input. Android accepts input but can stop randomly. |

---

## Browser Compatibility

I tested the deployed site on multiple browsers.  

| Chrome | Firefox | Safari | Edge | Notes |
| --- | --- | --- | --- | --- |
| ![screenshot](documentation/browsers/chrome-terminal.png) | ![screenshot](documentation/browsers/firefox-terminal.png) | ![screenshot](documentation/browsers/safari-terminal.png) | ![screenshot](documentation/browsers/edge-terminal.png) | Chrome: works fully. Firefox: emojis cut-off. Safari: terminal input unreliable. Edge: works as expected. |

---

## Lighthouse Audit

I ran Lighthouse audits on the deployed Heroku site.  
Scores are lower on mobile due to **third-party scripts** and **Code Institute terminal environment**, which are outside my control.  
Desktop performance and accessibility scored higher.  

| Mobile | Desktop |
| --- | --- |
| ![screenshot](documentation/lighthouse/mobile-terminal.png) | ![screenshot](documentation/lighthouse/desktop-terminal.png) |

---

## Defensive Programming

Defensive programming was tested extensively, covering both **happy paths** and **bad inputs**.  

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Master Password Setup | Should not accept empty or mismatched passwords. | Pressed Enter with no input, and entered two different passwords. | Both rejected with clear error messages. | ![screenshot](documentation/defensive/master-password.png) |
| Login Attempts | Only correct master password should unlock. | Tried wrong password 3 times, then correct one. | Wrong attempts rejected, correct one accepted. | ![screenshot](documentation/defensive/login.png) |
| Add Account | Should reject duplicates. | Added "google" twice. | First saved, second rejected. | ![screenshot](documentation/defensive/add-duplicate.png) |
| Get Password | Should return correct credentials if they exist. | Retrieved "twitter" account. | Correct details displayed. | ![screenshot](documentation/defensive/get-password.png) |
| Delete Account | Should handle missing accounts. | Deleted "twitter" twice. | First deleted, second rejected. | ![screenshot](documentation/defensive/delete.png) |
| Empty Input | Should not accept blank values. | Tried adding account with blank username. | Input rejected with error. | ![screenshot](documentation/defensive/empty-input.png) |
| Exit Handling | Program should close safely. | Used Exit menu and pressed CTRL+C. | Exit menu closed cleanly, CTRL+C showed handled error. | ![screenshot](documentation/defensive/exit.png) |

---

## User Story Testing

All user stories from the README were manually tested.  

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I want to set and confirm a master password | so that my vault is secure. | ![screenshot](documentation/features/master-password.png) |
| As a user | I want to log in with my master password | so that only I can access my vault. | ![screenshot](documentation/features/login.png) |
| As a user | I want to add new accounts | so that I can securely save my credentials. | ![screenshot](documentation/features/add.png) |
| As a user | I want to view stored accounts | so that I can check which ones are saved. | ![screenshot](documentation/features/view.png) |
| As a user | I want to retrieve a password | so that I can log into accounts when needed. | ![screenshot](documentation/features/get.png) |
| As a user | I want to delete accounts | so that I can keep the vault clean. | ![screenshot](documentation/features/delete.png) |
| As a user | I want to exit safely at any time | so that I don’t corrupt the vault. | ![screenshot](documentation/features/exit.png) |

---

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

- Fixed `PEP8` violations (E302, E501, W293, indentation issues).  
- Fixed issue where mismatched passwords in setup caused crash → now loops until valid.  
- Fixed JSON decode error when vault.json was empty/corrupted → now defaults to empty dict.  

![screenshot](documentation/bugs/gh-issues-closed.png)

---

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/PwdShell?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/colmwoods/PwdShell/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Currently, no functional bugs remain open. Any remaining issues are environmental (see below).  

![screenshot](documentation/bugs/gh-issues-open.png)

---

### Known Issues

| Issue | Explanation | Screenshot |
| --- | --- | --- |
| `clear()` does not fully clear when scrolling up. | Limitation of terminal height in Code Institute IDE. | ![screenshot](documentation/issues/clear-scrolling.png) |
| Colors fainter on Heroku. | Due to Code Institute’s terminal emulator. | ![screenshot](documentation/issues/colorama.png) |
| Emojis cut off in Firefox. | Known rendering issue with terminal fonts. | ![screenshot](documentation/issues/emojis.png) |
| Input broken in Safari/iOS. | Code Institute terminal not fully supported. | ![screenshot](documentation/issues/safari.png) |
| CTRL+C exits with error message. | Default Python behavior, partially handled with exception catch. | ![screenshot](documentation/issues/ctrl-c.png) |

> [!IMPORTANT]  
> No remaining functional bugs are known. Environment-specific issues have been documented.  
