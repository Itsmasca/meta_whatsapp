import hashlib
import hmac


def generate_appsecret_proof(app_secret, access_token):
    app_secret_bytes = app_secret.encode('utf-8')
    access_token_bytes = access_token.encode('utf-8')

    hash_hmac = hmac.new(app_secret_bytes, access_token_bytes, hashlib.sha256)
    appsecret_proof = hash_hmac.hexdigest()

    return appsecret_proof


# Ejemplo de uso
app_secret = "34616442ac06fad067febe585b09df8d"  # Reemplaza con tu App Secret
access_token = "EAAHRCGz6XnkBO9KaMJAINRW7upyZA6jA8dzSOVlKGB8MyzEYpNE03fYldTZAwrmaTCdk9xprhjOPK3xIoIwceU92TNdt8hbRrqYnXWwGnvKuKFGf0Wp7Qd9JcBOaZChkh5EmtpaiNWU2bJ5pI5VsS1ckjZAhEj6fTKTIOozQahdh63SV9ncslSLHo03kewcXhgZDZD"  # Reemplaza con tu Access Token

appsecret_proof = generate_appsecret_proof(app_secret, access_token)
print("App Secret Proof:", appsecret_proof)
