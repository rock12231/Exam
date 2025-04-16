# app/utils/helpers.py

from flask_jwt_extended import get_jwt
# No longer need pendulum or specific timezones here

def format_datetime(dt):
    """Formats a naive datetime object as ISO string. Returns None if dt is None."""
    if dt is None:
        return None
    # isoformat() on a naive datetime produces string without timezone info
    return dt.isoformat()

# JWT helper functions (remain the same)
def get_current_user_id():
    jwt = get_jwt()
    user_info = jwt.get('user_info', {})
    return user_info.get('id')

def get_current_user_role():
    jwt = get_jwt()
    user_info = jwt.get('user_info', {})
    return user_info.get('role')

def get_current_user_claims():
    return get_jwt().get('user_info', {})