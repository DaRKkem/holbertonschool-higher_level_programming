# JavaScript DOM Manipulation

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) ![HTML5](https://img.shields.io/badge/HTML5-semantic-orange)

```js
document.querySelector('header').style.color = '#FF0000';
```

Nine tasks pairing HTML pages with JavaScript scripts to progressively explore the Document Object Model. Starting from simple style changes with `document.querySelector`, the exercises advance through event listeners, element creation, and dynamic API-driven content.

---

## Tasks

### 0. Change the header color (script + HTML)
**Files:** `0-script.js`, `index0.html` -- Uses `document.querySelector` to change the `<header>` text color to red.

### 1. Change the header color with `#red_header`
**Files:** `1-script.js`, `index1.html` -- Adds a click event listener on a `DIV#red_header` to change the header color.

### 2. Toggle header class
**Files:** `2-script.js`, `index2.html` -- Toggles a CSS class on the `<header>` element when clicking `DIV#toggle_header`.

### 3. Add a `<li>` to the list
**Files:** `3-script.js`, `index3.html` -- Appends a new `<li>` element to `UL.my_list` when clicking `DIV#add_item`.

### 4. Remove an item from the list
**Files:** `4-script.js`, `index4.html` -- Removes the last `<li>` from `UL.my_list` when clicking `DIV#remove_item`.

### 5. Clear the list
**Files:** `5-script.js`, `index5.html` -- Empties all child `<li>` elements from `UL.my_list` when clicking `DIV#clear_list`.

### 6. Fetch and list Star Wars characters
**Files:** `6-script.js`, `index6.html` -- Uses the `fetch` API to load character names from `https://swapi-api.hbtn.io/api/people/5/?format=json` and displays them in `DIV#character`.

### 7. Fetch and list all Star Wars movies
**Files:** `7-script.js`, `index7.html` -- Fetches `https://swapi-api.hbtn.io/api/films/?format=json` and lists all movie titles in `UL#list_movies`.

### 8. Update a `<div>` with fetched content
**Files:** `8-script.js`, `index8.html` -- Fetches a greeting translation from `https://hellosalut.stefanbohacek.dev/?lang=fr` and inserts it into `DIV#hello`.

---

## Key Concepts

- `document.querySelector` and `document.querySelectorAll`
- Element style manipulation via `.style` property
- Event listeners (`addEventListener`)
- `document.createElement` and `appendChild`
- Class list manipulation (`classList.toggle`)
- `fetch` API for HTTP requests
- Dynamic DOM updates from API responses

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
