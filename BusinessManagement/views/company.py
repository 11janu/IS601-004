from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')


@company.route("/search", methods=["GET"])
def search():
    rows = []
    
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    query = """
    SELECT companies.id, companies.name, companies.address, companies.city, companies.country, companies.state, companies.zip, companies.website, COUNT(employees.id) as employees 
    FROM IS601_MP3_Companies companies LEFT JOIN IS601_MP3_Employees employees ON companies.id = employees.company_id 
    WHERE 1=1
    """
    group_by_query = " GROUP BY companies.id, companies.name, companies.address, companies.city, companies.country, companies.state, companies.zip, companies.website"
    
    
    args = {}
    
    allowed_columns = [("id", "Id"), ("name", "Name"), ("address", "Address"), ("city", "City"), ("country", "Country"), ("state", "State"), ("zip", "Zip"), ("website", "Website"), ("employees","Employees")]
    
    name = request.args.get("name")
    if name:
        name_filter = f"%{name}%"
        query += " AND companies.name LIKE %(name_filter)s"
        args["name_filter"] = name_filter
    
    country = request.args.get("country")
    if country:
        query += " AND companies.country = %(country)s"
        args["country"] = country
    
    state = request.args.get("state")
    if state:
        query += " AND companies.state = %(state)s"
        args["state"] = state
    
    query += group_by_query
    
    column = request.args.get("column")
    order = request.args.get("order")
    if column and order:
        if column in [col[0] for col in allowed_columns] and order.lower() in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    
    limit = request.args.get("limit")
    if limit:
        try:
            limit = int(limit)
            if limit < 1 or limit > 100:
                raise ValueError
        except ValueError:
            flash("Limit must be a number between 1 and 100", "danger")
        else:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
    else:
        query += " LIMIT 10"
    
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        flash("Error occurred", "danger")
    
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)


@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
       
        has_error = False # use this to control whether or not an insert occurs
        
        name = request.form.get("name")
        if not name:
            flash("Name is required", "danger")
            has_error = True
        
        address = request.form.get("address")
        if not address:
            flash("Address is required", "danger")
            has_error = True
        
        city = request.form.get("city")
        if not city:
            flash("City is required", "danger")
            has_error = True
        
        state = request.form.get("state")
        country = request.form.get("country")
        if not state:
            flash("State is required", "danger")
            has_error = True
        elif not is_valid_state(state, country):
            flash("Invalid state selected", "danger")
            has_error = True
        
        if not country:
            flash("Country is required", "danger")
            has_error = True
        elif not is_valid_country(country):
            flash("Invalid country selected", "danger")
            has_error = True
        
        zip_code = request.form.get("zip")
        if not zip_code:
            flash("Zipcode is required", "danger")
            has_error = True

        website = request.form.get("website")
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s);
                """, {"name": name, "address": address, "city": city, "state": state, "country": country, "zip": zip_code, "website": website})
                if result.status:
                    flash("Added Company successfully!", "success")
                    return redirect(url_for("company.add"))
            except Exception as e:
                print(str(e))
                flash("Error occurred", "danger")
        
    return render_template("add_company.html")

def is_valid_state(state_code, country_code):
    try:
        # country = pycountry.countries.get(alpha_2=country_code)
        states = pycountry.subdivisions.get(country_code=country_code)
        valid_states = [state.code for state in states]
        if country_code + '-' + state_code in valid_states:
            return True
        return False
    except (KeyError, AttributeError):
        return False

def is_valid_country(country_code):
    try:
        pycountry.countries.get(alpha_2=country_code)
        return True
    except KeyError:
        return False

@company.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    if not id: 
        flash("Company ID is required.", "danger")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {"id": id} 
            
            has_error = False # use this to control whether or not an insert occurs

            name = request.form.get("name")
            if not name:
                flash("Name is required", "danger")
                has_error = True
            else:
                data["name"] = name
            
            address = request.form.get("address")
            if not address:
                flash("Address is required", "danger")
                has_error = True
            else:
                data["address"] = address
            
            city = request.form.get("city")
            if not city:
                flash("City is required", "danger")
                has_error = True
            else:
                data["city"] = city
            
            state = request.form.get("state")
            country = request.form.get("country")
            if not state:
                flash("State is required", "danger")
                has_error = True
            elif not is_valid_state(state, country):
                flash("Invalid state selected", "danger")
                has_error = True
            else:
                state = pycountry.subdivisions.lookup(country +'-'+state)
                data["state"] = state.code.split('-')[1]
                
            # TODO edit-6 country is required (flash proper error message)
            if not country:
                flash("Country is required", "danger")
                has_error = True
            elif not is_valid_country(country):
                flash("Invalid country selected", "danger")
                has_error = True
            else:
                country = pycountry.countries.search_fuzzy(country)[0]
                print(country)
                data["country"] = country.alpha_2
            
            website = request.form.get("website")
            data["website"] = website
        
            zip_code = request.form.get("zip")
            if not zip_code:
                flash("Zipcode is required", "danger")
                has_error = True
            else:
                data["zip"] = zip_code
            
            if not has_error:
                try:
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET
                        name=%(name)s,
                        address=%(address)s,
                        city=%(city)s,
                        state=%(state)s,
                        country=%(country)s,
                        zip=%(zip)s,
                        website=%(website)s
                    WHERE
                        id=%(id)s
                    """, data)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash("Error occurred", "danger")
        row = {}
        try:
            result = DB.selectOne("SELECT * FROM IS601_MP3_Companies WHERE id=%s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            flash("Error occurred", "danger")
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    
    id = request.args.get("id")
    if id:
        try:
            DB.update("UPDATE IS601_MP3_Employees SET company_id = NULL WHERE company_id = %(id)s", {"id": id})
            result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %(id)s;", {"id": id})
            if result.status:
                flash("Deleted Company Successfully", "success")
        except Exception as e:
            flash("Error occured", "danger")

        args = {k: v for k, v in request.args.items() if k != "id"}
        return redirect(url_for("company.search", **args))
    else:
        flash("Company ID is required.", "danger")
        return redirect(url_for("company.search"))
    