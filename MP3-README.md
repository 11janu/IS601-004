<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Jahnavi Soman (js2679)</td></tr>
<tr><td> <em>Generated: </em> 4/21/2023 2:09:09 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/js2679" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233283883-ec8e83d4-67ba-4b18-8bc1-3817cb33c14e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page with updated UCID, showing from heroku dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233409710-841f5b92-4852-4af3-90e8-d144d3913ebc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Db showing companies table populated with values<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233409768-6f4f4f94-ae59-4b81-8fe5-ea677a330e28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB showing employee table populated with values<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233355254-5d84cfcc-b424-43fa-8daf-e2ef2dc539c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route to import data from a CSV file<br>into the database. The code checks if the request method is &quot;POST&quot; using<br>request.method, indicating that a file has been uploaded.  If a file has<br>been uploaded, the code retrieves the file from the request using request.files[&#39;file&#39;]. It<br>checks if the file has a valid filename and file extension (csv) and<br>sets a warning or error message using flash() if there are any issues.<br> If the file is valid, the code initializes two empty lists to<br>store the data: companies and employees.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233355699-07457010-a68c-4459-93df-dacbe5bf3b79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code reads the uploaded CSV file using a CSV reader. It loops<br>over each row in the CSV and checks if all required fields are<br>present in the row for both company and employee data.  If all<br>required fields are present, the code creates a dictionary for the company or<br>employee data and populates it with the values from the CSV row. For<br>company data, the keys are mapped to the database columns and for employee<br>data, the keys are kept as they are in the CSV.  The<br>company and employee dictionaries are appended to their respective lists companies and employees<br>for later use in the database insertions.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233356360-2857c016-af49-4603-b6fb-aca35b84ca91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The importCSV() function is used to handle the uploading and importing of CSV<br>files. It first checks if a file has been uploaded, and if so,<br>checks if it is a CSV file. If it is a CSV file,<br>it reads the data and separates it into two lists: companies and employees.<br>It then attempts to insert the data into the database using the insertMany()<br>function. It also counts the number of SQL queries that were executed during<br>the insertion process using the SHOW SESSION STATUS command. Finally, it returns the<br>upload.html template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233357306-4e15b9fa-3d2a-4b43-ae52-fad599932611.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website showing that 1000 employees were added successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233357402-1b3f8a5c-82a5-483e-90ed-df5ced03cfb1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message saying that only .csv files are accepted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233357526-0acd8ec4-9994-40c4-aee6-f94b2028f9f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message saying that some file should be submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233409768-6f4f4f94-ae59-4b81-8fe5-ea677a330e28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing employee data updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233409710-841f5b92-4852-4af3-90e8-d144d3913ebc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing company data updated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233369999-ead7ab5b-e7a8-45fa-8008-39aa595dfaf8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a Flask view function that handles both GET and POST requests<br>to add a new employee. If the request is POST, the function retrieves<br>form data for the first name, last name, company, and email, validates the<br>required fields, and verifies that the email is in the correct format using<br>a regular expression. The function then creates a dictionary of the form data<br>and passes it to the insertOne method of the DB object to insert<br>a new row into the IS601_MP3_Employees table. If the insert is successful, a<br>success message is flashed and the user is redirected to the add employee<br>page. If there is an error, an error message is flashed and the<br>user remains on the add employee page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233370219-8b8f5429-d9c3-4686-b0e9-ccd3174dd8b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a Flask view function for adding a new employee. It handles<br>both GET and POST requests. In case of a POST request, it retrieves<br>data from the form and validates required fields (first_name, last_name, email), and then<br>inserts the data into the database using the DB helper class. The company<br>name is used to find the corresponding company ID. If the insert is<br>successful, a success message is flashed, otherwise, an error message is displayed. Finally,<br>it renders the add_employee.html template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233374615-1d2f26e7-869b-4d7e-8931-9eee5b6827af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in data prior to submission of new employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233374811-a754e04b-2f72-464b-a65c-c6f611ffe7c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success message that new employee got added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233374902-fe19e79c-95b3-48ca-a6bc-13952bf0d861.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error messages when required fields are left empty and pressed submit button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233375507-8fc0964d-ac0d-4cbb-a8df-ae35cf672de8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New employee which was created can be seen on first row (I sorted<br>the db to show recent modifications first)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233376234-23a23dae-630a-4603-88a8-1a7dda0e2faa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The search function in the employee route searches for employees based on various<br>filter parameters passed as query parameters in the GET request. The function constructs<br>a SQL query to retrieve employee information including ID, first name, last name,<br>email, company ID, and company name, and applies filters to the query based<br>on the search parameters. The function then executes the query and returns the<br>resulting rows to a template for display. The allowed_columns list is used to<br>control which columns are displayed in the template.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233376676-04622b48-3afc-4340-a055-7fd369504668.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The search() function handles GET requests to search for employees based on provided<br>parameters. It retrieves the values of fn, ln, email, company, column, order, and<br>limit from the request args. It builds a SQL query with the given<br>parameters and executes it to retrieve the search results from the database. The<br>results are displayed in a template called list_employees.html. The allowed columns for sorting<br>are first_name, last_name, email, and company_name. The default limit for search results is<br>10, but it can be changed by providing the limit parameter in the<br>request. If the limit parameter is not provided, the default limit of 10<br>is used. If the limit parameter is provided but is not a valid<br>integer between 1 and 100, an error message is flashed. If an error<br>occurs during the search, an error message is flashed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233377061-26f36fe9-7ba9-42df-9b84-b301a59e9d89.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name filter applied with key word &#39;Del&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233377184-5f470631-edba-44ba-b6cd-edc881d56893.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last name filter applied with key word &quot;Shi&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233377286-4ebe6fa3-8329-4e97-b51a-056e052797d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mail filter applied with key word @gmaill.com<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233377479-d5b26277-e5b1-479c-89c3-8eaef7b69c8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company filter applied with key word &#39;A All American&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233378009-dc6a7138-d555-4540-99e4-3dbec05ecab6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mail column is selected and sorted ascending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233378079-6fc7aa1e-2600-4001-95fd-a227b4f43643.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mail column is selected and sorted descending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233379396-64edf8d7-5075-4c6e-8804-67fe2226e253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The code defines a Flask route for editing an existing employee record. It<br>first retrieves the ID of the employee to be edited from the request<br>arguments, and if not present, flashes an error message and redirects to the<br>employee search page. If the request method is POST, it retrieves the updated<br>form data for the employee&#39;s first name, last name, company, and email. It<br>then validates the first name and last name fields, and flashes an error<br>message if they are not present. It also retrieves the company ID from<br>the form, which can be None, and the email address, which it validates<br>against a regex pattern. If there are no errors, the code attempts to<br>update the employee record in the database with the new values using an<br>SQL query. If the update is successful, it flashes a success message and<br>redirects to the employee search page. Otherwise, it flashes an error message. The<br>corresponding HTML template for this route is not provided.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233380410-2230e0a1-4d14-4be8-a242-fa5d6497abee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a function for editing an employee&#39;s record. The function first checks<br>if the employee ID is provided in the request arguments, and if not,<br>flashes an error message and redirects the user to the search page. If<br>the ID is provided, the function checks if the request method is POST,<br>and if so, retrieves the form data for first name, last name, company,<br>and email. It then validates the data, checking that first name, last name,<br>and email are provided, and that the email is in a valid format.<br>If there are no errors, the function attempts to update the employee&#39;s record<br>in the database using the provided data. If the update is successful, it<br>flashes a success message; otherwise, it flashes an error message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233380788-0adb1806-8e61-4b6e-875e-3b2a979bae06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route that allows the user to edit an<br>employee record. The route can be accessed via GET or POST methods. If<br>the request method is POST, the form data is retrieved and validated, and<br>an update query is executed to modify the corresponding employee record. If the<br>update is successful, a success message is flashed. If the request method is<br>GET, the employee data is fetched from the database and passed to the<br>render template. The template renders an HTML form that allows the user to<br>edit the employee data, and includes a submit button to trigger the POST<br>request.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233381123-5372b877-3646-41e6-9cdd-69bbf8a6a943.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First row employee will be edited Zona Colla<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233382018-33b0416f-e909-465f-8214-3eaec7e9a2f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message showing that Update is a success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233382141-123e4d45-054d-4547-9273-2a11167e2b9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name of employee is edited to ZonaZona &amp; second name edited to<br>CollaColla<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233382298-ac6c71d4-7402-4e7c-9a35-30892e652917.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name of employee is edited to ZonaZona &amp; second name edited to<br>CollaColla<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233383756-4bd22fe9-42b6-4267-a06c-796ed3fdec7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route to add a new company record to<br>the database. It validates the submitted form data and sets the has_error flag<br>to True if any of the required fields (name, address, and city) are<br>missing.  The code checks if the request method is &quot;POST&quot; using request.method,<br>indicating that the form has been submitted. If the form data is valid,<br>the code will set has_error to False and proceed to insert the new<br>company record into the database.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233384124-b25d685a-a38b-4f28-b14b-e65046de2a65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code validates additional form data for adding a new company record. It<br>checks if the state and country fields are present in the form data<br>and whether the values are valid. If the state is missing or invalid,<br>it flashes an error message and sets the has_error flag to True. Similarly,<br>it checks if the country field is present and valid.  The code<br>also validates the zip code field and flashes an error message if it<br>is missing. Finally, it retrieves the website URL from the form data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233384213-8ecbec90-a16f-42ed-9869-50426dd63b9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code adds a new company record to the database if the form<br>data is valid. It first checks if the has_error flag is False, indicating<br>that there are no errors in the form data. If so, it inserts<br>the new record into the database using DB.insertOne() and sets a success message<br>using flash().  If an error occurs during the insert, it flashes an<br>error message. Finally, the code renders a template called &quot;add_company.html&quot;. If the request<br>method is not &quot;POST&quot;, the code will simply render the template without adding<br>a new record to the database.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233481878-308827cb-aa9c-4511-bdb7-e8eadba5e3a8.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filled data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233481959-3ef551ac-c628-44ea-a8d7-6f167dcefcfe.jpeg"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message after addition of company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233482277-1bf154c7-e02a-4f12-bd1e-64087653d06e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error messages if they are not filled and submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233482428-70c579b3-ac75-48f4-8433-a0912ed0b381.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test company added and seen in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233397265-f7e00577-d3ff-4693-80aa-50d822f4078a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route to search for companies based on certain<br>criteria. It retrieves the search criteria from the query string and builds a<br>SQL query to filter the results. It uses a LEFT JOIN to include<br>companies even if they have no employees. Finally, it executes the query and<br>stores the results in a list called &quot;rows&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233397328-12932202-4855-4c10-96d5-66c0340d4202.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code allows filtering and sorting of the company search results. It retrieves<br>the state filter parameter from the query string and adds it to the<br>SQL query if present. It also allows sorting of the results by a<br>specified column and order.  The code limits the number of search results<br>based on the &quot;limit&quot; parameter and adds it to the SQL query. If<br>the parameter is missing or invalid, it sets a default limit of 10.<br>Finally, it executes the SQL query with the parameters and stores the results<br>in a list called &quot;rows&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233397369-42ede2e2-5983-42f7-baed-873f8d72f48a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code executes the SQL query to search for companies with the specified<br>search criteria and retrieves the results using the DB.selectAll() method. If the query<br>is successful, it stores the results in a list called &quot;rows&quot;. If an<br>error occurs, it flashes an error message.  Finally, the code renders a<br>template called &quot;list_companies.html&quot; and passes the &quot;rows&quot; and &quot;allowed_columns&quot; lists as parameters. The<br>rest of the code for rendering the template is not shown.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233398393-63f57f95-4e6b-469f-a7d8-26ab779e1e1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter applied with key word &#39;cen&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233398780-1429f571-a1db-426b-9107-ef3d467b9504.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country filter applied with US as country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233398931-693ab91f-2499-4af6-b9b4-76329f167cb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State filter applied with New Jersey as state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233399164-cba5a1fd-e2f2-4e86-8d5a-95004058bf12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name column was chosen &amp; ascending <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233399258-189f176a-f58d-40fc-a1ad-4462649a5c4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name column was chosen &amp; descending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233399911-e403de2e-85a5-4e76-b0f2-4323cdcba69e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The given code defines a Flask route to edit a company record by<br>its ID. It validates the submitted form data for name, address, and city<br>fields and updates the corresponding company record in the database if there are<br>no errors. Finally, it flashes a success message and redirects to the company<br>search page. If the ID is not present, it flashes an error message<br>and redirects to the search page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233400694-f46f1ad7-3bde-4a2f-af89-4693ea083085.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route for editing a company by its ID.<br>It validates the submitted form data for the name, address, city, state, country,<br>and website fields. If any fields are missing or invalid, it flashes an<br>error message and sets the has_error flag to True. If all fields are<br>valid, it creates a dictionary of the validated data and updates the corresponding<br>company record in the database. Finally, it flashes a success message and redirects<br>to the company search page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233400758-2b285f68-c2a5-4060-8e9c-0a24f0f4d0ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code updates the corresponding company record in the database if there are<br>no errors in the form data. It retrieves the submitted value for the<br>&quot;zip&quot; field and adds it to the &quot;data&quot; dictionary. If there are no<br>errors in the form data, it attempts to update the corresponding company record<br>in the database using a SQL query and the DB.update() method. If the<br>update is successful, it flashes a success message. If an error occurs, it<br>prints the error to the console and flashes an error message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233400804-060923ec-a434-46ce-96dc-ed15584b8887.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code retrieves the company record with the given ID from the database<br>using the DB.selectOne() method and a SQL query. If the query is successful,<br>it stores the result row in a dictionary called &quot;row&quot;. If an error<br>occurs, it flashes an error message.  Finally, the code renders a template<br>called &quot;edit_company.html&quot; and passes the &quot;row&quot; dictionary as a parameter. The rest of<br>the code for rendering the template is not shown.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233401773-2523b205-e462-493c-b0f2-ce0c60d7e9f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before the editing of 1st name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233401921-eba7dba1-40f9-4f99-b25e-7b9885dd374a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Removed part of name &quot;John Br&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233401434-66cac488-6ac0-4516-afda-d2d3692abb5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before the editing of 1st name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233401986-777f9c30-d623-41ac-890b-243b22f5de6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Removed part of name &quot;John Br&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403180-8a71f0f0-0675-44b8-a63a-1dba68568839.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route for deleting an employee by their ID.<br>It retrieves the ID from the query string, deletes the corresponding employee record<br>from the database, flashes a success or error message, and redirects to the<br>employee search page without the deleted employee&#39;s ID. If the ID is missing,<br>it flashes an error message and redirects to the search page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403929-5923fce4-0358-470f-b4a0-7ad63fea851e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion of employee (Id 3, first name Art)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403998-add6ae26-0af2-4cb8-bac6-82eeb5abe851.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deletion of employee (Id 3, first name Art), it also shows the<br>success flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403059-f3927f25-213e-4470-8273-c2f58bf37f20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code defines a Flask route for deleting a company by its ID.<br>It retrieves the ID from the query string, updates the corresponding company&#39;s employees&#39;<br>company ID to NULL, deletes the company record from the database, flashes a<br>success or error message, and redirects to the company search page without the<br>deleted company&#39;s ID. If the ID is missing, it flashes an error message<br>and redirects to the search page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403657-cdbea025-548d-4564-98f6-fa3744caa49d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion of 1st employee Benton<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233403773-6f0c08d2-4c2d-4dac-ac29-cfac72cd2d95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deletion of 1st employee Benton, it shows the flash success message<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233481174-3f7ce44d-2f1c-48f2-b09c-fc4b43a4c551.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <div>This assignment involved creating a web application using Flask and MySQL, with features<br>such as adding new companies and employees, importing data from CSV files, and<br>searching and editing existing employee data. While working on this assignment, I learned<br>how to integrate MySQL with Flask using the PyMySQL library, and how to<br>use various Flask features such as blueprints, routing, templates, and flashing messages. I<br>also gained experience with SQL syntax for inserting, updating, and selecting data, and<br>learned about various best practices for web development such as validating user input<br>and handling errors.</div><div><br></div><div>One issue I faced while working on this assignment was formatting<br>the date and time in a way that was compatible with MySQL. I<br>solved this by using the datetime module in Python to format the date<br>and time as a string in the format "YYYY-MM-DD HH:MM:SS".&nbsp; Another issue I<br>faced was with sorting the table data by different columns in the database.<br>I solved this by using a conditional statement to check if the column<br>name and sorting order provided by the user were valid, and if so,<br>appending an ORDER BY clause to the SQL query. This allowed the user<br>to sort the data in ascending or descending order by any valid column.<br>One challenge I faced was figuring out how to properly structure the application<br>to avoid circular imports and make the code more modular. I solved this<br>by using Flask blueprints to organize the different parts of the application into<br>separate modules, each with its own set of routes and templates.</div><div><br></div><div>Overall, this was<br>a great learning experience and helped me develop my skills in web development<br>with Flask and MySQL.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/js2679" target="_blank">Grading</a></td></tr></table>
