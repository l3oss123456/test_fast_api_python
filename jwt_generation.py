from datetime import datetime
import jwt


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iat": now.timestamp(),
        # "exp": (now+timedelta(hours=24)).timestamp()
    }
    private_key = 'private_key'

    return jwt.encode(payload=payload, key=private_key, algorithms='RS256')
