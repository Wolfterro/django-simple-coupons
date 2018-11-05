run:
	@python manage.py runserver

clean:
	@rm -rf build/ dist/ django_simple_coupons.egg-info/

build:
	@python setup.py sdist bdist_wheel

upload:
	@twine upload dist/*
