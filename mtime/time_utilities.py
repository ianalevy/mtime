from __future__ import annotations

from enum import Enum

import numpy as np


class Units(Enum):
    """Metric unit prefixes."""

    tera = 1e12
    giga = 1e9
    mega = 1e6
    kilo = 1e3
    milli = 1e-3
    micro = 1e-6
    nano = 1e-9
    pico = 1e-12


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
        w_sec: float | int,
        f_sec: float,
        epoch: str = DEFAULT_EPOCH,
    ):
        self.w_sec = int(w_sec)
        self.f_sec = f_sec
        self.epoch = epoch

    def change_epoch(self, new_epoch: str):
        """Update times for new epoch.

        Parameters
        ----------
        new_epoch : str

        """
        num_secs = (
            np.datetime64(epoch_for_np(self.epoch))
            - np.datetime64(
                epoch_for_np(new_epoch),
            )
        ) / np.timedelta64(1, "s")
        self.w_sec = self.w_sec + num_secs
        self.epoch = new_epoch

    def __sub__(self, other: PTime):
        self.w_sec = self.w_sec - other.w_sec
        self.f_sec = self.f_sec - other.f_sec

        return self

    @property
    def gtk_format(self) -> dict:
        """Format for GTK input.

        Returns
        -------
        dict

        """
        return {"w_sec": self.w_sec, "f_sec": self.f_sec}


def ptime_to_ticks(ptime: PTime) -> int:
    """Convert ptime to time ticks.

    Time ticks are number of nanoseconds.

    Parameters
    ----------
    ptime : PTime

    Returns
    -------
    int
        number of nanoseconds

    """
    w_ns = int(ptime.w_sec * 1e9)
    f_ns = int(ptime.f_sec * 1e9)

    return w_ns + f_ns


def datetime_to_ptime(np_time: np.datetime64, epoch: str = DEFAULT_EPOCH) -> PTime:
    time_str = epoch_for_np(epoch)

    epoch_delta = (np_time - np.datetime64(time_str)) / np.timedelta64(1, "s")
    f_secs, w_secs = np.modf(epoch_delta)

    return PTime(w_secs, f_secs, epoch)


def ptime_to_datetime(ptime: PTime, epoch: str = DEFAULT_EPOCH) -> np.datetime64:
    f_sec = int(ptime.f_sec * (1e9))

    return (
        np.datetime64(epoch_for_np(epoch))
        + np.timedelta64(ptime.w_sec, "s")
        + np.timedelta64(f_sec, "ns")
    )
