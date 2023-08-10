import os
import gspread
import json


def write_in_googlesheet(data):
    if data == []: data = [['No se encontraron blogs asociados a esa categoria.']]
    credentials = {
        "type": "service_account",
        "project_id": "articulate-ego-395201",
        "private_key_id": "eb69072ea448e1842216139ab60fda3795077136",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCZsAquo+1cBVKN\nk6/+wAnkBGMRn/ImCQfM4dnscbc5du8dhYWXwhBwkv0aImp7MjSjlK834H71WCTl\nlDYlt1UDXJSuhOk9l6pnc2Ee4Yh2qKdU712mGMcJ/j2kzFEd9W/g+zJYdNl1LMkS\nnavOobwzEqvhC/+MVBLw+NuQNRKP9a97RgbPllxxYYncAi+NaPGeLMymK2VDyf19\nR1U43oyK41rMmpQN8/q++IFFwWCxrCyy05iQIVCw9NR0l1AwGg11sE+Syhq2WfQO\nggBFx1R1WG2w8KVDZweQMr5h0/XUsY9u1O9fVPQA+O73ZVUxK1vZzSNG3qXw5WSd\ncSdgumC/AgMBAAECggEAKQ5VtDS3jnsfhBG9lNTxb3fajVVIp2+HJWz6Pgdc1p2W\noDDQsOtXX/NsaORjxLhzRnXMXyV6VQlwheITmvzAWa8MSxjXhCw1igBRJCJExcol\nNXPidSIuXdWM2y73xoSQGC6S0v2YMAzARFhZktAzCgPFZc/CO1ckXjpk0T/UTx99\nHKqAA1nxeC8T9yv7wVD4RZ9LXPuLoIt94ZZ0U3ImR9H7Ad4ews1n/2sUsB0au4Wz\nGA91gYyma1LzHkFklIG/SXtXKPTa89Yts9Vq3sPMkrSAsy6DQ60I1/Tz+5ozdY5i\nVJDDGLK+C+MkDlaWxdULchOufE+G3k5ofOwTf2VFEQKBgQDYIra9V8F+uDeRRUP+\nX9pFOiaNDxjqNBVMyfc1enXirOb41CK+QTTz3H0sX8050juPvvUvMoO+7f9tauZJ\nrz6rQO3hunTtX4Gw5vVS6iylNA8/JlzVgvIKJ7RoHAj29WzlBUJJOCoD+5FJQ1mj\n6qe5ClTSYHccdvyhkId3KWDfzwKBgQC2CLhlHR2Ixe2z+jKBnGI/4nKoi4O8dVJg\n1Q5tYAPRSDDwEoXvvasMZl3SgEI1PMSLHe3YLkJGhdqZxFZ27avfF4NU7n4bNGwF\nJ96Uvu5bFOfzwcfh4XSFjJ0S76SYtauJBenGDzf/wLiefqwRe+rjJ3NWEbGPUB1Y\nw21xnHk8EQKBgEw9wpR79keLGB7ofhmnGkm9P4gWwUUsZi8WN1vn/NmfAELaIf9W\n5ST4rDcQ/EXfQR9tzvN9MDgToDyqrt1jMgoa907fBQwO2qLadcNv05vbB13RXIH8\nlQC8DMmEyizDWkxXVJCbfUa2YQOk/GP0DIIbgNxNJvcliew8HW0NbZzFAoGAc33c\n3+o1Ds3lHkcjPDBn9XhKnrzFfBBDj8QdPy+nvGQ9CFP4Pj7sAxX/eMp/Nx+y40C9\n4maXDf9mziBPa20nmodkf8JAqCn+TtcY1O6+c3M0JudPVfSg5QptrdH1cB3zEyB5\nTXviX5V6jLR5ny4rvKsO9hCLww1lUSfMjERmdsECgYBwnbaLKR10KA0goC/kADpm\niGTzuGIJ6wl7bVumfeYTYlklOSzg3SiFZbTID5tYcOZAibxHCdC7g9NRDwrnHBf5\nEukr2T9/f+kMAMTA51FGs+nBBt5utkomzFOI1BHs8adkY7J+XR4YE26yb3eNpKcY\n8DLEGiCf51BHSRNNlls7NQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "xepelin-prueba-tecnica@articulate-ego-395201.iam.gserviceaccount.com",
        "client_id": "111859071937923275805",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xepelin-prueba-tecnica%40articulate-ego-395201.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
    with open("/tmp/credentials.json", "w") as outfile:
        outfile.write(json.dumps(credentials))
    sa = gspread.service_account("/tmp/credentials.json")
    sh = sa.open_by_url("https://docs.google.com/spreadsheets/d/1eJSwV1ObnAsEmDaHVLAiEUB5MZ6RJolA5QO-CFMUE9I/")
    wks = sh.worksheet("Blogs")
    wks.clear()
    wks.update([['Titular', 'Categoria', 'Autor', 'Tiempo de lectura', 'Fecha de publicacion' ]] + data)
    return
