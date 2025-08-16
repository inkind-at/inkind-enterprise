# inkind-enterprise
A digital inventory management platform that facilitates the intake, categorization, and distribution of in-kind donations for social enterprises — with transparency and communication between enterprises and donors.

## Development

### Translations

Managing translations is a three-step process:

**Step 1: Mark and Extract Strings**

First, ensure all user-facing strings in your templates (`.html`) and Python files (`.py`) are marked for translation.

-   In templates, use `{% load i18n %}` at the top and wrap strings with `{% trans "Your string here" %}`.
-   In Python code, import `from django.utils.translation import gettext as _` and wrap strings with `_("Your string here")`.

Once strings are marked, run the following command to extract them into a `.po` file. Replace `de` with the desired language code.

```bash
django-admin makemessages -l de
```

**Step 2: Translate the Strings**

Open the generated file at `locale/<language_code>/LC_MESSAGES/django.po`. For each `msgid`, you must manually add the translation in the corresponding `msgstr`.

Example:

```po
#: templates/landing.html:10
msgid "A seamless solution for managing in-kind donations."
msgstr "Eine nahtlose Lösung für die Verwaltung von Sachspenden."
```

**Step 3: Compile the Translations**

After saving your changes to the `.po` file, run the following command to compile the messages into a `.mo` file, which Django uses to serve the translations.

```bash
django-admin compilemessages
```

Your translations should now be visible in the application when the language is switched to German.
