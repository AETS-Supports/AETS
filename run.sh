#!/bash/sh

pytest test_cases/test_allure.py --clean-alluredir --alluredir=allure_results
cp environment.properties allure_results

# way 1:
# allure serve allure_results

# way 2:
allure generate allure_results -c -o allure_report
allure open allure_report