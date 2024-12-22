from __future__ import annotations

import numpy as np

DEFAULT_EPOCH = "19500101"


def epoch_for_np(epoch: str) -> str:
    """Format epoch string for numpy.

    Parameters
    ----------
    epoch : str

    Returns
    -------
    str

    """
    year = epoch[:4]
    month = epoch[4:6]
    day = epoch[6:8]
    return f"{year}-{month}-{day}"


class PTime:
    def __init__(
        self,
        w_sec: str | float | int,
        f_sec: float,
        epoch: str = DEFAULT_EPOCH,
    ):
        self.w_sec = str(int(w_sec))
        self.f_sec = f_sec
        self.epoch = epoch


def datetime_to_ptime(np_time: np.datetime64, epoch: str = DEFAULT_EPOCH) -> PTime:
    time_str = epoch_for_np(epoch)

    epoch_delta = (np_time - np.datetime64(time_str)) / np.timedelta64(1, "s")
    f_secs, w_secs = np.modf(epoch_delta)

    return PTime(w_secs, f_secs, epoch)


def add_one(number):
    return number + 1
