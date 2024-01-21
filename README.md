# custom-component-gen for the @material/web library

### A script that will generate a file that enables the use of Material Web Components in React (works with Typescript) 🚀

---

**Disclaimer**

This script was made for the purpose of helping other developers use the @materia/web library for their React projects. I am not one of the developers for the @material/web library, but I simply came across the issue of the library not working natively in React and I decided to write a script based on a workaround from one of their developers. This workaround can be found in the @material/web Github Repo's discussions, found [here](https://github.com/material-components/material-web/discussions/5186). This script will basically do the workaround for each component that's available in the library, generate a file that anyone can paste in their React project, and make it usable right away.

> I would love a star ⭐️ though for this repository if you found this helpful 🤩

Also, this script does not connect to the internet, whatsoever. I'm sure people would appreciate this sense of privacy, and therefore you would have to download the necessary file for the script to use as reference manually from the @material/web's Repo: [here](https://github.com/material-components/material-web)

---

**Requirements**

- python installed on your computer

---

**Description**

The [@material/web library](https://m3.material.io/) is the new official web components library from Google. It currently does not provide the native support to be used in a React project. Therefore, based on the discussion in their official GitHub Repo: [here](https://github.com/material-components/material-web/discussions/5186) , they were able to make the @material/web component work in React.

However, typing every single component out to make it work like that would take A LOT of work. So, I wrote this script to help other people who wanted to use the @material/web components in a React project, and fast track them to having all the available components right away.

NOTE: you have to run the python script everytime they add a new component to their library. Not all components are finished as of my time of writing this, (January 2024), so if they add a new component to their library... just follow the instructions below again. It should not take more than 30 seconds after you've done it once.

> Please give this repository a star 🌟 if you found it useful! Thanks guys!

Feel free to let me know if there's any issue with the script in this repo's _issues_. Thanks!

---

**Instructions**

1. Download the @lit/react and @material/web libraries

run the commands:

`npm install @material/web` and `npm install --save-dev @lit/react`

or if you're using yarn:

`yarn add @material/web` and `yarn add --dev @lit/react`

2. go to the [Material Web Components GitHub Repository](https://github.com/material-components/material-web) and download the _all.ts_ file (it's in the the root folder of the repository)

> The all.ts file contains all the components available in @material/web. This serves as a list for the python script to generate a React component for each @material/web component. If they update this file, you would **NEED** to run this script again after you download the new version of all.ts. This is so you get all the components they potentially added in the new version.

3. Download and run the Python script
   run the command: `python componentGenerator.py`

> if this does not work, make sure you have Python installed by running `python --version` and the terminal should output something like "Python 3.11.0". Sometimes Python is ran as "python3" instead of just "python". Therefore, run `python3 --version` and make sure it returns a Python version. If so, run `python3 componentGenerator.py` instead.

4. Paste the generate file _material.ts_ in the root folder of your React Project

5. Use the Material Web Components in your React Project 😎

**Example on using the new React components from @material/web**

Lets say you want to use the _filled-tonal-button_ they tell you to do:

`import '@material/web/button/filled-tonal-button.js';`

and then:

`<md-filled-tonal-button>Tonal</md-filled-tonal-button>`

_BUT SINCE WE ARE USING REACT, THIS DOES NOT WORK.
WE NEED TO USE THE GENERATED FILE_

The way we would use the component in React:

`import { MDFilledTonalButton } from "@/material"`

and then:

`<MdFilledTonalButton>Tonal</MdFilledTonalButton>`

> the import above pretends that "@" is the root directory of your project

5. At this point, you should have the button on screen. You are now ready to use any custom component from @material/web 🎉

---

**Additional guidance on how to use the @material/web components**

1. Go to the [Material Design website](https://m3.material.io/), and choose "components"

2. Choose a component you would like to use, for example: you wanted to use their [Button](https://m3.material.io/components/buttons/overview) component.

3. Look for _"Web - MWC"_ under the _Resources_ section and click on that

4. You are now in the documentation of that specific component. Goodluck!
