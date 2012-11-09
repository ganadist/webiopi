def make_cert(server_pem):
    import os
    certpem = os.path.join(os.path.dirname(__file__), 'cert.pem')
    priv = os.path.join(os.path.dirname(__file__), 'priv.pem')
    if not (os.path.isfile(certpem) and os.path.isfile(priv)):
        cmd = """openssl genrsa -out %(priv)s &&
            openssl req -new -key %(priv)s -out %(cert)s.csr &&
            openssl x509 -req -days 3650 -in %(cert)s.csr -signkey %(priv)s -out %(cert)s &&
            (openssl x509 -in %(cert)s; cat %(priv)s) > %(server)s"""%{'priv': priv, 'cert': certpem, 'server':server_pem}
        if os.system(cmd) != 0:
            assert False
