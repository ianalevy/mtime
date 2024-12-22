from __future__ import annotations

import numpy as np

DEFAULT_EPOCH = "19500101"


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

    @property
    def epoch_for_np(self) -> str:
        """Format epoch for numpy.

        Returns
        -------
        str

        """
        year = self.epoch[:4]
        month = self.epoch[4:6]
        day = self.epoch[6:8]
        return f"{year}-{month}-{day}"


def datetime_to_ptime(np_time: np.datetime64, epoch: str = DEFAULT_EPOCH) -> PTime:
    year = epoch[:4]
    month = epoch[4:6]
    day = epoch[6:8]
    time_str = f"{year}-{month}-{day}"

    epoch_delta = (np_time - np.datetime64(time_str)) / np.timedelta64(1, "s")
    f_secs, w_secs = np.modf(epoch_delta)

    return PTime(w_secs, f_secs, epoch)


def add_one(number):
    return number + 1
