import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import csv
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        print(file.filename)
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        if file.filename[-4:] != '.csv':
            flash('Only csv files are allowed!', "danger")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            # DON'T EDIT
            company_query = """
            INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website)
            """
            # DON'T EDIT
            employee_query = """
             INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, 
                        company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            reader = csv.DictReader(stream)
            
            company_required_fields = ['company_name', 'address', 'city', 'country', 'state', 'zip', 'web']
            employee_required_fields = ['first_name', 'last_name', 'email', 'company_name']

            for row in reader:
                all_fields_present = True

                for field in company_required_fields:
                    if field not in row and row[field]!='':
                        all_fields_present = False
                        break
                
                if all_fields_present:
                    company = {}
                    for field in company_required_fields:
                        if field == 'company_name':
                            new_key = 'name'
                        elif field == 'web':
                            new_key = 'website'
                        else:
                            new_key = field
                            
                        company[new_key] = row[field]
                    companies.append(company)
                
                all_fields_present = True

                for field in employee_required_fields:
                    if field not in row and row[field]!='':
                        all_fields_present = False
                        break
                if all_fields_present:
                    employee = {}
                    for field in employee_required_fields:
                        employee[field] = row[field]
                    employees.append(employee)
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    flash(f"Processed {len(companies)} companies", "message")
                    print(f"Processed {len(companies)} companies", "message")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                flash("No companies are Loaded", "info")
                # pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    flash(f"Processed {len(employees)} Employees", "message")
                    print(f"Processed {len(employees)} Employees", "message")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                 flash("No Emplopyees are Loaded", "info")
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                    traceback.print_exc()
                    flash("There was an error counting session queries", "danger")
    return render_template("upload.html")
