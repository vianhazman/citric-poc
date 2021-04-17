from citric import Client
LS_URL = "http://localhost:8082/index.php/admin/remotecontrol"
with Client(LS_URL, 'admin', 'password') as client:

    surveys = client.list_surveys('admin')
    participants = [ {"email":"me@example.com","lastname":"Bond","firstname":"James"},{"email":"me2@example.com","attribute_1":"example"} ]
    for s in surveys:
        try:
            client.activate_tokens(s.get('sid'))
        except Exception as e:
            pass
        participants_response = client.add_participants(s.get('sid'), participants)
        for p in participants_response:
            res = {}
            res['survey_id'] = s.get('sid')
            res['surveyls_title'] = s.get('surveyls_title')
            res['url'] = f"http://localhost:8082/index.php/{s.get('sid')}/token={p.get('token')}"
            res['email'] = p.get('email')
            print(res)
