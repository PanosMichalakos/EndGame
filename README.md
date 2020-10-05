# EndGame News Website

EndGame is a WIP News Website, built in Django (backend), using the template [Endgam template](https://colorlib.com/wp/template/endgam/).

List of working features:
-
- Index
- News
- Search Feature
- Admin Panel
- Subscribe to newsletter
- Pagination

ToDo:
-
- User Auth
- Mailchimp for newsletter
- Authors for article editing
- Chat room for users
- Contact Us page with map and contact info
## Installation

Create a virtualenv:

```bash
virtualenv env
```
Install requirements.txt

```bash
pip install -r requirements.txt
```
Make migrations
```bash
manage.py makemigrations
manage.py migrate
```
Run Django server

```bash
manage.py runserver
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
