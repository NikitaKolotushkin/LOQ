import time

from .blueprint import meets_bp


@meets_bp.route('/time')
def get_current_time():
    return {'time': time.time()}
