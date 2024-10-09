from flask import  request, jsonify
from ysvnmis import *
from ysvnmis.dao.collaborate import insert_data, get_all_data, update_data


@app.route("/api/create/collaborate", methods=["POST"])
def create_collaborate():
    """
    Create a new collaboration entry
    ---
    tags:
      - Collaboration
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - job_title
            - start_time
            - end_time
          properties:
            job_title:
              type: string
              description: The title of the job
            start_time:
              type: string
              description: The start time
            end_time:
              type: string
              description: The end time
            priority:
              type: string
              description: Priority of the job
            content:
              type: string
              description: Content description
            with_person:
              type: string
              description: Collaborating with
            transportation_mode:
              type: string
              description: Transportation mode
            next_appointment:
              type: string
              description: Next appointment
            referral:
              type: string
              description: Referral information
            cost:
              type: number
              description: The cost involved
            notes:
              type: string
              description: Additional notes
            attachment:
              type: string
              description: Base64 encoded attachment file
    responses:
      201:
        description: Collaboration created successfully
      500:
        description: Error while inserting data
    """
    data = request.get_json()
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
    attachment_base64 = data.get('attachment')

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
    """
    Get all collaboration data
    ---
    tags:
      - Collaboration
    responses:
      200:
        description: A list of collaboration data
      500:
        description: Error fetching data
    """
    data = get_all_data()
    print(data)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data"}), 500


@app.route('/api/collaborate/<int:id>', methods=['PUT'])
def update_collaborate(id):
    """
    Update collaboration entry
    ---
    tags:
      - Collaboration
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: Collaboration ID
      - in: body
        name: body
        schema:
          type: object
          properties:
            job_title:
              type: string
            start_time:
              type: string
            end_time:
              type: string
            priority:
              type: string
            content:
              type: string
            with_person:
              type: string
            transportation_mode:
              type: string
            next_appointment:
              type: string
            referral:
              type: string
            cost:
              type: number
            notes:
              type: string
            attachment:
              type: string
              description: Base64 encoded attachment
            status:
              type: integer
    responses:
      200:
        description: Collaboration updated successfully
      500:
        description: Error updating data
    """
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


