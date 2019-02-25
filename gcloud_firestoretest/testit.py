from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

def main():
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

    users_ref = db.collection(u'users')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


if __name__ == "__main__":
    main()