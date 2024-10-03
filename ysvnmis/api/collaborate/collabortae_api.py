import base64
from flask import request, jsonify
from ysvnmis import *
from ysvnmis.dao.collaborate import insert_data, get_all_data, update_data

import base64

def add_base64_padding(base64_string):
    """Ensures the Base64 string has proper padding with '='"""
    return base64_string + '=='[(len(base64_string) % 4):]


@app.route("/api/create/collaborate", methods=["POST"])
def create_collaborate():
    data = request.get_json()

    # Extract fields from the form data
    job_title = data['job_title']
    start_time = data['start_time']
    end_time = data['end_time']
    priority = data['priority']
    content = data['content']
    with_person = data['with_person']
    transportation_mode = data['transportation_mode']
    next_appointment = data['next_appointment']
    referral = data['referral']
    cost = data['cost']
    notes = data['notes']

    try:

        attachment_base64 = data.get('attachment')

        if attachment_base64:

            padded_base64 = add_base64_padding(attachment_base64)


            attachment_bytes = base64.b64decode(padded_base64)

            with open('attachment_file.png', 'wb') as f:
                f.write(attachment_bytes)
        else:
            print("No attachment provided")
    except KeyError as e:
        print(f"Missing field: {str(e)}")
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return jsonify({"error": str(e)}), 500

    try:
        insert_data(job_title, start_time, end_time, priority, content, with_person,
                    transportation_mode, next_appointment, referral, cost, notes,
                    attachment_base64, 1)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Data inserted successfully!"}), 201



@app.route('/api/collaborate', methods=['GET'])
def get_collaborate():
    data = get_all_data()
    print(data)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data"}), 500


@app.route('/api/collaborate/<int:id>', methods=['PUT'])
def update_collaborate(id):
    data = request.json

    job_title = data.get('JobTitle')
    start_time = data.get('StartTime')
    end_time = data.get('EndTime')
    priority = data.get('Priority')
    content = data.get('Content')
    with_person = data.get('WithPerson')
    transportation_mode = data.get('TransportationMode')
    next_appointment = data.get('NextAppointment')
    referral = data.get('Referral')
    cost = data.get('Cost')
    notes = data.get('Notes')
    status = data.get('Status')

    attachment_base64 = data.get('AttachmentURL')


    update_data(id, job_title, start_time, end_time, priority, content, with_person, transportation_mode,
                next_appointment, referral, cost, notes, attachment_base64, status)

    return jsonify({'message': 'Data updated successfully!'}), 200
