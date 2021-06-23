
from flask import Flask,render_template,request
from google.cloud import datastore
import os



project_id = os.getenv('GCLOUD_PROJECT')

app=Flask(__name__)

datastore_client = datastore.Client(project_id)


def list_entities(quiz='1'):
    query = datastore_client.query(kind='Question10')
    #query.add_filter('quiz', '=', 'gcp')
    limit=20
    results =list(query.fetch(limit=limit))
    #print(results)
    for result in results:
        result['id'] = result.key.id
        print(result)
    return results



def save_question(question):
# TODO: Create a key for a Datastore entity
# whose kind is Question

    key = datastore_client.key('Question10')

# END TODO

# TODO: Create a Datastore entity object using the key

    q_entity = datastore.Entity(key=key)
    print(q_entity)

# END TODO

# TODO: Iterate over the form values supplied to the function

    for q_prop, q_val in question.items():

# END TODO

# TODO: Assign each key and value to the Datastore entity

        q_entity[q_prop] = q_val

# END TODO

# TODO: Save the entity

    datastore_client.put(q_entity)

# END TODO



@app.route('/')
def serve_home():
    return render_template('home.html',question={})



@app.route('/saved', methods=['GET', 'POST'])
def add_question():
    msg="msg"
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        data = request.form.to_dict(flat=True)
        print(data)
        save_question(data)
        msg="Record added successfully"
        return render_template('add.html',msg=msg)
    else:
        msg="We cannot add the record"
        return render_template('add.html',msg=msg)


@app.route('/client/',methods=["GET","POST"])
def fetch_employee():
    query = datastore_client.query(kind='Question10')
    limit=20
    times=query.fetch(limit=limit)
    return render_template('index.html',times=times)

"""
@app.route('/fetch',methods=["GET","POST"])
def fetch():
    query=datastore_client.query(kind="Question10")
    name=request.form.get('name')
    breakpoint()
    times=query.add_filter("name",'=',"rahul").fetch()
    print(times)
    return render_template
"""

  

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)


























