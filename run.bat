(if exist "allure-report" rmdir "allure-report" /s /q)
pytest --alluredir allure-report
allure serve allure-report