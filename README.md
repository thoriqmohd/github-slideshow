# Your GitHub Learning Lab Repository for Introducing GitHub

Welcome to **your** repository for your GitHub Learning Lab course. This repository will be used during the different activities that I will be guiding you through. See a word you don't understand? We've included an emoji 📖 next to some key terms. Click on it to see its definition.

Oh! I haven't introduced myself...

I'm the GitHub Learning Lab bot and I'm here to help guide you in your journey to learn and master the various topics covered in this course. I will be using Issue and Pull Request comments to communicate with you. In fact, I already added an issue for you to check out.

![issue tab](https://lab.github.com/public/images/issue_tab.png)

I'll meet you over there, can't wait to get started!

This course is using the :sparkles: open source project [reveal.js](https://github.com/hakimel/reveal.js/). In some cases we’ve made changes to the history so it would behave during class, so head to the original project repo to learn more about the cool people behind this project.

## Running the School App

This repository now includes a small command line application for storing simple
school records. The CLI is located in the `school_app/` folder.

### Setup

The CLI uses only the Python standard library. Ensure you have Python 3
installed, then run commands with:

```bash
python school_app/cli.py --help
```

### Examples

Add a student and list all students:

```bash
python school_app/cli.py add_student "Alice" 13
python school_app/cli.py list_students
```

The data is stored in `school_app/data.json`. You can edit or delete entries
using similar commands, for example:

```bash
python school_app/cli.py edit_student <id> "Alicia" 14
python school_app/cli.py delete students <id>
```
