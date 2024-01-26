# 0x15. JavaScript - Web jQuery
### Resources
- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- Manipulate CSS classes
- Manipulate DOM elements
- API
- Introduction
- GET & POST request
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- JQuery
- JQuery API
- [JQuery Ajax](https://learn.jquery.com/ajax/)

## Import JQuery
```HTML
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## [0. No JQuery](0-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the JQuery API

## [1. With JQuery](1-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API

## [2. Click and turn red](2-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`

## [3. Add `.red` class](3-script.js)

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`

## [4. Toggle classes](4-script.js)

Write a JavaScript script that toggles the class of the `<header> `element when the user clicks on the tag `DIV#toggle_header`:

- The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
- If the current class is red, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.


## [5. List of elements](5-script.js)

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`

## [6. Change the text](6-script.js)

Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`

## [7. Star wars character](7-script.js)

Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`


## [8. Star Wars movies](8-script.js)

Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`

- All movie titles must be list in the HTML tag `UL#list_movies`

## [9. Say Hello!](9-script.js)

Write a JavaScript script that fetches from h`ttps://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.

- The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- Your script must work when it is imported from the `<head>` tag

## [10. No jQuery - document loaded](100-script.js)

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

## [11. List, add, remove](101-script.js)

Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks

## [12. Say hello to everybody!](102-script.js)

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetched when the user clicks on `INPUT#btn_translate`
- The translation of “Hello” must be displayed in the HTML tag `DIV#hello`

## 13. And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
- The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER`