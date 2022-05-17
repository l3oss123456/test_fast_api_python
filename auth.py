from hashlib import algorithms_available
import jwt


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    public_key = "public_key"

    return jwt.decode(
        access_token,
        key=public_key,
        algorithms=unverified_headers["alg"],
        audience=[]
    )
