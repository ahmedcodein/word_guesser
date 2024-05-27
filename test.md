# Test Appendix

This Appendix contains the screenshots of all the tests conducted.

## CI Python Linter

This file contains the captures of the test results of CI Python Linter for each class code.

1. Class InitiateGame
![CI Python Linter for Class InitiateGame](docs/images/intiategame.png)

2. Class Player
![CI Python Linter for Class Player](docs/images/player.png)

3. Class DifficultySelection
![CI Python Linter for Class DifficultySelection](docs/images/difficultyselection.png)

4. Class WordSelector
![CI Python Linter for Class WordSelector](docs/images/wordselector.png)

5. Class PlayerGuess
![CI Python Linter for Class PlayerGuess](docs/images/playerguess.png)

6. Class GameMixins
![CI Python Linter for Class GameMixins](docs/images/gamemixins.png)

## Lighthouse Test


The following screenshot shows the test result of Lighthouse tool.

**The initial test shows an issue of missing meta tags for the search engin. The issue is resolved by adding the relevant tags.**

![Lighthouse](docs/images/lighthouse.png)

## Web Accessibility Evaluation Tools (WAVE )

The following screenshot shows the test result of Wave. It is worth mentioning here that test shows an alert of missing a heading structure. The solution is to add an h1 heading element. The author decides to leave it the way it is since the alert comes with default design of CI console.

![Wave](docs/images/wave.png)

## W3C Markup Validation Service

The following screenshot shows the test result of W3C Markup Validation Service. The result does not show any errors.

![W3C HTML](docs/images/w3c-html.png)

## Chrome DevTools

In Chrome DevTools, the author observes the following issue: 

**A form field element should have an id or name attribute
A form field element has neither an id nor a name attribute. This might prevent the browser from correctly auto filling the form.
To fix this issue, add a unique id or name attribute to a form field. This is not strictly needed, but still recommended even if you have an autocomplete attribute on the same element.**

The author does not consider finding a resolution to this issue since it comes as a default issue with CI console design.

A screenshot of the issue is provided below:

![Chrome DevTools](docs/images/chrome_devtools.png)


## Console Flaw

There is an issue with the console occurs when the game is reset multiple time. It seems that console does not effectively clear the screen completely after each game reset, resulting in accumulating some previous screen views from earlier rounds. See the screenshot below.

![Console Flaw](docs/images/console-flaw.png)


Return to [Readme file](README.md)

